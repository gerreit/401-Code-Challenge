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

# Imported Libraries:
import sys
from scapy.all import sr1,IP,TCP,ICMP


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



#Main:

print("Make sure you run this script as sudo")

#p=sr1(IP(dst=sys.argv[1])/ICMP())
#if p:
   # p.show()

#print (response)

test_ports
