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


# Variables:

# same as above but for a  destionation port on the hostinstead
destination_port = input("Input a destination port")
# stores the port you want your traffic to come from as a variable
source_port = input("Input a source port")
# range of ports to scan. for this one its just as singe port, dont think this is actually used in the code though
port_range = 22
# which port you want to start the scan at as a variable
start_port = int(input("Input a starting port:"))
# which port you want to end the scan on as a variable
end_port = int(input("Input a end port:"))

# Functions:
def test_ports():
    target_ip = "localhost"  # Replace with the target IP address
    # stores the name of the host to be scanned into a variable
    host_name = "scanme.nmap.org"

    # for each port in the range of the start port and end port do...
    for port in range(start_port, end_port + 1):
        # Create an packet that is sent to the host destination port
        packet = IP(dst=host_name)/TCP(dport=port, flags='S')

        # Send the packet and wait for a response
        response = sr1(packet, timeout=1, verbose=False)

        # if the packet has a tcp packet then 
        if response and response.haslayer(TCP):
            if response[TCP].flags == 18:
                print(f"Port {port} is open.")
                # closes the open connection
                rst_packet = IP(dst=target_ip)/TCP(dport=port, sport=response[TCP].dport, flags='R')
                send(rst_packet, verbose=False)
                # if the port is closed it will return a 4 which means its closed
            elif response[TCP].flags == 4:
                print(f"Port {port} is closed.")
                # if not 4 or 18 then it will print this 
            else:
                print(f"Port {port} is filtered and silently dropped.")
        else:
            print(f"Port {port} is closed.")



#Main:

print("Make sure you run this script as sudo")




test_ports()
