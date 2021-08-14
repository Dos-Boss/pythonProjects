#!/usr/bin/env python3

# Brendan McCann
# 05/08/2021
# Python Triple DES Decryptor

import os
import argparse
from platform import system
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


def init():
    global session_key

    usr_keys = get_args()
    private_key = RSA.importKey(open(usr_keys.priv_key, 'rb').read())
    cipher_rsa = PKCS1_OAEP.new(private_key)

    secret_key = open(usr_keys.sec_key, 'rb').read()
    session_key = cipher_rsa.decrypt(secret_key).decode('utf-8')
    print("_______________________________")
    print("Keys Initialised...Get Psyched!")

    if system() == "Windows":
        drive_to_scan_win()
    else:
        drive_to_scan_nix()
    return


def drive_to_scan_win():
    global drive
    drive = []

    drive_list = [chr(x) for x in range(65, 91) if os.path.exists(chr(x) + ":")]

    drive_adj = drive_list.copy()
    for x in range(len(drive_adj)):
        drive_adj[x] += ":/"

    drive_list.append("All")

    uinput = ""
    while uinput not in drive_list:
        print("\n", drive_list)
        uinput = input("Please Enter Drive Letter to Scan: ").capitalize()
    if uinput != "All":
        drive.append(uinput + ":/")
    else:
        drive = drive_adj
    return


def drive_to_scan_nix():
    # TODO: List mount points instead of defaulting to root scan.
    global drive
    drive = []
    drive.append("/")
    return


def decryptor(in_file):
    ifile = open(in_file, 'rb')
    iv = ifile.read(8)
    cipher_des3 = DES3.new(session_key, DES3.MODE_CFB, iv)
    data = cipher_des3.decrypt(ifile.read())
    return data.decode()


def write_file(file, data):
    ofile = open(file[:-4], 'w')
    ofile.write(data)
    ofile.close()
    return


def main():
    init()
    print("\nPlease Wait...")
    for x in range(len(drive)):
        os.chdir(drive[x])
        for root, dirs, files in os.walk(drive[x]):
            for file in files:
                if file.endswith(".cry"):
                    fname = os.path.abspath(os.path.join(root, file))
                    try:
                        write_file(fname, decryptor(fname))
                        print(fname + " - Decrypted Successfully")
                    except UnicodeDecodeError:
                        print(fname + " - Could Not Be Decrypted! - Bad Keys")
    print("\nDecryption Complete\n")

main()
