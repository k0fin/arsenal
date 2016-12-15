#!/usr/bin/python2

import sys
import os
import subprocess
import requests

from bs4 import BeautifulSoup

download_url = 'http://www.cobaltstrike.com'
download_uri ='/download'
get_download_url = requests.get('{}{}'.format(download_url,download_uri))
cs_soup = BeautifulSoup(get_download_url.text, 'html.parser')
for cs in cs_soup.findAll('a', {'id':'link'}):
    cs_download_url = str(cs).split('"')[1].strip().replace('trial.zip','trial.tgz')
    os.system('wget {}{} -O /opt/cs.tgz'.format(download_url,cs_download_url))

os.system('cd /opt && tar xvf cs.tgz && rm cs.tgz && cd arsenal')
