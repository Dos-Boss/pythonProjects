#!/usr/bin/env python3

# Brendan McCann
# 05/08/2021
# Python DES3 Decryptor

import os
# import sys
import argparse
from Crypto.PublicKey import RSA
from Crypto.Cipher import DES3, PKCS1_OAEP
from Crypto import Random


home = os.environ['USERPROFILE']
# home = "C:"


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

usr_keys = get_args()
priv_key = RSA.importKey(open(usr_keys.priv_key, 'rb').read())
cipher_rsa = PKCS1_OAEP.new(priv_key)

sec_key = open(usr_keys.sec_key, 'rb').read()
session_key = cipher_rsa.decrypt(sec_key).decode()
print("Keys Initialised...Get Psyched!\n")

def decryptor(in_file):
    ifile = open(in_file, 'rb')
    iv = ifile.read(8)
    cipher_des3 = DES3.new(session_key, DES3.MODE_CFB, iv)

    data = cipher_des3.decrypt(ifile.read())

    print(data.decode())
    return data.decode()

def write_file(file, data):
    ofile = open(file[:-4], 'x')
    ofile.write(data)
    ofile.close()
    return

os.chdir(home)
for root, dirs, files in os.walk(home):
    for file in files:
        if file.endswith(".cry"):
            fname = os.path.join(os.path.dirname(os.path.abspath(__file__)), file)
            write_file(fname,decryptor(fname))
            print(fname + " - Decrypted Successfully")
