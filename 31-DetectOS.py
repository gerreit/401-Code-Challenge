#!/usr/bin/env python3

# Script Name:               Detect operating system
# Author:                    Gerald
# Date of latest revision:   8/14/2023
# Purpose:                   runs a command depending on your operating system
# Instructions:

# Prompt the user to type in a file name to search for.
# input variable for file name
# Prompt the user for a directory to search in.
#  input a variable for file path
# Search each file in the directory by name.
#  need to look this up, it reminds me of the file.readline from a few weeks ago
# For each positive detection, print to the screen the file name and location.

# At the end of the search process, print to the screen how many files were searched and how many hits were found.

# Imported Libraries:
import os
import platform
from time import sleep

# Functions:
def Linux_FileSearch():
    # store the file name and path
    File_Name = input("Input a file name to search for: ")
    # store the file path
    File_Path = input("Input a file path: ")
    # store the number of files searched
    Files_Searched = 0
    # store the number of hits
    Confirmed = 0
    # will walk through the directory and search for the file
    for root, dirnames, filenames in os.walk(File_Path):
        # for each file in the directory,
        for filename in filenames:  
            # for each file in the directory, add the file name to the list of files searched
            Files_Searched += 1
            # if the file name is the same as the inputted file name
            if filename == File_Name: 
                # add one file confirmed 
                Confirmed += 1
                # print to the screen the file name and location
                print(f"Found {File_Name} in {File_Path}")

    return Files_Searched, Confirmed

# portion from marcos code
def Windows_FileSearch():
    File_Name = input("Input a file name to search for: ")
    Directory = input("Input a directory: ")
    Files_Searched = 0
    # uses os.system to run windows specific commands to look for specified files . This looks like a bunch of gibberish to me honestly
    searchcount = os.system("dir /a:-d /s /b " + str(Directory) + "\\" + str(whichFile) + " | find /c \":\\\"").read()
    print("Found files: " + Files_Searched)

# Variables:
check_OS = platform.system()

# Main: 
if check_OS == "Linux":
    Linux_FileSearch()
elif check_OS == "Windows":
    Windows_FileSearch()
else:
    print("Operating System could not be determined")
