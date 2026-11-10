---
name: alcance
description: Pone a Claude a editar tus reels DENTRO de Edits para Mac (la app de vídeo de Instagram) y a dejarlos listos para subir desde ahí, también como reel de prueba. Comprueba el Mac, te guía para activar el Automation Server de Edits y conectarlo con Claude Code, y edita con reglas de calidad de editor - cortes que no se comen ninguna palabra, sin zooms, subtítulos y gráficos fuera del HUD de Instagram, nunca encima de tu cara (pantalla dividida si no cabe), colores naturales y final con respiro. Revisa fotogramas antes de exportar y te dice qué botones pulsar para publicar. Úsala cuando digan /alcance, «comenta ALCANCE», «edita mi reel en Edits», «Edits para Mac con Claude», «conecta Claude con Edits», «que Claude me edite dentro de Edits» o «subir el reel desde Edits».
---

# /alcance: Claude edita tus reels dentro de Edits y los subes desde ahí

Al terminar, el usuario tiene Edits conectado a Claude Code, su reel editado dentro de un proyecto de Edits (cortes
limpios, subtítulos, gráficos en su sitio), exportado a 1080×1920 y sabe exactamente qué pulsar para publicarlo desde
Edits, como reel normal o como reel de prueba.

Habla en español, cercano, corto y sin tecnicismos. Una pregunta cada vez. Ejecuta tú los comandos; lo único que hace
la persona es copiar su token de Edits (y nunca lo pega en el chat). Detalle de las reglas de edición:
`ref/reglas-de-calidad.md`. Publicar desde Edits: `ref/publicar.md`. `<skill>` = la carpeta de esta skill.

## Paso 0. Comprobar el Mac

```bash
bash <skill>/scripts/comprobar.sh
```

- **Mac con chip de Apple (M1 o posterior).** Edits para Mac no existe para Intel, Windows ni para el navegador. Si no
  lo tiene, díselo claro y para: puede seguir editando con el móvil, pero esta skill no le sirve.
- **Edits para Mac** (gratis, de Instagram: edits.instagram.com/desktop), en Aplicaciones, abierto y con su cuenta de
  Instagram iniciada.
- **Claude Code** en la Terminal o en la pestaña Code de la app de Claude para Mac. En claude.ai (navegador) no funciona.
- `ffmpeg` para medir los cortes (si falta: `brew install ffmpeg`, pide permiso antes).

## Paso 1. Activar el Automation Server de Edits (una vez)

Dile que, en Edits: **Edits › Configuración (o Ajustes, ⌘ ,) › Automation › Enable Automation Server**. Viene apagado.
Al encenderlo, Edits enseña un **Access token**: que lo copie y no se lo enseñe a nadie (ni en el chat, ni en un vídeo,
ni en una captura). Edits escucha solo en su Mac (127.0.0.1, puerto 19501).

## Paso 2. Conectar Claude Code con Edits (una vez)

La forma recomendada es el puente gratuito **insta-edits** (código abierto, MIT, no es de Meta ni de Anthropic):
guarda el token en el llavero del Mac y hace que Claude vea las herramientas del editor al abrir un proyecto (Edits
pasa de unas 32 herramientas en la pantalla de inicio a unas 274 con un proyecto abierto, y sin el puente Claude se
queda con las 32).

Dile que escriba en Claude Code, uno detrás de otro:

```
/plugin marketplace add faisalkhanzemi/insta-edits-for-claude
/plugin install insta-edits@insta-edits
```

Claude Code le pide el token con un recuadro que lo oculta: ahí lo pega. Si lo instalas tú desde la Terminal, no sale
ese recuadro: que luego escriba `/plugin configure insta-edits@insta-edits` y lo pegue ahí. Después, que **reinicie
Claude Code** y escriba `/mcp`: tiene que salir **edits** conectado.

Edits también trae un botón para copiar una línea de conexión para Claude Code con el token dentro. Funciona, pero deja
el token escrito en un archivo de configuración y Claude solo ve las herramientas de inicio; por eso preferimos el puente.

Para comprobarlo: pide la lista de proyectos de Edits. Si salen, está conectado.
Si falla: `bash <skill>/scripts/comprobar.sh`, que Edits esté abierto con el servidor encendido, y volver a meter el
token con `/plugin configure insta-edits@insta-edits` (si lo cambió en Edits, el viejo ya no vale).

