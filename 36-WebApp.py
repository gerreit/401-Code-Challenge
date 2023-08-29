#!/usr/bin/env python3

# Script Name:               Web app fingerprint
# Author:                    Gerald
# Date of latest revision:   8/28/2023
# Purpose:                   web app fingerprint

# Instructions:
# Prompts the user to type a URL or IP address.
#   variable url or ip address is input 
# Prompts the user to type a port number.
#   variable input for port number is input 
# Performs banner grabbing using netcat against the target address at the target port; prints the results to the screen then moves on to the step below.

# Performs banner grabbing using telnet against the target address at the target port; prints the results to the screen then moves on to the step below.
# Performs banner grabbing using Nmap against the target address of all well-known ports; prints the results to the screen.

# Soucres:
# https://pypi.org/project/python-nmap/
# https://www.instructables.com/Netcat-in-Python/
# https://www.geeksforgeeks.org/what-is-banner-grabbing/#
# Chat GPT 

# Imported Libraries:
import socket
import sys 
import os
import telnet
import nmap

# Functions:
def net_cat(addr,port):
    addr = input("input hostname: " )
    port = input("input port: ")
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect((addr, port))


def tel_net(addr,port):
    addr = input(:input hostname: )
    port = input(:input port: )
    tn = telnetlib.Telnet(target_host, target_port, timeout=5)
    tn.read_until(b"\r\n", timeout=5).decode("utf-8")
    print("Banner:")
    print(banner)
    tn.close()
    


def nmap():


# Variables: 




