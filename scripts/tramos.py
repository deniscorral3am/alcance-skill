#!/usr/bin/env python3
"""Dice dónde cortar una toma sin comerse ninguna palabra.

Mide la energía del audio en ventanas de 10 ms (no se fía de la transcripción), encuentra los silencios más largos que
--pausa y devuelve los tramos con voz que se quedan, con --margen de silencio a cada lado. Avisa si algún corte cae
sobre voz y deja al final --cola segundos de respiro.

Uso:
  python3 tramos.py "/Users/tu/Movies/Reels con Edits/Tomas/toma.mp4" [--pausa 0.25] [--margen 0.1] [--cola 0.6]
                    [--quitar "5.2-7.8,40-44.5"] [--json salida.json]

--quitar: trozos que sobran (arranques fallidos, frases repetidas) en segundos del vídeo original; se ajustan solos
al silencio más cercano para no cortar una palabra.
Solo necesita ffmpeg y Python 3 (sin librerías extra).
"""
import argparse
import array
import json
import math
import subprocess
import sys

SR = 16000
PASO = 0.01  # 10 ms
N = int(SR * PASO)


def energia(ruta):
    cmd = ["ffmpeg", "-v", "error", "-i", ruta, "-vn", "-ac", "1", "-ar", str(SR), "-f", "s16le", "-"]
    try:
        crudo = subprocess.run(cmd, capture_output=True, check=True).stdout
    except FileNotFoundError:
        sys.exit("Falta ffmpeg (en Mac: brew install ffmpeg)")
    except subprocess.CalledProcessError as e:
        sys.exit("ffmpeg no pudo leer el audio: " + e.stderr.decode(errors="ignore")[-300:])
    m = array.array("h")
    m.frombytes(crudo[: len(crudo) // 2 * 2])
    if sys.byteorder == "big":
        m.byteswap()
    db = []
    for i in range(0, len(m) - N + 1, N):
        s = 0
        for v in m[i:i + N]:
            s += v * v
        rms = math.sqrt(s / N) / 32768.0
        db.append(20 * math.log10(rms) if rms > 0 else -100.0)
    return db


def umbral(db):
    o = sorted(db)
    fondo = o[int(len(o) * 0.10)]  # el 10 % más bajo ≈ ruido de fondo
    voz = o[int(len(o) * 0.90)]
    # a medio camino, pero nunca más de 30 dB por debajo de la voz
    return max(fondo + (voz - fondo) * 0.35, voz - 30), fondo, voz


def silencios(db, th, minimo):
    res, ini = [], None
    for i, v in enumerate(db + [100.0]):
        if v < th and ini is None:
            ini = i
        elif v >= th and ini is not None:
            if (i - ini) * PASO >= minimo:
                res.append((ini * PASO, i * PASO))
            ini = None
    return res


def rangos(txt):
    out = []
    for p in (txt or "").split(","):
        p = p.strip()
        if p:
            a, b = p.split("-")
            out.append((float(a), float(b)))
    return out


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("video")
    ap.add_argument("--pausa", type=float, default=0.25, help="silencio mínimo que se quita (s)")
    ap.add_argument("--margen", type=float, default=0.1, help="silencio que se deja a cada lado de la voz (s)")
    ap.add_argument("--cola", type=float, default=0.6, help="respiro en silencio al final (s)")
    ap.add_argument("--quitar", default="", help='trozos que sobran, p. ej. "5.2-7.8,40-44.5"')
    ap.add_argument("--json", default="", help="guardar los tramos en este archivo")
    a = ap.parse_args()

    db = energia(a.video)
    if not db:
        sys.exit("El vídeo no tiene audio")
    dur = len(db) * PASO
    th, fondo, voz = umbral(db)
    sil = silencios(db, th, a.pausa)

    # tramos con voz entre silencios
    voz_r, t = [], 0.0
    for s0, s1 in sil:
        if s0 > t:
            voz_r.append((t, s0))
        t = s1
    if t < dur:
        voz_r.append((t, dur))
    tramos = [[round(max(0.0, v0 - a.margen), 2), round(min(dur, v1 + a.margen), 2)]
              for v0, v1 in voz_r if v1 - v0 >= 0.06]

    # quitar trozos: cada borde se lleva al silencio más cercano
    def a_silencio(x):
        mejor = None
        for s0, s1 in sil:
            c = min(max(x, s0), s1)
            if mejor is None or abs(c - x) < abs(mejor - x):
                mejor = c
        if mejor is None or abs(mejor - x) > 0.6:
            avisos.append(f"no hay silencio cerca de {x:.2f} s: ese corte puede comerse voz, revísalo a oído")
            return x
        return mejor

    avisos = []
    for q0, q1 in rangos(a.quitar):
        q0, q1 = a_silencio(q0), a_silencio(q1)
        nuevos = []
        for i0, i1 in tramos:
            if i1 <= q0 or i0 >= q1:
                nuevos.append([i0, i1])
                continue
            if i0 < q0:
                nuevos.append([i0, round(q0, 2)])
            if i1 > q1:
                nuevos.append([round(q1, 2), i1])
        tramos = [x for x in nuevos if x[1] - x[0] > 0.05]

    # respiro al final: alarga el último tramo si hay silencio detrás
    if tramos:
        ult = tramos[-1]
        ult[1] = round(min(dur, ult[1] - a.margen + a.cola), 2)

    # avisos: algún borde de corte sobre voz
    for i0, i1 in tramos:
        for borde, nombre in ((i0, "inicio"), (i1, "final")):
            if borde in (0.0, round(dur, 2)):
                continue
            k = min(len(db) - 1, int(borde / PASO))
            if db[k] >= th:
                avisos.append(f"el {nombre} del tramo {i0}-{i1} cae sobre voz ({db[k]:.0f} dB): revísalo a oído")
    if tramos and tramos[-1][1] >= dur - 0.05 and db[-1] >= th:
        avisos.append("el vídeo acaba hablando: no hay respiro al final, busca una cola en silencio")

    total = sum(b - a_ for a_, b in tramos)
    print(f"Duración {dur:.2f} s → {total:.2f} s en {len(tramos)} tramos "
          f"(fondo {fondo:.0f} dB, voz {voz:.0f} dB, umbral {th:.0f} dB)")
    for i, (i0, i1) in enumerate(tramos, 1):
        print(f"  {i:>2}. {i0:7.2f} → {i1:7.2f}  ({i1 - i0:.2f} s)")
    for av in avisos:
        print("  ⚠ " + av)
    if a.json:
        with open(a.json, "w") as f:
            json.dump({"video": a.video, "duracion": round(dur, 2), "tramos": tramos, "avisos": avisos}, f,
                      ensure_ascii=False, indent=2)
        print("Guardado en " + a.json)


if __name__ == "__main__":
    main()
