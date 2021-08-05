#!/usr/bin/env python3

# Brendan McCann
# 05/08/2021
# Python DES3 Decryptor

# import os
# import sys
import argparse
from Crypto.PublicKey import RSA
from Crypto.Cipher import DES3, PKCS1_OAEP



def get_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("-p", "--privatekey", dest="priv_key", help="Private Key")
    parser.add_argument("-s", "--secretkey", dest="sec_key", help="Secret Key")
    usr_keys = parser.parse_args()
    if not usr_keys.priv_key:
        print("No privatekey specified!")
        exit()
    elif not usr_keys.sec_key:
        print("No secretkey specified!")
        exit()
    return usr_keys


file_in = open("ZeroC00l.zzz.cry", "rb")

usr_keys = get_args()
priv_key = RSA.importKey(open(usr_keys.priv_key, 'rb').read())
print("\nPrivatekey Initialised!")

cipher_rsa = PKCS1_OAEP.new(priv_key)
sec_key = open(usr_keys.sec_key, 'rb').read()
print("Secretkey Initialised!\n")

session_key = cipher_rsa.decrypt(sec_key).decode()
iv = file_in.read(8)
cipher_des3 = DES3.new(session_key, DES3.MODE_CFB, iv)
data = cipher_des3.decrypt(file_in.read())
print(data.decode("utf-8"))
