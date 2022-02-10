import subprocess

def vpn_settings():
    subprocess.call("start ms-settings:network-vpn", shell=True)
