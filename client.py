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

def setup():
    if len(jsonRead['OS']) == 0:
        print(sign + "Please select your OS: Linux | Windows | Mac")
        os = input(sign + ":\t")
        with open("data.json", "w") as f:
            jsonRead["OS"] = os
            json.dump(jsonRead, f, indent=4)
            f.close()

        if os == "Linux" or os == "Windows" or os == "MacOS" or os == "Lin" or os == "Win" or os == "Mac":
            print("Your language setting has been successfully set to: " + os)

        elif os != "Linux" or "Windows" or "MacOS" or "Win" or "Mac" or "Lin":
            print("Please enter a valid option.")
            return setup()
    else:
        pass
def ui():
    if len(jsonRead['OS']) >= 1 and jsonRead['OS'] == "Win":
        print("1) New VPN connection")
        print("2) Go Windows VPN Settings")
        print("3) Show VPN profiles")
        print("4) Settings")
        inpWin = int(input(sign +" | Please select:\t"))

        if inpWin == 1:
            print("Name of connection:")
            name = input(sign + ":  ")
            print("IP/server adress:")
            ip = input(sign + ":  ")
            print("IPSec PSK:")
            ipsecpsk = input(sign + ":\t")

            subprocess.call(["powershell","Add-VpnConnection -Name 132 -ServerAddress 321 -L2tpPsk 321 -TunnelType L2tp -EncryptionLevel Required -AuthenticationMethod Chap,MSChapv2 -Force -RememberCredential -PassThru"],shell=True)
        elif inpWin == 2:
            vpnsettings.vpn_settings()

        elif inpWin == 3:
            subprocess.call(["powershell", "Get-VpnConnection"], shell=True)

        elif inpWin == 4:
            print(sign + "Select your operating system: [Win | Linux | MacOS")
            settingOS = input(sign + "\t")

            if settingOS == "Win" or "Windows":
                print(sign + "Please select your OS: Linux | Windows | Mac")


            elif settingOS == "Linux" or "Lin":
                print(sign + "Please select your OS: Linux | Windows | Mac")


            elif settingOS == "Mac" or "MacOS":
                print(sign + "Please select your OS: Linux | Windows | Mac")


        elif inpWin != 1 or jsonRead['OS'] != "Win" or inpWin != 2 or inpWin != 3 or inpWin != 4:
            print(sign + "Please enter a valid option.")
            return ui()
setup()
ui()
