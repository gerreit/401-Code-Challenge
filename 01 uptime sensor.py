#!/usr/bin/env python3

# Script Name:               Uptime sensor
# Author:                    Gerald
# Date of latest revision:   7/11/2023
# Purpose:                   use ping command to check if system is up and running
# Instructions:   

# put this in a function so like def uptime sensor
#Transmit a single ICMP (ping) packet to a specific IP every two seconds.
# import the time library and use time.sleep(2) so it only sends a ping every two second
# put in a while loop so like while Infinite variable is true ping
#Evaluate the response as either success or failure.
# if statement that if the error code is equal to 0 (success) 
#Assign success or failure to a status variable.
#For every ICMP transmission attempted, print the status variable along with a comprehensive timestamp and destination IP tested.
# i imagine date time library would be nice for htis

# Sources: https://stackoverflow.com/questions/2953462/pinging-servers-in-python

# Imported libraries:
import os
import time
import datetime

# Variables:
Infinite = 1
destination = input("Enter a DNS server to ping: ")

# Functions:
def uptime_sensor():
    while Infinite == 1:
        response = os.system("ping -c 1 " + destination)
        response
        time.sleep(2)
        if response == 0:
            return response
        else:
            return response
        print(response + datetime.datetime.now + destination)

uptime_sensor()
# i cant figure out why this loop and keep pinging