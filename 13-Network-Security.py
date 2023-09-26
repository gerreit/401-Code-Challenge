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

def ping_sweep():
    # stores CIDR block as a variable
    network = input("input CIDR")
    # IPv4 uses that cidr block and is stored into addresses variable
    addresses = IPv4Network(network)
    # starts a counter variable at 0
    live_count = 0
    # for each host in the CIDR block do...
    for host in addresses:
        # if its a network address or broadcast address ignore them
        if (host in (addresses.network_address, addresses.broadcast_address)):
            continue
        # looks out for response packets
        response = sr1(IP(dst=str(host))/ICMP(), timeout=1, verbose=0)
        # if there is no response then print not responsive
        if response is None:
            print(f"{host} is not responsive")
        # if we get a type 3 response and its one of the mentioned code then print is not responsive
        elif (int(response.getlayer(ICMP).type == 3) and int(response.getlayer(ICMP).code) in [1,2,3,9,10,13]):
            print(f"{host} is not responsive")
        # else just say its up and add one to the live count counter
        else:
            print(f"{host} is up ")
            live_count += 1
    # prints the number of live hosts
    print(f"{live_count}/{addresses.num_addresses} hosts are up")

def tcp_scan():
    # stores user input as a host to scan
    host = input("Enter IP address to scan: ")
    # stores the ports to be scanned as a variable
    port_range = [22, 23, 80]
    # for each destination port in the port range...
    for dst_port in port_range:
        # uses the random library to pick a random source port between 1023 and 1037
        src_port = random.randint (1023, 1037)
        # looks for a response from the host
        response = sr1(IP(dst=host)/TCP(sport=src_port,dport=dst_port, flags='S'), timeout=1, verbose=0)
    # if there is no response print below
    if response is None:
        print(f"{host} {dst_port} is filtered and silently dropped.")
    # 0x12 means a response which means if we get a response from the host then prin the port is open. This will then send a request to close the connection
    elif (response.haslayer(TCP)):
        if (response.getlayer(TCP).flags == 0x12):
            (f"Port {port} is open.")
            send_rst =sr1(IP(dst=host)/TCP(sport=src_port,dport=dst_port, flags='R'), timeout=1, verbose=0)
        # 0x14 means no response, if theres no response then below is printed
        elif (response.getlayer(TCP).flags == 0x14):
            print(f"{host}:{dst_port} is closed")
    #if the response is ICMP and gets back a code from the specified codes then print below
    elif (response.haslayer(ICMP)):
        if (int(response.getlayer(ICMP).type == 3) and int(response.getlayer(ICMP).code) in [1,2,3,9,10,13]):
            print(f"{host}:{dst_port} is filtered ")

# makes a function called ping target
def ping_target():
    # stores user inputted target to ping as a variable
    target = input("Input IP address to ping")
    # makes a ICMP packet that is sent to the target
    packet = IP(dst=target) / ICMP()
    # picks a random source port between 1023 and 1037
    src_port = random.randint (1023, 1037)
    # user input variable for which source port you want
    dest_port = input("Input a destination port:  ")
    # makes an empty list called open ports
    open_ports = []

    # looks for a response from the target
    response = sr1(packet, timeout=2, verbose=False)
    # if a response is received then...
    if response:
        # start at port 1
        start_port = 1
        # end at port 100
        end_port = 100
        # looks for a TCP response from the target
        response = sr1(IP(dst=target) / TCP(sport=src_port, dport=dest_port, flags="S"), timeout=1, verbose=False)
        # then for each port from the start port to end port keep going until th end port. each port that is open added to the open port empty list
        for port in range(start_port,end_port + 1):
            open_ports.append(port)
    # prints all ports that were open
    print(open_ports)


# Main
menu = input("Press 1 to ping sweep  Press 2 tcp scan  Press 3 to ping a computer and scan its ports:  ")
if menu == "1":
    ping_sweep()
elif menu == "2": 
    tcp_scan()
elif menu == "3":
    ping_target()
else:
    print("Theres been an error") 
