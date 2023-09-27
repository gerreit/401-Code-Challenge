from cryptography.fernet import Fernet
import os 
from os.path import exists
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


key_check = exists("./key.key")

if key_check == True:
    key = load_key()
else:
    make_key()
    key = load_key()


# calls the function to load a previously made key, you would need it to decrypt already encrypted files


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

def recursive_encryption():
    # see previous
    f = Fernet(key)
    # saves the file path of the file to decrypt as variable path
    path = input("Path of files to recursvively encrypt: ")
    for root, dirnames, filenames in os.walk(path):
        for filename in filenames:
            # full path to the file, ChatGPT helped with this never woulda considered this
            file_path = os.path.join(root, filename)

            # with the file open read as binary as the variable file
            with open(file_path, "rb") as file:
                file_data = file.read()

            # Encrypts the file data
            encrypted_data = f.encrypt(file_data)

            # Write the encrypted data back to the file
            with open(file_path, "wb") as file:
                file.write(encrypted_data)

def recursive_decryption():
    # see previous
    f = Fernet(key)
    # saves the file path of the file to decrypt as variable path
    path = input("Path of files to recursively decrypt: ")
    for root, dirnames, filenames in os.walk(path):
        for filename in filenames:
            # full path to the file, ChatGPT helped with this never woulda considered this
            file_path = os.path.join(root, filename)

            # with the file open read as binary as the variable file
            with open(file_path, "rb") as file:
                file_data = file.read()

            # Encrypts the file data
            decrypted_data = f.decrypt(file_data)

            # Write the encrypted data back to the file
            with open(file_path, "wb") as file:
                file.write(decrypted_data)


# stuff for making a menu to select which option you wanna use
#make_or_load_key()
option = input("Press 1 to encrypt message\nPress 2 to decrypt message\n Press 3 to encrypt file\n Press 4 to decrypt file\nPress5 to recursively encrypt a directory\n Press 6 to recursively decrypt a directory:  ")
if option == '1':
    encrypt_message()
elif option == "2":
    decrypt_message()
elif option == "3":
    encrypt()
elif option == "4":
    decrypt()
elif option == "5":
    recursive_encryption()
elif option == "6":
    recursive_decryption()
else:
    print("Error happened")