# Frittenautomat

[DE] Ein robustes CLI-Tool zur Netzwerk-Inventur für FRITZ!Box-Router.
[ENG] A robust CLI tool for network inventory on FRITZ!Box routers.

## Features
- [DE] Auflistung aller aktiven und inaktiven Geräte
- [ENG] List all active and inactive devices
- [DE] Sortierung nach Name oder IP-Adresse
- [ENG] Sort by name or IP address
- [DE] Status-Anzeige (Online/Offline) und MAC-Adressen
- [ENG] Status display (Online/Offline) and MAC addresses

## Installation

### [DE]
1. Repository klonen: `git clone https://github.com/DEIN-USER/frittenautomat.git`
2. Venv erstellen: `python3 -m venv .venv && source .venv/bin/activate`
3. Abhängigkeiten installieren: `pip install -r requirements.txt`
4. Konfiguration: `cp .env.example .env` und Datei anpassen.
5. Ausführen: `python fritten-hosts.py`

### [ENG]
1. Clone the repo: `git clone https://github.com/DEIN-USER/frittenautomat.git`
2. Create venv: `python3 -m venv .venv && source .venv/bin/activate`
3. Install requirements: `pip install -r requirements.txt`
4. Configuration: `cp .env.example .env` and adjust the file.
5. Execution: `python fritten-hosts.py`

## Usage / Benutzung
`python fritten-hosts.py [-n | -i]`

- `-n`: Sortiert/Sort by Hostname
- `-i`: Sortiert/Sort by IP-Address



