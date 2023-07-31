#!/usr/bin/env python3

# Script Name:               Brute Force tool
# Author:                    Gerald
# Date of latest revision:   7/24/2023
# Purpose:                   looks through files for users and passwords to use to brute force
# Instructions:

#Mode 1: Offensive; Dictionary Iterator
#Accepts a user input word list file path and iterates through the word list, assigning the word being read to a variable.
# need a while loopt to iterate through each line
# open file in r 
# file_path = input
# list or word or whatever the variable name is gonna be
# import time module for slep
#Add a delay between words.
#Print to the screen the value of the variable

#Mode 2: Defensive; Password Recognized
#Accepts a user input string.
#Accepts a user input word list file path.
#Search the word list for the user input string.
#Print to the screen whether the string appeared in the word list.
# i guess if password == file.readline print("your password is here")

# Imported Libraries:
import time 

# c:\Users\greit\Downloads\rockyou.txt.tar.gz

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
    File_Path = input("Input a file path for dictionary attack")
    # opens the file from the file path in read mode and stores as a variable
    file = open(File_Path, "r")
    # looks at the file (the file path) variable and reads lines from it
    line = file.readline()
    # while there is lines to read in the line variable (stops if there are no more lines)
    while line:
        # gets rid of any trailing characters like accidental spaces and saves as a variable
        line = line.rstrip()
        # saves line as the word variable. This seems unneccessary wouldnt print(line) work here just fine?
        word = line
        print(word)
        # uses time library to sleep for one second
        time.sleep(1)
        # changes the line variable to read lines from the file. This will move on to the next line
        line = file.readline
    # when there are no more lines to read closes the file
    file.close()

def Check_Password():
    File_Path = input("Input a file path to check for passwrod ")
    Password_to_check = input("Input a password to check")
    file = open(File_Path, "r")
    line = file.readline()
    while line:
        line = line.rstrip()
        word = line

        if word == Password_to_check: 
            print("Change your password")
        else:
            print("Your password is fine")

        line = file.readline()
    file.close()
# Main
menu = input("Press 1 to use a dictionary attack  Press 2 to check your password: ")
if menu == "1":
    Brute_Force
elif menu == 2: 
    Check_Password  
#else:
    print("Theres been an error") 


