# mark joseph
from spytools import*
import re

# could not get the v cipher decrypt method to work

# use regex. I learnt it in natural language processing class
encrypt = re.compile(r"[Ee]ncrypt|[Ee]")
subcipher = re.compile(r"[Ss]|[Ss]ubstitution")
vcipher = re.compile(r"[Vv]|[Vv]igenere")

decrypt = re.compile(r"[Dd]ecrypt|[Dd]")
subcipher = re.compile(r"[Ss]|[Ss]ubstitution")
vcipher = re.compile(r"[Vv]|[Vv]igenere")

quit = re.compile(r"[Qq]|[Qq]uit")

running = True

while running:
    method = input("Do you want to (e)ncrypt, (d)ecrypt or (q)uit: ")
    if encrypt.search(method):
        cipher = input("Which cipher do you want to use?\n(s)ubstitution cipher or the (v)igenère cipher: ")
        if subcipher.search(cipher):
            password = input("please enter the password")
            message = input("please enter the message")
            print("sub cipher used to encrypt")
            print(sub_encrypt(password,message))
        elif vcipher.search(cipher):
            password = input("please enter the password")
            message = input("please enter the message")
            print("vigenere cipher used to encrypt")
            print(vig_encrypt(password,message))
        else:
            print("not an option")
    elif(decrypt.search(method)):
        cipher = input("Which cipher do you want to use?\n(s)ubstitution cipher or the (v)igenère cipher: ")
        if subcipher.search(cipher):
            password = input("please enter the password")
            message = input("please enter the message")
            print("sub cipher used to decrypt")
            print(sub_decrypt(password,message))
        elif vcipher.search(cipher):
            password = input("please enter the password")
            message = input("please enter the message")
            print("vigenere cipher used to decrypt")
            print(vig_decrypt(password,message))
        else:
            print("not an option")
    elif(quit.search(method)):
        running = False
    else:
        print("wrong command")
print('Done')

