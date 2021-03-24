#!/usr/bin/env python3

# - Brendan McCann
# - 24/03/2021
# - Simple Network Scanner, displaying connected IPs, MACs, and Hostnames

import scapy.all as scapy
import optparse
import socket


def getArgs():
    parser = optparse.OptionParser()
    parser.add_option("-t", "--target", dest="target", help="Target IP / IP range.")
    (options, args) = parser.parse_args()
    return options


def scan(ip_address):
    arp_request = scapy.ARP(pdst=ip_address)
    broadcast = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
    packet = broadcast / arp_request
    lstAns, lstUnans = scapy.srp(packet, timeout=1, verbose=False)

    lstClients = []
    for result in lstAns:
        dictClient = {"ip": result[1].psrc, "mac": result[1].hwsrc}
        lstClients.append(dictClient)

    return lstClients


def printResults(lstResults):
    print("-----------------------------------------------------")
    print("IP\t\tMAC Address\t\tHostname")
    print("-----------------------------------------------------")

    for client in lstResults:
        print(client["ip"] + "\t" + client["mac"] + "\t" + socket.gethostbyaddr(client["ip"])[0])


options = getArgs()

if options.target:
    scanResult = scan(options.target)
    printResults(scanResult)
else:
    print("No target specified\nRun with -h for help")
