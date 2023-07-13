#!/usr/bin/env python3

# Script Name:               Uptime sensor part 2
# Author:                    Gerald
# Date of latest revision:   7/11/2023
# Purpose:                   get rid of hard coding and email when server goes up
# Instructions:   
#Ask the user for an email address and password to use for sending notifications.
# import getpass and use input("message") to store as an email variable
#Send an email to the administrator if a host status changes (from “up” to “down” or “down” to “up”).
# import smtplib 
#Clearly indicate in the message which host status changed, the status before and after, and a timestamp of the event.
# idk


# Sources: https://stackoverflow.com/questions/2953462/pinging-servers-in-python

# Imported libraries:
import os
import time
import datetime
from getpass import getpass
import smtplib

# Variables:
Infinite = 1
destination = input("Enter a DNS server to ping: ")
#email = input("Enter in your email: ")
#password = getpass("Enter in your password, nothing visual will happen when inputting for security: ")

# Functions:
def uptime_sensor():
    while Infinite == 1:
        response = os.system("ping -c 1 " + destination)
        time.sleep(2)
        if response == 0:
            DNS = "Host is up"
        else:
            DNS = "Host is down"
        return DNS
        print(response + datetime.datetime.now + destination)

uptime_sensor()


# i cant figure out why this loop and keep pinging