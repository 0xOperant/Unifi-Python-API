from ubiquiti.unifi import API as Unifi_API
import json
import os

# List name, ip, mac, and manufacturer (oui) of all known clients (stations)
with Unifi_API(username=os.environ['UNIFI_USER'], password=os.environ['UNIFI_PASS'], baseurl=os.environ['UNIFI_URL'], verify_ssl=False) as api:
    device_list = api.list_clients()
    for device in device_list:
        try:
            name = device['hostname']
        except KeyError:
            name = device['name']
        try:
            ip = device['ip']
        except KeyError:
            ip = device['fixed_ip']
        oui = device['oui']
        mac = device['mac']
        print(name, "\n   ip  = ",ip,"\n   mac = ",mac,"\n   oui = ",oui)
