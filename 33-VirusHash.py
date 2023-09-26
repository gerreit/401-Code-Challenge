#!/usr/bin/env python3

# Script Name:               Virus Total hash check
# Author:                    Gerald
# Date of latest revision:   8/14/2023
# Purpose:                   checks a user inputted hash in virus total to see if its malicious


import os
import getpass
import platform 
import subprocess

os.system(query)

def Linux_Hash():

    inputkey = getpass.getpass('Input your api key:  ')
    #apikey = os.getenv(inputkey) # Set your environment variable before proceeding. You'll need a free API key from virustotal.com so get signed up there first.
    #hash = 'D41D8CD98F00B204E9800998ECF8427E' # Set your hash here. 
    hash = input("Input the file hash to check:  ")

    # This concatenates everything into a working shell statement that gets passed into virustotal-search.py
    query = 'python3 virustotal-search.py -k ' + inputkey + ' -m ' + hash

def Windows_Hash():
    import os
    import getpass

    inputkey = getpass.getpass('Input your api key:  ')
    #apikey = os.getenv(inputkey) # Set your environment variable before proceeding. You'll need a free API key from virustotal.com so get signed up there first.
    #hash = 'D41D8CD98F00B204E9800998ECF8427E' # Set your hash here. 
    hash = input("Input the file hash to check:  ")
    command = f'python virustotal-search.py -k {inputkey} -m {hash}'
    result = subprocess.run(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)




def OS_result():
    check_OS = platform.system()
    if check_OS == "Linux":
        Linux_Hash()
    elif check_OS == "Windows":
       Windows_Hash()
    else:
        print("Operating System could not be determined")
# Variables:

OS_result()