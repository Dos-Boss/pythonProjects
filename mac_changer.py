#!/usr/bin/env python3

# - Brendan McCann
# - 21/03/2021
# - MAC address changer

import subprocess
import optparse
import re


def get_args():
    parser = optparse.OptionParser()
    parser.add_option("-i", "--interface", dest="interface", help="Interface to change MAC address")
    parser.add_option("-m", "--mac", dest="new_mac", help=("New MAC address"))
    (options, _arguments) = parser.parse_args()

    if not options.interface:
        parser.error('Invalid interface, use --help for more info.')
    elif not options.new_mac:
        parser.error('Invalid MAC, use --help for more info.')
    return options


def changeMac(interface, new_mac):
    print('[+] Changing MAC address for ' + interface + ' to ' + new_mac)
    subprocess.call(['ifconfig', interface, 'down'])
    subprocess.call(['ifconfig', interface, 'hw', 'ether', new_mac])
    subprocess.call(['ifconfig', interface, 'up'])


def getCurrentMac(interface):
    ifconfig_result = subprocess.check_output(['ifconfig', interface])

    mac_search_result = re.search(r'\w\w:\w\w:\w\w:\w\w:\w\w:\w\w', str(ifconfig_result))

    if mac_search_result:
        return mac_search_result.group(0)
    else:
        print("[-] Could not read MAC address")


options = get_args()
currentMac = getCurrentMac(options.interface)
print('Current MAC = ' + str(currentMac))

changeMac(options.interface, options.new_mac)

currentMac = getCurrentMac(options.interface)

if currentMac == options.new_mac:
    print('[+] MAC address successfully changed to ' + currentMac)
else:
    print('[-] MAC address was not changed.')
