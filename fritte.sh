#!/bin/bash
# Pfad zum lokalen venv-Python
#./.venv/bin/python "$(dirname "$0")/fritten-hosts.py" "$@"

# Absoluten Pfad des Skript-Verzeichnisses ermitteln
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"

# Python aus dem korrekten venv aufrufen und das Python-Skript starten
"$SCRIPT_DIR/.venv/bin/python" "$SCRIPT_DIR/fritten-hosts.py" "$@"
#EOF

