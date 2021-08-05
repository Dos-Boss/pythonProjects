#!/usr/bin/env python3

# Brendan McCann
# 05/08/2021
# Python Ransomware Decryptor (DES3)

import os
import sys
import argparse
from Crypto.PublicKey import RSA
from Crypto.Cipher import DES3, PKCS1_OAEP
from Crypto import Random


def get_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("-p", "--priv-key", dest="priv_key", help="Private Key")
    parser.add_argument("-s", "--secret-key", dest="sec_key", help="Secret Key")
    usr_keys = parser.parse_args()
    if usr_keys.priv_key:
        print("Privatekey initialised")
    else:
        print("No privatekey loaded!")
        exit()

    if usr_keys.sec_key:
        print("Secret Key Initialised")
    else:
        print("No secretkey loaded!")
        exit()
    return usr_keys


usr_keys = get_args()
priv_key = RSA.import_key(open(usr_keys.priv_key).read())
sec_key = RSA.import_key(open(usr_keys.sec_key).read())

cipher_rsa = PKCS1_OAEP.new(priv_key)
session_key = cipher_rsa.decrypt(sec_key)

file_in = open("ZeroC00l.zzz.cry", "rb")

cipher_des3 = DES3.new(session_key, DES3.MODE_CFB, iv=Random.get_random_bytes(8))
data = cipher_des3.decrypt_and_verify(file_in)
print(data.decode("utf-8"))








