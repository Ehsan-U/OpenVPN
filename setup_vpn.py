
import sh
import os
import time
import sys
import argparse



def destroy_iac():
    os.chdir("./IAC")
    print("Destroying resources")
    sh.terraform("destroy", "-auto-approve",  _out=sys.stdout, _err=sys.stderr)


def run_terraform():
    destroy_iac()
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

def remove_connection():
    # remove connection if already exists
    try:
        sh.nmcli("connection", "delete", "client")
    except:
        pass

remove_connection()
if os.path.exists("/tmp/client.ovpn"):
    os.remove("/tmp/client.ovpn")

parser = argparse.ArgumentParser()
parser.add_argument('-a', '--action', dest="action", required=True, help="Action to perform, create/destroy")
action = vars(parser.parse_args()).get("action",'').lower().strip()

if action == 'destroy':
    destroy_iac()
elif action == 'create':
    run_terraform()
    time.sleep(30)
    run_ansible()
    sh.nmcli("connection", "import", "type", "openvpn", "file", "/tmp/client.ovpn")
    print("Setup Completed!")

