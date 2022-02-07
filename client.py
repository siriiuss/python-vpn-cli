# -*- coding: utf-8 -*-
import subprocess
import colorama
from colorama import Fore
import json
import logo

logo.logo_text()
sign = "siriOS-VPN"

with open("data.json") as jsonFile:
    jsonRead = json.load(jsonFile)
    jsonWrite = json.dump
    jsonFile.close()

def setup():
    if len(jsonRead['lang']) == 0:
        print(sign + "Please select your language: TR | EN")
        lang = input(sign + ": ")

        if lang == "TR" or lang == "tr":
            print("your language setting has been successfully set to: " + lang)

        elif lang == "EN" or lang == "EN":
            print("Your language setting has been successfully set to: " + lang)

        elif lang != "TR" or "tr" or "EN" or "en":
            print("Please enter a valid option.")
            return setup()
    else:
        pass

    if len(jsonRead['lang']) >= 1 and jsonRead['lang'] == "TR":
        print("New VPN connection")
        print("Show VPN profiles")
        print("Settings")
        transwer = int(input(sign +" | Please select:  "))

        if transwer == 1 and jsonRead['OS'] == "Win":
            print("Name of connection:")
            name = input(sign + ":  ")
            print("IP/server adress:")
            ip = input(sign + ":  ")
            print("IPSec PSK:")
            ipsecpsk = input(sign + ":  ")

            subprocess.call(rf'C:\Windows\System32\WindowsPowerShell\v1.0\powershell.exe,Add-VpnConnection -Name {name} -ServerAddress {ip} -L2tpPsk {ipsecpsk} -TunnelType L2tp -EncryptionLevel Required -AuthenticationMethod Chap,MSChapv2 -Force -RememberCredential -PassThru', shell=True)
setup()