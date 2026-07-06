#!/usr/bin/env python3
import os
import argparse
import ipaddress
from dotenv import load_dotenv
from fritzconnection import FritzConnection
from fritzconnection.core.exceptions import FritzArrayIndexError

load_dotenv()

def get_devices():
    fc = FritzConnection(
        address=os.getenv('FRITZ_IP'),
        user=os.getenv('FRITZ_USER'),
        password=os.getenv('FRITZ_PW')
    )
    
    devices = []
    try:
        num_hosts = fc.call_action('Hosts:1', 'GetHostNumberOfEntries')['NewHostNumberOfEntries']
        for i in range(num_hosts):
            try:
                host = fc.call_action('Hosts:1', 'GetGenericHostEntry', NewIndex=i)
                ip = host.get('NewIPAddress') or ""
                netzwerk = 'Gastnetz' if ip.startswith('192.168.179') else 'Heimnetz'
                
                devices.append({
                    'name': host.get('NewHostName') or "Unbekannt",
                    'ip': ip,
                    'mac': host.get('NewMACAddress'),
                    'type': netzwerk,
                    'status': 'Online' if host.get('NewActive') == 1 else 'Offline'
                })
            except FritzArrayIndexError:
                continue
    except Exception:
        pass
    return devices

def main():
    parser = argparse.ArgumentParser(
        description="FRITZ!Box Netzwerk-Inventur v1.0.1",
        add_help=True
    )
    
    # explizite Definition für -help (mit einem Bindestrich) zur Vermeidung von Fehlern
    parser.add_argument("-help", action="help", help="Zeige diese Hilfe an")
    
    group = parser.add_mutually_exclusive_group()
    group.add_argument("-n", "--name", action="store_true", help="Sortiert nach Hostname")
    group.add_argument("-i", "--ip", action="store_true", help="Sortiert nach IP-Adresse")
    
    args = parser.parse_args()
    devices = get_devices()

    print(f"{'Name':<20} | {'MAC-Adresse':<17} | {'IP-Adresse':<15} | {'Netzwerk':<10} | {'Status'}")
    print("-" * 90)

    if args.ip:
        has_ip = [d for d in devices if d['ip']]
        no_ip = [d for d in devices if not d['ip']]
        sorted_ip = sorted(has_ip, key=lambda x: ipaddress.ip_address(x['ip']))
        for d in sorted_ip + no_ip:
            print(f"{d['name']:<20} | {d['mac']:<17} | {d['ip'] or '---':<15} | {d['type']:<10} | {d['status']}")
    else:
        for d in sorted(devices, key=lambda x: x['name'].lower()):
            print(f"{d['name']:<20} | {d['mac']:<17} | {d['ip'] or '---':<15} | {d['type']:<10} | {d['status']}")

if __name__ == "__main__":
    main()



##  Mit Hilfe von KI erstellt:
#EOF
