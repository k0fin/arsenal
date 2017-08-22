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
# Arsenal | > A Python script to download an arsenal of additional
#         |   penetration testing tools.
#         | > Tested on Kali Linux 2.
###############################################################

border = blessings.Terminal().width

def arsenal_menu():
    config_vars = load_config_file('/opt/arsenal/conf/arsenal.conf')

    menu = '''
[ 1 ] - Launch Updates
[ 2 ] - Install Tools
[ 3 ] - Exit Arsenal

    '''
    print menu

    select = int(raw_input('[<>] Select an option: '))
    if select < 1 or select > 4:
        print '[--] Invalid selection.'
        banner()
        arsenal_menu()

    if select == 1:
        confirm = raw_input('[<>] This option will update and upgrade your Kali Linux distro. Continue? (y / n): ')
        if confirm.lower() == 'y':
            os.system('apt-get -y update && apt-get -y upgrade && apt-get -y dist-upgrade')
        else:
            arsenal_menu()

    elif select == 2:
        confirm = raw_input('[<>] This option will install the tools in arsenal-tools to your Kali Linux distro. Continue? (y / n): ')
        if confirm.lower() == 'y':
            install_file = config_vars['TOOLS_INSTALL_FILE']
            install_buf = load_install_file(install_file)
            arsenal_tools_install(install_buf)
        else:
            arsenal_menu()

    elif select == 3:
        print '[<>] Goodbye!'
        sys.exit()

    else:
        arsenal_menu()

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

def load_extras_file(fname):

    with open(fname, 'r') as extrasfile:
        extras = []
        extrakeys = {}
        dcount = 1
        extrasbuf = extrasfile.read().strip().split('\n##')
        for obj in extrasbuf:
            if obj.startswith('#'):
                continue
            extras.append(obj)

        for e in extras:
            directive = e.split('\n')
            direct_keys = []
            for d in directive:
                var = d.split('=')[0]
                val = "".join(d.split('=')[1:])
                if var == '' or val == '':
                    continue
                keypair = {var:val}
                direct_keys.append(keypair)
            extrakeys.update({dcount:direct_keys})
            dcount += 1
        return extrakeys

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

def arsenal_tools_install(install_buf):

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
        os.system('{} &'.format(arsenalstr))
        print '-' * border

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

def main():
    banner()
    arsenal_menu()

if __name__ == '__main__':
    main()
