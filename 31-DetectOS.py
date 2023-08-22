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
    File_Name = input("Input a file name to search for: ")
    File_Path = input("Input a file path: ")
    Files_Searched = 0
    Confirmed = 0
    for root, dir, files in os.walk(directory):
        Files_Searched += 1
        if file == File_Name:
            Confirmed += 1
            print(f"Found {file} in {File_Path}")

    return Files_Searched, hits
def_Windows_FileSearch():
    File_Name = input("Input a file name to search for: ")
    File_Path = input("Input a file path: ")


# Variables:
check_OS = platform.system()

# Main: 
if check_OS == "Linux":
    Linux_FileSearch()
elif check_OS == "Windows":
    Windows_FileSearch()
else:
    print("Operating System could not be determined")