## Paso 3. Preparar la toma

- Edits **solo abre archivos de la carpeta Películas** (`~/Movies`) y con la ruta completa
  (`/Users/<usuario>/Movies/...`, nunca `~`). Descargas y Escritorio los rechaza.
- Trabaja en `~/Movies/Reels con Edits/` con `Tomas/`, `Graficos/`, `Musica/` y `Exportados/`. Si la toma está en otro
  sitio, **cópiala** ahí (nunca la muevas ni la toques).
- Edits tiene que estar abierto todo el rato.

## Paso 4. Entrevista corta (una tanda, tu recomendación primero)

Mira antes `~/Movies/Reels con Edits/mis-reglas.md` (lo aprobado en reels anteriores) y no preguntes lo que ya sepas.

1. **La toma** (las más recientes de `Tomas/`) y **la palabra del CTA** si tiene («Comenta X»).
2. **Subtítulos:** palabra a palabra (recomendado) · frase corta · sin subtítulos. Elige con él un estilo de la lista de
   estilos de subtítulos que tenga Edits.
3. **Gráficos:** solo subtítulos · subtítulos + 3-5 rótulos o tarjetas (recomendado) · con pantalla dividida para
   enseñar cosas (capturas, listas, cifras).
4. **Música:** de la biblioteca de Edits (avísale: entonces la exportación final la hace él desde la ventana de Edits)
   · la suya (`Musica/`) · sin música.

Guárdalo en `~/Movies/Reels con Edits/<AAAA-MM-DD tema>/proyecto.json` para poder retomar.

## Paso 5. Descubrir las herramientas

Las herramientas de Edits **no están documentadas y cambian con cada versión**. Nunca supongas un nombre: búscalas
(ToolSearch con «edits»), y **vuelve a buscar después de abrir un proyecto** porque la lista cambia. Si el puente instaló
su skill `edits`, léela primero. Apunta en `proyecto.json` → `herramientas` la que uses para cada cosa (abrir proyecto,
importar, cortar o recortar, velocidad, texto, subtítulos, transformar o mover, transiciones, audio, vista previa,
exportar). Antes de cada pasada lee la línea de tiempo; después de cada cambio, vuelve a leerla para confirmarlo. Si una
herramienta falla, lee el error y busca otra: no reintentes a ciegas.

## Paso 6. Editar en pasadas (cada pasada acaba con una vista previa)

Antes de un cambio grande, duplica el proyecto. Reglas completas en `ref/reglas-de-calidad.md`; lo esencial:

1. **Cortes que no se comen ninguna palabra.** Transcribe (subtítulos automáticos de Edits o Whisper local si lo tiene)
   y marca lo que sobra: arranques fallidos, frases repetidas (se queda **la última toma buena entera**), muletillas y
   silencios. Luego mide dónde cortar con el audio, no con la transcripción:

   ```bash
   python3 <skill>/scripts/tramos.py "/Users/<usuario>/Movies/Reels con Edits/Tomas/toma.mp4" --pausa 0.25
   ```

   Te da los tramos que se quedan con un margen de 0,1 s de silencio a cada lado, y avisa si algún corte cae sobre voz.
   Enséñale la lista de cortes antes de aplicarlos en Edits. Después, vuelve a mirar cada unión: la palabra de antes y
   la de después tienen que salir enteras (con su última consonante). Nunca cortes la última palabra del vídeo: deja
   0,5-0,8 s de imagen en silencio al final.
2. **Ritmo:** velocidad 1,1× si lo quiere más ágil (no se nota y engancha más). Sin pausas muertas.
3. **Nada de zooms** ni punch-ins ni cambios de encuadre: un único encuadre todo el vídeo. Sin espejo salvo que lo pida.
   Color natural: como mucho bajar un poco la exposición; nada de filtros de cine, viñetas ni desaturar.
4. **Subtítulos** debajo de la barbilla y dentro de la zona que se ve (abajo).
5. **Rótulos y tarjetas** con lo que dice en ese momento (una idea cada vez, legible en 1 s): gancho en los 2 primeros
   segundos, cifras, listas, el CTA «Comenta X» al final (texto, sin dibujar ningún botón).
