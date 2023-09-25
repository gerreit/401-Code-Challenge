#!/usr/bin/env python3

# Script Name:               Network Security Tool
# Author:                    Gerald
# Date of latest revision:   7/24/2023
# Purpose:                   script alternative to NMAP
# Instructions:   
#Define host IP
# host_ip = ip
#Define port range or specific set of ports to scan
# ports_to_scan = input("Input ports to scan: ")
#Test each port in the specified range using a for loop
#If flag 0x12 received, send a RST packet to graciously close the open connection. Notify the user the port is open.
#If flag 0x14 received, notify user the port is closed.
#If no flag is received, notify the user the port is filtered and silently dropped.

# I think it would be cool to make a function that asks if you ran the script in sudo and closes it if you didnt

# Sources:
# https://scapy.readthedocs.io/en/latest/extending.html
# ChatGPT helped with the for loop part
# marco code

# Imported Libraries:
import sys
from scapy.all import sr1,IP,TCP,ICMP
from ipaddress import IPv4Network
import random

# Variables:
host_name = "scanme.nmap.org"
destination_port = input("Input a destination port")
source_port = input("Input a source port")
port_range = 22
start_port = input("Input a starting port:")
end_port = input("Input a end port:")

# Functions:
def test_ports(start_port, end_port):
    target_ip = "localhost"  # Replace with the target IP address

    for port in range(start_port, end_port + 1):
        # Create an IP and TCP layer packet with destination port as 'port'
        packet = IP(dst=target_ip)/TCP(dport=port, flags='S')

        # Send the packet and wait for a response
        response = sr1(packet, timeout=1, verbose=False)

        if response and response.haslayer(TCP):
            if response[TCP].flags == "SA":
                print(f"Port {port} is open.")
                # Send a RST packet to graciously close the open connection
                rst_packet = IP(dst=target_ip)/TCP(dport=port, sport=response[TCP].dport, flags='R')
                send(rst_packet, verbose=False)
            elif response[TCP].flags == "RA":
                print(f"Port {port} is closed.")
            else:
                print(f"Port {port} is filtered and silently dropped.")
        else:
            print(f"Port {port} is closed.")

def ping_sweep():
    network = input("input CIDR")
    addresses = IPv4Network(network)
    live_count = 0
    for host in addresses:
        if (host in (addresses.network_address, addresses.broadcast_address)):
            continue

        response = sr1(IP(dst=str(host))/ICMP(), timeout=1, verbose=0)
        if response is None:
            print(f"{host} is not responsive")
        elif (int(response.getlayer(ICMP).type == 3) and int(response.getlayer(ICMP).code) in [1,2,3,9,10,13]):
            print(f"{host} is not responsive")
        else:
            print(f"{host} is up ")
            live_count += 1

    print(f"{live_count}/{addresses.num_addresses} hosts are up")

def tcp_scan():
    host = input("Enter IP address to scan: ")

    port_range = [22, 23, 80]

    for dst_port in port_range:
        src_port = random.randint (1023, 1037)
        response = sr1(IP(dst=host)/TCP(sport=src_port,dport=dst_port, flags='S'), timeout=1, verbose=0)

    if response is None:
        print(f"{host} {dst_port} is filtered and silently dropped.")

    elif (response.haslayer(TCP)):
        if (response.getlayer(TCP).flags == 0x12):
            (f"Port {port} is open.")
            send_rst =sr1(IP(dst=host)/TCP(sport=src_port,dport=dst_port, flags='R'), timeout=1, verbose=0)

        elif (response.getlayer(TCP).flags == 0x14):
            print(f"{host}:{dst_port} is closed")

    elif (response.haslayer(ICMP)):
        if (int(response.getlayer(ICMP).type == 3) and int(response.getlayer(ICMP).code) in [1,2,3,9,10,13]):
            print(f"{host}:{dst_port} is filtered ")
print("Make sure you run this script as sudo")

#p=sr1(IP(dst=sys.argv[1])/ICMP())
#if p:
   # p.show()

#print (response)

# Main
menu = input("Press 1 to ping sweep  Press 2 tcp scan: ")
if menu == "1":
    ping_sweep()
elif menu == 2: 
    tcp_scan()
#else:
    print("Theres been an error") 