# Qué está comprobado

- 9/11/2026, en el Mac de Denis (M-series, macOS 26): Edits para Mac con el Automation Server encendido (puerto 19501),
  el plugin `insta-edits@insta-edits` 0.1.1 con el token en el llavero (`/plugin configure`), `/mcp` con edits
  conectado. Unas 32 herramientas en inicio y 274 con un proyecto abierto. Importa solo desde `~/Movies` con ruta
  absoluta.
- 9/11/2026: ninguna de las 274 herramientas publica, comparte, programa ni hace reels de prueba; solo exporta.
  Publicado desde la app (Exportar → Compartir en Instagram → descripción → «Reel de prueba» con graduación Manual →
  Compartir): 3 trials confirmados («Se ha compartido correctamente»). La ventana de compartir no tiene opción de
  programar.
- 10/11/2026: `scripts/comprobar.sh` y `scripts/tramos.py` probados en macOS con Python 3.9 y ffmpeg (tramos con
  silencios metidos a propósito: los detecta, deja el margen, avisa de los cortes sobre voz y deja la cola).

## Sin probar todavía

- Una edición completa de punta a punta hecha solo con las herramientas de Edits (cortes, subtítulos, pantalla dividida
  con fotogramas clave). La pantalla dividida depende de que la versión de Edits deje mover el clip; si no, el plan B es
  hacer ese tramo en código e importarlo.
- El botón de Edits que copia una línea de conexión para Claude Code (lo cuenta la guía de otro creador; no lo usamos
  porque deja el token en un archivo de configuración).
- Que lo publicado desde Edits llegue más lejos: no hay dato público de Instagram que lo cuantifique. Estamos midiendo
  4 trials publicados desde Edits contra sus parejas publicadas por API.