6. **Pantalla dividida** cuando lo que quiere enseñar no cabe sin taparle la cara (ver abajo).
7. **Sonido:** voz alta y clara; música por debajo de la voz (unos -18 dB), sube un poco cuando no habla y termina con
   fundido.

### El HUD de Instagram (lo que tapa la app) y la cara

En un vídeo de 1080×1920 (en coordenadas de 0 a 1 entre paréntesis, que es como suele trabajar Edits):

- **Arriba, y < 250 (0,13):** barra de estado y cabecera de Reels. Nada importante ahí.
- **Abajo, y > 1500 (0,78):** nombre, descripción y audio.
- **Derecha, x > 950 (0,88) entre y 1000 y 1700:** los botones de me gusta, comentar, compartir.
- **Todo el texto entre y 250 y 1150 (0,13-0,60).** Subtítulos en plano normal hacia y 1110 (0,58).
- **La cara entera** (boca y barbilla incluidas) por encima de y 1500 (0,78), y **nada encima de la cara ni del pelo.**

**Pantalla dividida:** si un gráfico no cabe sin pisarle la cara, panel claro arriba (alto 1000 px, contenido entre
y 250 y 900, subtítulos dentro hacia y 935) y la cámara bajada unos 480 px (un 25 %), con una transición suave al entrar
y al salir. Con las herramientas de transformar o fotogramas clave de Edits si las tiene; si no, haz el panel en código
como vídeo vertical (ver `ref/reglas-de-calidad.md`) e impórtalo como capa. En plano normal, solo él y los subtítulos.

Estilo de los gráficos (si no tiene uno propio): limpio tipo Apple, panel casi blanco (#FBFBFD → #F2F2F5), tarjetas
blancas con sombra suave, letra SF Pro o Inter, pastillas negras (#1D1D1F) para lo importante y entradas suaves.

## Paso 7. Revisar antes de exportar

Saca 6-8 fotogramas de la vista previa (gancho, cada gráfico, cada pantalla dividida, el CTA y el final) y míralos con
el HUD en la cabeza: texto legible, nada en las zonas tapadas, nada encima de la cara. Escucha el principio, cada corte y
el final. Si algo falla, arréglalo antes de seguir. No le enseñes nada que no hayas mirado tú.

## Paso 8. Exportar y publicar desde Edits

- Exporta a 1080×1920 en `Exportados/`. **Si la música es de la biblioteca de Edits, no exportes tú** (sale muda desde
  la automatización): que pulse él Exportar en la ventana de Edits.
- **Publicar no se hace por la conexión** (no hay herramienta para eso). Se hace en la app, en 1-2 minutos:
  **Exportar → Compartir en Instagram → escribe la descripción → (opcional) activa «Reel de prueba» → Compartir.**
  Detalle en `ref/publicar.md`. Recomiéndale una descripción corta: `Comenta PALABRA ⤵️`.
- **Reel de prueba (trial):** sí se puede desde Edits. Solo lo ve gente que no le sigue y él decide si pasa a su perfil.
- **Programar: Edits para Mac no programa.** Publica en el momento. Si quiere programar, que exporte el vídeo y lo
  programe con otra herramienta (Meta Business Suite o la que use).
- **Nunca publiques tú** sin que te lo pida para ese vídeo en concreto. Si tiene el control del ordenador activado en
  Claude y te pide que pulses los botones, enséñale antes la descripción y la cuenta.

## Al terminar

Guarda en `~/Movies/Reels con Edits/mis-reglas.md` lo que haya aprobado (estilo de subtítulos, colores, letra, ritmo,
lo que no le gustó) para el próximo reel. Resumen en 4-6 líneas: qué se cortó, el estilo, la música, dónde está el
exportado y los botones para publicarlo. Ofrece cambios concretos.

## Reglas

- **El token de Edits nunca en el chat**, ni en archivos, ni en commits.
- No borres proyectos de Edits sin preguntar.
- Si la conexión cae (Edits cerrado), espera a que vuelva; no repitas acciones que quizá ya se hicieron: vuelve a leer
  la línea de tiempo.
- No inventes herramientas ni botones. Si algo de Edits no existe en su versión, díselo y busca otra forma.
- El puente es de un tercero y Edits cambia: si deja de ir tras una actualización, actualiza el plugin
  (`/plugin`) y, si sigue sin ir, espera a la nueva versión del puente.
