# -*- coding: utf-8 -*-
import subprocess
import colorama
from colorama import Fore
import json
import logo
import vpnsettings

logo.logo_text()
sign = "siriOS-VPN"

with open("data.json") as jsonFile:
    jsonRead = json.load(jsonFile)
    jsonWrite = json.dump
    jsonFile.close()
    
with open("data.json", "w") as f:
    jsonRead["OS"] = lang
    json.dump(jsonRead, f, indent=4)
    f.close()

def setup():
    if len(jsonRead['OS']) == 0:
        print(sign + "Please select your OS: Linux | Windows | Mac")
        lang = input(sign + ":\t")

        if lang == "Linux" or lang == "Windows" or lang == "MacOS" or lang == "Lin" or lang == "Win" or lang == "Mac":
            print("Your language setting has been successfully set to: " + lang)

        elif lang != "Linux" or "Windows" or "MacOS" or "Win" or "Mac" or "Lin":
            print("Please enter a valid option.")
            return setup()
    else:
        pass
def ui():
    if len(jsonRead['OS']) >= 1 and jsonRead['OS'] == "Win":
        print("1) New VPN connection")
        print("2) Show VPN profiles")
        print("3) Go Windows VPN Settings")
        print("4) Settings")
        inpWin = int(input(sign +" | Please select:\t"))

        if inpWin == 1:
            print("Name of connection:")
            name = input(sign + ":  ")
            print("IP/server adress:")
            ip = input(sign + ":  ")
            print("IPSec PSK:")
            ipsecpsk = input(sign + ":\t")

            subprocess.call(rf'C:\Windows\System32\WindowsPowerShell\v1.0\powershell.exe,Add-VpnConnection -Name {name} -ServerAddress {ip} -L2tpPsk {ipsecpsk} -TunnelType L2tp -EncryptionLevel Required -AuthenticationMethod Chap,MSChapv2 -Force -RememberCredential -PassThru', shell=True)
        elif inpWin == 3:
            vpnsettings.vpn_settings()


        elif inpWin != 1 or jsonRead['OS'] != "Win" or inpWin != 2 or inpWin != 3 or inpWin != 4:
            print(sign + "Please enter a valid option.")
            return ui()
setup()
ui()
