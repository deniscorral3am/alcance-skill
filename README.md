# Alcance · Claude edita tus reels dentro de Edits (y los subes desde ahí)

Edits, la app de vídeo de Instagram, ya está en Mac y trae una puerta para que una IA la maneje (el Automation Server).
Esta skill conecta Claude Code a esa puerta y le da las instrucciones con las que edito mis reels: Claude corta,
subtitula, pone rótulos y exporta **dentro de tu proyecto de Edits**, y tú lo subes desde la app, también como reel de
prueba.

| Paso | Qué hace |
|---|---|
| 0 | Comprueba tu Mac (chip de Apple, Edits abierto, servidor encendido, puente instalado) |
| 1-2 | Te guía para encender el Automation Server y conectar Claude Code (el token nunca pasa por el chat) |
| 3-4 | Prepara la toma en Películas y te hace 4 preguntas (toma, subtítulos, gráficos, música) |
| 5-6 | Edita en pasadas: cortes que no se comen palabras, sin zooms, subtítulos y gráficos fuera del HUD de Instagram, nunca encima de tu cara (pantalla dividida si no cabe) |
| 7 | Revisa fotogramas y cortes antes de exportar |
| 8 | Exporta a 1080×1920 y te dice qué pulsar para publicar desde Edits, como reel normal o de prueba |

Hecha por Denís Corral · [@deniscorralvillarraso](https://instagram.com/deniscorralvillarraso) · [Sell Your AI](https://sellyourai.io)

## Instalación

```bash
git clone https://github.com/deniscorral3am/alcance-skill ~/.claude/skills/alcance
```

Abre Claude Code y escribe `/alcance`.

¿Sin instalar nada? Abre [`PROMPT.md`](PROMPT.md) (el documento «Cómo poner a tu Claude a editar tus reels dentro de
Edits»), haz los 3 pasos y pega el recuadro en Claude Code.

## Qué necesitas

- Un **Mac con chip de Apple** (M1 o posterior).
- **Edits para Mac** (gratis, edits.instagram.com/desktop) con tu cuenta de Instagram.
- [Claude Code](https://claude.com/claude-code) en la Terminal o en la pestaña Code de la app de Claude.
- El puente gratuito [insta-edits](https://github.com/faisalkhanzemi/insta-edits-for-claude) (se instala desde Claude
  Code con `/plugin`).
- `ffmpeg` para medir los cortes (`brew install ffmpeg`).

## Bueno saber

- **Publicar y programar no van por la conexión.** Publicar se hace con los botones de Edits (Exportar → Compartir en
  Instagram), y Edits para Mac **no programa**: publica en el momento.
- La música de la biblioteca de Edits sale muda si exporta la IA: esa exportación la haces tú desde la ventana de Edits.
- Edits solo abre vídeos de la carpeta Películas.
- Las herramientas de Edits no están documentadas y cambian con cada versión; el puente es de un tercero. Si algo deja
  de ir tras una actualización, toca esperar a la nueva versión.

## Lo que hay dentro

- `SKILL.md`: las instrucciones para Claude.
- `PROMPT.md`: el documento para pegar en Claude sin instalar nada.
- `ref/reglas-de-calidad.md`: las reglas de edición (cortes, HUD, pantalla dividida, gráficos, sonido).
- `ref/publicar.md`: exportar y publicar desde Edits, reel de prueba y qué no hace.
- `scripts/comprobar.sh`: comprueba el Mac y la conexión.
- `scripts/tramos.py`: mide en el audio dónde cortar sin comerse palabras.

Edits e Instagram son marcas de Meta; Claude, de Anthropic.

## Licencia

MIT
