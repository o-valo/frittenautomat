# Frittenautomat v1.0.0

[DE] Ein robustes CLI-Tool zur Netzwerk-Inventur für FRITZ!Box-Router.  
[ENG] A robust CLI tool for network inventory on FRITZ!Box routers.

## Features
- [DE] Auflistung aller aktiven und inaktiven Geräte
- [ENG] List all active and inactive devices
- [DE] Sortierung nach Name oder IP-Adresse
- [ENG] Sort by name or IP address
- [DE] Status-Anzeige (Online/Offline) und MAC-Adressen
- [ENG] Status display (Online/Offline) and MAC addresses
- [DE] Gastnetz-Erkennung
- [ENG] Guest network detection

## Installation

### [DE]
1. Repository klonen: `git clone https://github.com/DEIN-USER/frittenautomat.git`
2. In Ordner wechseln: `cd frittenautomat`
3. Installationsskript ausführen: `./install.sh`
4. Konfiguration: `cp .env.example .env` und `.env` Datei mit Zugangsdaten anpassen.
5. Ausführen: `./fritten-hosts.py`

### [ENG]
1. Clone the repo: `git clone https://github.com/DEIN-USER/frittenautomat.git`
2. Change directory: `cd frittenautomat`
3. Run install script: `./install.sh`
4. Configuration: `cp .env.example .env` and adjust the credentials.
5. Execution: `./fritten-hosts.py`

## Usage / Benutzung
`python fritten-hosts.py [-n | -i]`

- `-n`: Sortiert/Sort by Hostname
- `-i`: Sortiert/Sort by IP-Address

## Troubleshooting
[DE] **Keine Verbindung zur FRITZ!Box?**
1. Stelle sicher, dass "Zugriff für Anwendungen zulassen" in der FRITZ!Box-Oberfläche unter *Heimnetz -> Netzwerk -> Netzwerkeinstellungen* aktiviert ist.
2. Prüfe, ob die IP der FRITZ!Box in der `.env` korrekt hinterlegt ist.
3. Stelle sicher, dass dein User-Account in der Box berechtigt ist, TR-064 Anfragen zu stellen.

[ENG] **No connection to the FRITZ!Box?**
1. Ensure "Access for applications" is enabled in the FRITZ!Box UI under *Home Network -> Network -> Network Settings*.
2. Verify the FRITZ!Box IP address in the `.env` file.
3. Ensure your user account has permissions to perform TR-064 requests.

## Version
v1.0.0 - Stable Release

## Mit Hilfe von KI erstellt:
#EOF
