# Reglas de calidad (las de Denis)

Son las reglas con las que se editan los reels de Sell Your AI. No dependen de Edits: valen para cualquier editor.
Lo que pida el usuario manda; si algo choca con estas reglas, avísale una vez y haz lo que diga.

## 1. Ninguna palabra cortada

- **Se corta solo en silencio real.** Un corte «apretado» quita silencio, nunca voz.
- **No te fíes de dónde dice la transcripción que acaba una palabra.** Whisper y los subtítulos automáticos se comen las
  consonantes finales (la «r» de «sector», la «s» de un plural). Busca el final real con el audio, en pasos de 10 ms,
  hasta que la energía baja al ruido de fondo, y deja **80-120 ms de margen**. `scripts/tramos.py` lo hace.
- Si la palabra siguiente va pegada (sin silencio entre las dos), no cortes ahí: usa otra toma o corta en el punto más
  bajo de energía **después** de la palabra completa.
- **De cada frase repetida, la última toma buena, entera.** Fuera arranques fallidos («y el, y el…»), muletillas largas
  y lo que dice fuera de guion.
- **Revisa cada unión** después de cortar: la palabra de antes y la de después tienen que oírse enteras. Si al
  transcribir la unión sola sale una palabra de más, de menos o rara, hay una traba escondida: mueve el corte.
- **El gancho (la primera frase) va entero, tal cual.**
- **El final:** la última palabra completa (medida con el audio) y después **0,5-0,8 s de imagen en silencio**. Si
  justo después sigue hablando, usa como cola un trozo en el que esté callado.
- Pausas: 0,2-0,25 s entre frases da ritmo de reel; 0,35 s, natural. Velocidad 1,1× en reels si quiere más ritmo.

## 2. Imagen

- **Nada de zooms**: ni punch-ins, ni zooms lentos, ni cambios de encuadre que parezcan un zoom. Un encuadre por plano
  todo el vídeo.
- **Sin espejo** salvo que el usuario lo pida (o que su cámara grabe girada).
- **Color natural.** Como mucho, bajar un poco la exposición si está quemado. Nada de etalonaje de cine (teal & orange),
  viñetas ni desaturar: la piel se ve «demacrada».
- No toques sus planos (desenfocar, tapar, sustituir) si no lo pide.

## 3. El HUD de Instagram (en 1080×1920)

| Zona | Píxeles | En 0-1 | Qué tapa |
|---|---|---|---|
| Arriba | y < 250 | y < 0,13 | barra de estado y cabecera de Reels |
| Abajo | y > 1500 | y > 0,78 | nombre, descripción, audio |
| Derecha | x > 950, y 1000-1700 | x > 0,88 | botones (me gusta, comentar, compartir) |
| Texto | y 250-1150, x < 940 | y 0,13-0,60 | aquí sí |
| Subtítulos (plano normal) | y ≈ 1110 | ≈ 0,58 | bajo la barbilla |

Y la **cara entera** (boca y barbilla) por encima de y 1500.

**Nunca encima de la cara ni del pelo.** Si algo no cabe sin pisarla → pantalla dividida.

## 4. Pantalla dividida

- Panel claro arriba, de 1080×1000: contenido entre y 250 y 900, subtítulos dentro del panel hacia y 935.
- La cámara baja unos **480 px** (un 25 % del alto) con una transición suave (0,4-0,5 s, curva de entrada y salida) y
  vuelve igual al terminar. El panel entra con la misma curva.
- En Edits: con transformar/posición y fotogramas clave del clip de cámara, y el panel como capa importada.
- Si Edits no deja mover el clip, haz el tramo entero en código: un vídeo 1080×1920 con el panel arriba y la cámara
  bajada (por ejemplo con ffmpeg `pad` + `overlay`, o con HTML renderizado), guárdalo en `Graficos/` e impórtalo encima
  de ese tramo. Comprueba que la boca no se descuadra con el audio.
- En plano normal, solo él y los subtítulos.

## 5. Gráficos

- **Cada palabra clave que dice → algo en pantalla en ese instante**: una cifra → contador o tarjeta con el número; una
  lista → que entre punto a punto con la voz; una marca → su logo real (solo si habla de ella); algo que niega → tachado.
- Una idea cada vez, legible en 1 segundo, sin saturar.
- Gancho visual en los 2 primeros segundos (por ejemplo, «logo + logo» o el titular de la promesa) dentro de la zona
  de texto, nunca en la cabecera.
- Estilo por defecto (si no tiene marca propia): limpio tipo Apple. Panel #FBFBFD → #F2F2F5, tarjetas blancas con
  sombra suave, SF Pro o Inter, pastillas negras #1D1D1F, entradas con un poco de desenfoque y muelle, filas que entran
  escalonadas. Nada de azul marino ni degradados chillones.
- Si un gráfico se hace en código: 1080×1920 a 30 fps, MOV con transparencia (ProRes 4444,
  `-c:v prores_ks -profile:v 4 -pix_fmt yuva444p10le`). Si Edits no respeta la transparencia, hazlo a pantalla completa.
- **CTA:** texto «Comenta PALABRA» con una flecha hacia abajo, en la zona de texto. Nunca dibujes un botón dentro del vídeo.

## 6. Sonido

- La voz manda: alta, clara y sin picos. Si suena a sala, recomiéndale limpiarla (por ejemplo Adobe Podcast Enhance).
- Música por debajo de la voz (unos -18 dB), un poco más alta donde no habla, fundido de 1 s al final. Solo música que
  tenga derecho a usar: la de la biblioteca de Edits o la suya.
- Efectos con moderación: un «whoosh» suave al entrar en pantalla dividida, un «pop» en una cifra importante.

## 7. Revisar antes de entregar

- Fotogramas del gancho, de cada gráfico, de cada pantalla dividida, del CTA y del final, mirados con la tabla del HUD.
- Escuchar el principio, cada unión y el final.
- Nunca entregar algo que no hayas mirado.
