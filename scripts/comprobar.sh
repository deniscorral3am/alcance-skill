#!/usr/bin/env bash
# Comprueba lo que necesita /alcance: Mac con chip de Apple, Edits para Mac abierto con el Automation Server,
# Claude Code, el puente insta-edits, ffmpeg y la carpeta de Películas. Solo lee: no instala ni cambia nada.
ok(){ printf '  ✓ %s\n' "$1"; }; ko(){ printf '  ✗ %s\n' "$1"; }; av(){ printf '  · %s\n' "$1"; }
echo "Comprobando el Mac…"

if [ "$(uname -s)" = "Darwin" ] && [ "$(uname -m)" = "arm64" ]; then
  ok "Mac con chip de Apple (macOS $(sw_vers -productVersion))"
else
  ko "Edits para Mac solo funciona en un Mac con chip de Apple (M1 o posterior)"
fi

if [ -d "/Applications/Edits.app" ]; then ok "Edits está en Aplicaciones"
else ko "No encuentro Edits en Aplicaciones: descárgalo gratis en edits.instagram.com/desktop"; fi

if pgrep -xq "Edits" || pgrep -qf "/Applications/Edits.app/"; then ok "Edits está abierto"
else ko "Edits está cerrado: ábrelo y déjalo abierto mientras Claude trabaja"; fi

CODE=$(curl -s -o /dev/null -w "%{http_code}" --max-time 3 "http://127.0.0.1:19501/mcp" 2>/dev/null)
if [ -n "$CODE" ] && [ "$CODE" != "000" ]; then
  ok "El Automation Server de Edits responde (puerto 19501)"
else
  ko "El Automation Server no responde: Edits › Configuración › Automation › Enable Automation Server"
fi

if command -v claude >/dev/null 2>&1; then ok "Claude Code $(claude --version 2>/dev/null | head -1)"
else av "No veo el comando claude (si usas la pestaña Code de la app de Claude, es normal)"; fi

if [ -d "$HOME/.claude/plugins/cache/insta-edits" ]; then ok "Puente insta-edits instalado como plugin"
elif command -v insta-edits >/dev/null 2>&1; then ok "Puente insta-edits instalado (línea de comandos)"
else ko "Falta el puente: /plugin marketplace add faisalkhanzemi/insta-edits-for-claude y /plugin install insta-edits@insta-edits"; fi

# Con el plugin, el token está en el llavero y el doctor de la línea de comandos no lo ve: solo lo pasamos sin plugin.
if [ ! -d "$HOME/.claude/plugins/cache/insta-edits" ] && command -v insta-edits >/dev/null 2>&1; then
  echo "Diagnóstico del puente:"; insta-edits doctor 2>/dev/null | sed 's/^/    /' || true
fi

if command -v ffmpeg >/dev/null 2>&1; then ok "ffmpeg (para medir los cortes)"
else ko "Falta ffmpeg: brew install ffmpeg"; fi
if command -v python3 >/dev/null 2>&1; then ok "$(python3 --version)"; else ko "Falta Python 3: xcode-select --install"; fi

if [ -d "$HOME/Movies" ]; then
  ok "Carpeta Películas: $HOME/Movies (Edits solo abre vídeos de aquí)"
  [ -d "$HOME/Movies/Reels con Edits" ] && ok "Carpeta de trabajo: $HOME/Movies/Reels con Edits" \
    || av "Aún no existe ~/Movies/Reels con Edits (se crea al empezar)"
else
  ko "No existe ~/Movies"
fi
echo "Al terminar, en Claude Code escribe /mcp: tiene que salir «edits» conectado."
