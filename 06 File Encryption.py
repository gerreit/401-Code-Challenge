#!/usr/bin/env python3

# Script Name:               File Encryption
# Author:                    Gerald
# Date of latest revision:   7/17/2023
# Purpose:                   
# Instructions:   
#Prompt the user to select a mode:
# could do user = input("Please select an option:" ) and put it all in an if statement
#Encrypt a file (mode 1)
# figure out
#Decrypt a file (mode 2)
# figure out
#Encrypt a message (mode 3)
# figure out
#Decrypt a message (mode 4)
# figure out
#If mode 1 or 2 are selected, prompt the user to provide a filepath to a target file.
# path = input("Input file path:")
#If mode 3 or 4 are selected, prompt the user to provide a cleartext string.
# cleartext_string = input (Input a cleartext string:)
#Encrypt the target file if in mode 1.
#Delete the existing target file and replace it entirely with the encrypted version.
#Decrypt the target file if in mode 2.
#Delete the encrypted target file and replace it entirely with the decrypted version.
#Encrypt the string if in mode 3.
#Print the ciphertext to the screen.
#Decrypt the string if in mode 4.
#Print the cleartext to the screen
#   nest the functions in an if statement

# Source:
# https://www.thepythoncode.com/article/encrypt-decrypt-files-symmetric-python

# Imported Libraries:
from cryptography.fernet import Fernet

# Functions:
def make_key():
    # stores generated key as a variable
    key = Fernet.generate_key()
    # Open the file named "key.key" in binary mode ("wb") to write the key
    with open("key.key", "wb") as key_file:
        # Write the key to the file in binary format
        key_file.write(key)

def load_key():
    # opens and reads in binary format then returns the contents of the file
    return open("key.key", "rb").read()

# defines a function to encrypt messages
def encrypt_message():
    # takes the message user inputted variable and encrypts it
    message.encrypt()
    # initialize the Fernet class (taken from site dont quite understand it)
    f = Fernet(key)
    # stores the encrypted message as a variable 
    encrypted = f.encrypt(message)

def decrypt_message():
    # initialize the Fernet class (taken from site dont quite understand it)
    f = Fernet(key)
    # save decrypting message as a variable
    decrypted_encrypted_message = f.decrypt(message)

def encrypt(filename, key):
    f = fernet(key)
    with open(filename, "rb") as file:
        
        file_data = file.read()
        encrypted_data = f.encrypt(file_data)


# Variables:

# stores load key function as a variable
key = load_key

# 
menu = input("Press 1 for thing\nPress 2 for thing\n Press 3 for thing\n Press 4 for thing")

# the message stored as a variable
message = input("Please type the message to encode: ")

# Main:

if menu == 1():
    pass
elif
    pass
elif       
    pass
elif    
    pass
else
    print("Not a valid input")

# calls the make_key function defined earlier
make_key

