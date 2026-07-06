#!/bin/bash
# install.sh - Automatisierte Installation

echo "Installiere Frittenautomat..."

# 1. venv erstellen
python3 -m venv .venv

# 2. Umgebung aktivieren
source .venv/bin/activate

# 3. Pip upgraden & Pakete installieren
pip install --upgrade pip
pip install -r requirements.txt

# 4. .env erstellen falls nicht vorhanden
if [ ! -f .env ]; then
    cp .env.example .env
    echo "Bitte .env Datei anpassen!"
fi

echo "Installation abgeschlossen. Starte mit: ./fritten-hosts.py"

#EOF
##  Mit Hilfe von KI erstellt:
