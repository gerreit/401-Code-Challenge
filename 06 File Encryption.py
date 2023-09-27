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

# makes key for encryption/decryption
def make_key():
    # saves Fernet.generate_key() as a variable, this is to make this easier to call and for cleaner looking code
    key = Fernet.generate_key()
    # with your key open as a key file write in binary a generated key
    with open("key.key", "wb") as key_file:
        key_file.write(key)

# function to load previously made keys
def load_key():
    return open("key.key", "rb").read()


# calls the function to load a previously made key, you would need it to decrypt already encrypted files
key = load_key()

# makes a function for encrypting messages
def encrypt_message():
    # takes a user inputted message and encodes it and is stored as a variable
    message = input("Please type the message to encode: ").encode()
    # honestly no clue, saves it as a variable though
    f = Fernet(key)
    # encrypts the message variable and saves it as a different variable
    encrypted = f.encrypt(message)
    print("Your encrypted message is:  ")
    print(encrypted)

# function for decrypting messages
def decrypt_message():
    # input a decrypted message here and it gets saved as a variable
    message = input("Message to decrypt: ").encode()
    # see previous
    f = Fernet(key)
    # decrypts the message variable and saves it as different variable
    decrypted_encrypted_message = f.decrypt(message)
    print("Decrypted message:")
    print(decrypted_encrypted_message)

# function for encrypting a file
def encrypt():
    # see previous
    f = Fernet(key)
    # this takes the file path of the file you wanna encrypt and saves it as a variable
    path = input("Input file path of file to encrypt: ")
    # with the filepath open read it as binary as the variable file
    with open(path, "rb") as file:
        # reads the file at the end of the file path and saves it as variable file_data
        file_data = file.read()
    # takes the file_data variable and encrypts it then saves it as encrypted_data variable
    encrypted_data = f.encrypt(file_data)
    # with the file path open write in binary as file
    with open(path, "wb") as file:
        # this does all the encrypting stuff
        file.write(encrypted_data)

# defines a function for decrypting a file
# if your decrypting a file previously encrypted with a different key make sure you load that key or else this wont work properly (if at all)
def decrypt():
    # see previous
    f = Fernet(key)
    # saves the file path of the file to decrypt as variable path
    path = input("Path of file to decrypt: ")
    # with the file path open read as binary as variable file
    with open(path, "rb") as file:
        # reads the file path and saves it as variable file_data
        file_data = file.read()
    # decrypts the file data and saves it as variable decypted
    decrypted = f.decrypt(file_data)
    # with the file path open write in binary the decrypted text into the file
    with open(path, "wb") as file:
        file.write(decrypted)

# stuff for making a menu to select which option you wanna use
option = input("Press 1 to encrypt message\nPress 2 to decrypt message\n Press 3 to encrypt file\n Press 4 to decrypt file: ")
if option == '1':
    encrypt_message()
elif option == "2":
    decrypt_message()
elif option == "3":
    encrypt()
elif option == "4":
    decrypt()
else:
    print("Error happened")
