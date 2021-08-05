#!/usr/bin/env python3

# WIP
# Brendan McCann
# 05/08/2021
# Python Ransomware Decryptor (DES3)

import os
import sys
import argparse
from Crypto.PublicKey import RSA
from Crypto.Cipher import DES3, PKCS1_OAEP


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
priv_key = usr_keys.priv_key
sec_key = usr_keys.sec_key

cipher_rsa = PKCS1_OAEP.new(priv_key)
session_key = cipher_rsa.decrypt(sec_key)


def decrypt_file():
    return







