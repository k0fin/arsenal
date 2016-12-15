#!/usr/bin/python2

import sys
import os
import glob
import random
import re
import requests
import subprocess
import blessings

from argparse import ArgumentParser

###############################################################
#     ___                               __
#    /   |  _____________  ____  ____ _/ /
#   / /| | / ___/ ___/ _ \/ __ \/ __ '/ /
#  / ___ |/ /  (__  )  __/ / / / /_/ / /
# /_/  |_/_/  /____/\___/_/ /_/\__,_/_/
#
# Arsenal | A script to download and install additional tools
#         | to Kali Linux 2.
###############################################################

border = blessings.Terminal().width

def main():

    parser = ArgumentParser()

    parser.add_argument('-c', '--config', help='alternate path to arsenal configuration file path')
    args = parser.parse_args()
    arsenal_config = args.config

    if arsenal_config and len(glob.glob('{}/*'.format(arsenal_config))) != 0:
        loaded_config = load_config_file(arsenal_config)
        install_file = loaded_config['INSTALL_FILE']
        loaded_install = load_install_file(install_file)

def arsenal_menu():

    menu = '''
[ 1 ] - Launch Updates
[ 2 ] - Install Tools
[ 3 ] - Install Extras
[ 4 ] - Exit Arsenal

    '''

    select = int(raw_input('[<>] Select an option: '))
    if select < 1 or select > 4:
        print '[--] Invalid selection.'
        banner()
        arsenal_menu()

    if select == 1:
        print "UPDATING KALI"

    elif select == 2:
        print "INSTALLING TOOLS"

    elif select == 3:
        print "INSTALLING EXTRAS"


    elif select == 4:
        print "EXITING"
        sys.exit()

def load_config_file(fname):

    configs = []
    config_keys = {}
    with open(fname, 'r') as configfile:
        configbuf = configfile.read().strip().split('\n')
        for obj in configbuf:
            if obj.strip().startswith('#'):
                continue
            configs.append(obj.strip())

    for cvar in configs:
        config_keys.update({cvar.split('=')[0]:cvar.split('=')[1]})

    return config_keys

def load_updater_file(fname):

    with open(fname, 'r') as updatefile:
        return updatefile.read()

def load_install_file(fname):

    with open(fname, 'r') as installfile:
        installs = []
        directs = []
        install_keys = {}
        dcount = 1
        installbuf = installfile.read().strip().split('\n##')
        for obj in installbuf:
            if obj.startswith('#'):
                continue
            installs.append(obj)

        for i in installs:
            directive = i.split('\n')
            direct_keys = []
            for d in directive:
                var = d.split('=')[0]
                val = ''.join(d.split('=')[1:])
                if var == '' or val == '':
                    continue
                keypair = {var:val}
                direct_keys.append(keypair)
            install_keys.update({dcount:direct_keys})
            dcount += 1
        return install_keys

def banner():

    os.system('clear')
    print '''
###############################################################
#             ___                               __
#            /   |  _____________  ____  ____ _/ /
#           / /| | / ___/ ___/ _ \/ __ \/ __ '/ /
#          / ___ |/ /  (__  )  __/ / / / /_/ / /
#         /_/  |_/_/  /____/\___/_/ /_/\__,_/_/
#
# Arsenal | A script to download and install additional tools
#         | and extra pentesting utilities to Kali Linux 2.
###############################################################
    '''

banner()
config_vars = load_config_file('/opt/arsenal/conf/arsenal.conf')
updater_file = config_vars['UPDATES_INSTALL_FILE']
install_file = config_vars['TOOLS_INSTALL_FILE']
extras_file = config_vars['EXTRA_INSTALL_FILE']
update_buf = load_updater_file(updater_file)
install_buf = load_install_file(install_file)
print update_buf

for ib in install_buf:
    keylist = install_buf[ib]
    tempkeys = {}
    for k in keylist:
        keyname = ''.join(k.keys())
        tempkeys.update({keyname:k[keyname]})
    title = tempkeys['TITLE']
    if title.startswith('#'):
        continue
    install_to = tempkeys['PATH']
    client_cmd = tempkeys['CLIENT_CMD']
    package_url = tempkeys['URL']
    preinstall = tempkeys['PREINSTALL']
    install = tempkeys['INSTALL']

    arsenalstr = '{} {} {}'.format(client_cmd,package_url,install_to)
    if preinstall != 'None':
        arsenalstr = preinstall + ' && ' + arsenalstr

    if install != 'None':
        arsenalstr = arsenalstr + ' && ' + install

    print '-' * border
    print "[<>] Installing {} to {}...".format(title,install_to)
    print "[<>] URL: {}".format(package_url)
    print "[<>] Full Command: {}".format(arsenalstr)
    print '-' * border
