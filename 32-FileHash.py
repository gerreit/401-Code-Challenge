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

# Sources:
# ChatGPT
#Marco code

# Imported Libraries:
import os
import platform
from time import sleep
import hashlib 
import datetime 

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
    # makes a counting variable to keep track of the number of files searched 
    Files_Searched = 0
    # uses os.system to run windows specific commands to look for specified files . This looks like a bunch of gibberish to me honestly
    searchcount = os.system("dir /a:-d /s /b " + str(Directory) + "\\" + str(whichFile) + " | find /c \":\\\"").read()
    print("Found files: " + Files_Searched)

# function to easily call for timestamps
def time_stamp():
    now = datetime.datetime.now()
    return now.strftime('%m-%d-%Y %H:%M:%S')

# function to get the hashes of files
def file_hash(filename):
    h = hashlib.md5()
    # with the file open read binary as file
    with open (filename, 'rb') as file:
        chunk = 0
        # while the file is not empty read it and read it and make a hash of the files
        while chunk != b'':
            chunk = file.read(1024)
            h.update(chunk)

def hash():
    # sets dir and file count variables to 1
    dir_count = 1
    file_count = 1
    # variable that takes user input for a directory file path
    path = input("Input path to directory:  ")
    # for each file path, directory, and file at the user inputted file path do...
    for (path,dirs,files) in os.walk(path):
        # add 1 to directory count
        dir_count += 1
        # for each file 
        for file in files:
            # add 1 to the file count
            file_count += 1
            # join the path of the file right before the name of the file for a full filepth
            filename = os.path.join(path,file)
            # saves the file hash as a variable
            md5 = file_hash(filename)
            # prints the filename, hash, and time stamp
            print(filename)
            print(md5)
            print(time_stamp)
    # prints the directory and file count after its done
    print(dir_count)
    print(file_count)

# function to check which OS is being run        
def OS_result():
    # uses system platform to check which os is being run
    check_OS = platform.system()
    # if the result of the playform.system check is linux run the linux search, if its windows run the windows search
    if check_OS == "Linux":
        Linux_FileSearch()
    elif check_OS == "Windows":
        Windows_FileSearch()
    else:
        print("Operating System could not be determined")
# Variables:
check_OS = platform.system()

# Main: 

# menu to let users pick which option to do
menu = input("Press 1 to search for a file\nPress2 to get a file hash:  ")
if menu == "1":
    OS_result()
elif menu == '2':
    hash()
else:
    print("Error has occured")
