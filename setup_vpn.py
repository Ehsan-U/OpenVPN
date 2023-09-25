
import sh
import os
import time
import sys


def run_terraform():
    os.chdir("./IAC")
    print("Destroying resources")
    sh.terraform("destroy", "-auto-approve",  _out=sys.stdout, _err=sys.stderr)
    print("Creating resouces")
    sh.terraform("apply", "-auto-approve",  _out=sys.stdout, _err=sys.stderr)
    print("Updating inventory")
    sh.python3("update_inventory.py")
    os.chdir("../")
    return True

def run_ansible():
    os.chdir("./Management")
    print("Running playbook")
    sh.ansible_playbook("vpn_playbook.yml",  _out=sys.stdout, _err=sys.stderr)
    os.chdir("../")
    return True

if not os.path.exists("/opt/ovpn_config"):
    os.mkdir("/opt/ovpn_config")
run_terraform()
time.sleep(30)
run_ansible()
# add ovpn to network manager
try:
    sh.nmcli("connection", "delete", "client")
except:
    pass
sh.nmcli("connection", "import", "type", "openvpn", "file", "/opt/ovpn_config/client.ovpn")
print("Setup Completed!")

