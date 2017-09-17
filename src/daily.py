#!/usr/bin/env python
# -*- coding: utf-8 -*-
# This is a daily file for downloading achd inspections

import time
import requests as r
import urllib.request
import urllib.error
import datetime as dt
import sys
from itertools import chain
from functools import wraps
from os import mkdir, path, stat

from glob import glob
from os.path import basename

def bucks(inspect_id=None):
    "scraper for bucks county"
    base_url = "http://pa.healthinspections.us/_templates/100/Food%20Inspection/_report_full.cfm"
    inspect_id = inspect_id
    domain_id = '100'
    for inspection in range(inspect_id, inspect_id+100):
        inspect="inspectionID="+str(inspection)
        domain="domainID="+domain_id
        full_url = base_url+"?"+inspect+"&"+domain
        yield {'inspect_url':full_url,'inspect_id':inspection}

def grab_txt(inspect_url=None,inspect_id=None):
    "Takes inspection from url_prep, download pdf"
    opener = urllib.request.build_opener()
    opener.addheaders = [('User-agent',\
        '''Mozilla/5.0 
        (X11; Ubuntu; Linux x86_64; rv:55.0) 
        Gecko/20170613 Firefox/54.0'''),\
        ('Accept-encoding', 'gzip')]
    folder = "./bucks"
    txtfile = inspect_id
    if path.isdir(folder) == False:
                mkdir(folder)
    with opener.open(inspect_url) as viewout:
        if viewout.getheader('Content-Type') == 'text/html;charset=UTF-8':  
            outputfolder = folder+'/'+txtfile+'.txt'
            with open(outputfolder, "w") as txtout:
                    txtout.write(viewout.read())
            return outputfolder
                    #time.sleep(1)
        else:
            print(viewout.getheader('Content-Type'))

'''http://pa.healthinspections.us/_templates/100/Food%20Inspection/_report_full.cfm?inspectionID=928462&domainID=100'''
def get_txt(inspect_url=None,inspect_id=None, to_file=False):
    b = r.get(inspect_url)
    if to_file:
        if b.headers['Content-Type'] == 'text/html;charset=UTF-8':
            with open(str(inspect_id)+".html",'w') as file:
                file.write(b.text)
        return {'request':b,'inspect_id':inspect_id}
    else:
        return {'request':b,'inspect_id':inspect_id}

if __name__ == '__main__':
    for x in bucks(inspect_id=928900):
        get_txt(**x,to_file=False)
