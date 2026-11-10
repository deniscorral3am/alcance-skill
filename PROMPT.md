# Cómo poner a tu Claude a editar tus reels dentro de Edits (y subirlos desde ahí)

Por Denís Corral · @deniscorralvillarraso en Instagram · [Sell Your AI](https://sellyourai.io)

Edits, la app de vídeo de Instagram, ya tiene versión para Mac, y trae una puerta para que una IA la maneje: el
**Automation Server**. Con eso, Claude corta, subtitula, pone rótulos y exporta **dentro de tu proyecto de Edits**, y tú
lo subes desde la propia app, también como reel de prueba.

Lo que marca la diferencia no es la herramienta, son las instrucciones. Abajo tienes las mías: las reglas con las que
edito mis reels (cortes que no se comen palabras, nada encima de la cara, nada debajo de los botones de Instagram).

## Lo que necesitas

- Un **Mac con chip de Apple** (M1 o posterior). En Intel o Windows no hay Edits para ordenador.
- **Edits para Mac** (gratis): edits.instagram.com/desktop, con tu cuenta de Instagram iniciada.
- **Claude Code** (en la Terminal o en la pestaña Code de la app de Claude para Mac, con un plan de pago de Claude).
  En claude.ai desde el navegador no funciona.

## Los 3 pasos que haces tú (una sola vez, 5 minutos)

1. **Enciende la puerta.** En Edits: menú **Edits › Configuración** (⌘ ,) › pestaña **Automation** › activa
   **Enable Automation Server**. Copia el **Access token**. Es como una contraseña: no lo pegues en el chat ni lo
   enseñes en un vídeo.
2. **Conecta Claude.** En Claude Code escribe, de uno en uno:
   ```
   /plugin marketplace add faisalkhanzemi/insta-edits-for-claude
   /plugin install insta-edits@insta-edits
   ```
   Te pide el token en un recuadro que lo oculta: pégalo ahí. Es un puente gratuito y de código abierto (no es de
   Instagram ni de Anthropic) que guarda el token en el llavero de tu Mac y deja a Claude usar todo el editor.
3. **Reinicia Claude Code** y escribe `/mcp`: tiene que salir **edits** conectado.

Después, deja tu vídeo en la carpeta **Películas** (Edits no abre vídeos de Descargas ni del Escritorio), deja Edits
abierto y pega en Claude Code todo lo que hay dentro del recuadro de abajo.

¿Quieres la versión completa (con el script que mide los cortes)? Instala la skill:
`git clone https://github.com/deniscorral3am/alcance-skill ~/.claude/skills/alcance` y escribe `/alcance`.

---

```
Quiero que edites mis reels DENTRO de Edits para Mac (la app de Instagram) usando su conexión (las herramientas
«edits») y que me los dejes listos para subir desde Edits. Háblame en español, corto y sin tecnicismos, y pregúntame
una sola cosa cada vez. Nunca me pidas el token de Edits por el chat.

1 · COMPRUEBA EL MAC Y LA CONEXIÓN
- Comprueba que es un Mac con chip de Apple (uname -m = arm64), que Edits está abierto y que su servidor responde
  (curl a http://127.0.0.1:19501/mcp: cualquier respuesta que no sea 000 vale), y que tienes ffmpeg.
- Busca tus herramientas de Edits (busca «edits»). Si no hay, dime qué falta: Edits › Configuración › Automation ›
  Enable Automation Server, el plugin insta-edits@insta-edits y reiniciar Claude Code.
- Las herramientas de Edits no están documentadas y cambian: nunca supongas un nombre. Vuelve a buscarlas después de
  abrir un proyecto (con un proyecto abierto aparecen muchas más). Apunta cuál usas para cada cosa.

2 · PREPARA LA TOMA
- Edits solo abre archivos de ~/Movies y con la ruta completa (/Users/<usuario>/Movies/...). Trabaja en
  ~/Movies/Reels con Edits/ (Tomas, Graficos, Musica, Exportados). Si mi vídeo está en otro sitio, cópialo ahí; no lo
  muevas ni lo toques.
- Pregúntame en una tanda: qué toma, la palabra del CTA («Comenta X»), subtítulos (palabra a palabra / frase corta /
  sin), cuántos gráficos (solo subtítulos / 3-5 rótulos o tarjetas / con pantalla dividida para enseñar cosas) y
  música (biblioteca de Edits / la mía / sin). Guarda mis respuestas en un proyecto.json para poder retomar.
- Crea el proyecto en Edits, vertical 9:16, e importa la toma. Antes de cada cambio grande, duplica el proyecto.

3 · CORTES QUE NO SE COMEN NINGUNA PALABRA
- Transcribe (subtítulos automáticos de Edits o Whisper en local) y marca lo que sobra: arranques fallidos, frases
  repetidas (quédate con la ÚLTIMA toma buena, entera), muletillas y silencios de más de 0,25 s.
- No te fíes de dónde dice la transcripción que acaba una palabra: se come las consonantes finales. Mide el final real
  con el audio (ffmpeg, energía en pasos de 10 ms hasta el ruido de fondo) y deja 80-120 ms de margen. Si la palabra
  siguiente va pegada, usa otra toma o corta en el punto más bajo de energía DESPUÉS de la palabra completa.
- Enséñame la lista de cortes antes de aplicarlos. Después revisa cada unión: la palabra de antes y la de después
  tienen que oírse enteras. El gancho (la primera frase) va entero.
- El final: la última palabra completa y después 0,5-0,8 s de imagen en silencio. Nunca cortes la última palabra.
- Si quiero más ritmo, velocidad 1,1×.

4 · IMAGEN
- Nada de zooms, punch-ins ni cambios de encuadre: un único encuadre todo el vídeo. Sin espejo salvo que te lo pida.
- Color natural: como mucho baja un poco la exposición. Nada de filtros de cine, viñetas ni desaturar.

5 · EL HUD DE INSTAGRAM Y MI CARA (en 1080×1920; entre paréntesis, de 0 a 1)
- Arriba, y < 250 (0,13): lo tapa la barra de estado y la cabecera de Reels.
- Abajo, y > 1500 (0,78): lo tapan mi nombre, la descripción y el audio.
- Derecha, x > 950 (0,88) entre y 1000 y 1700: los botones.
- Todo el texto entre y 250 y 1150 (0,13-0,60). Subtítulos en plano normal hacia y 1110 (0,58), bajo la barbilla.
- Mi cara entera (boca y barbilla) por encima de y 1500, y NADA encima de mi cara ni de mi pelo.
- Si algo no cabe sin taparme: PANTALLA DIVIDIDA. Panel claro arriba (alto 1000 px, contenido entre y 250 y 900,
  subtítulos dentro hacia y 935) y mi cámara bajada unos 480 px (un 25 %), con transición suave al entrar y al salir.
  Hazlo con transformar y fotogramas clave de Edits; si no se puede, haz ese tramo en código como vídeo vertical e
  impórtalo como capa. En plano normal, solo yo y los subtítulos.

6 · GRÁFICOS Y SONIDO
- Cada palabra clave que digo, algo en pantalla en ese momento: una cifra en grande, una lista que entra punto a punto
  con mi voz, el logo de la marca de la que hablo. Una idea cada vez, legible en 1 segundo.
- Gancho visual en los 2 primeros segundos (dentro de la zona de texto). Al final, el CTA «Comenta PALABRA» con una
  flecha hacia abajo, como texto: nunca dibujes un botón.
- Estilo si no tengo uno: limpio tipo Apple, panel casi blanco, tarjetas blancas con sombra suave, SF Pro o Inter,
  pastillas negras para lo importante, entradas suaves.
- Voz alta y clara. Música por debajo (unos -18 dB) con fundido al final.

7 · REVISA ANTES DE EXPORTAR
- Saca fotogramas de la vista previa (gancho, cada gráfico, cada pantalla dividida, CTA y final) y míralos con el HUD
  en la cabeza. Escucha el principio, cada corte y el final. Arregla lo que falle antes de enseñármelo.

8 · EXPORTAR Y SUBIR DESDE EDITS
- Exporta a 1080×1920 en Exportados/. Si la música es de la biblioteca de Edits, no exportes tú (sale muda): dime que
  pulse Exportar en la ventana de Edits.
- Publicar no se puede por la conexión: lo hago yo en la app. Dime los pasos: Exportar → Compartir en Instagram →
  descripción → (si quiero) activar «Reel de prueba» → Compartir. Descripción recomendada: «Comenta PALABRA ⤵️».
- Recuérdame que Edits para Mac no programa: publica en el momento. Si quiero programarlo, que exporte y use otra
  herramienta.
- Nunca publiques tú sin que te lo pida para ese vídeo.

9 · AL TERMINAR
- Guarda en ~/Movies/Reels con Edits/mis-reglas.md lo que te haya aprobado (subtítulos, colores, letra, ritmo, lo que
  no me gustó) y léelo la próxima vez antes de preguntarme nada.
- Resúmeme en 4-6 líneas qué has cortado, el estilo, la música y dónde está el exportado.

Empieza por el paso 1.
```

---

Edits e Instagram son marcas de Meta; Claude, de Anthropic. El puente insta-edits es un proyecto independiente de código
abierto (github.com/faisalkhanzemi/insta-edits-for-claude). Si Edits se actualiza, puede dejar de ir un tiempo.
