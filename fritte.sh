#!/bin/bash
# Pfad zum lokalen venv-Python
./.venv/bin/python "$(dirname "$0")/fritten-hosts.py" "$@"
