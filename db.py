#!/usr/bin/env python
# -*- coding: utf-8 -*-
from parse import *
import psycopg2
import glob
import json

def test_gather():
    coll = []
    bucks_data = iglob("./bucks/*.html")
    for i in bucks_data:
        with open(i,'r') as file:
            soup = BeautifulSoup(file.read(),'lxml')
            record_id = path.basename(file.name[:-5])
            pars = tableParse(soup,record_id)
            coll.append(pars)
    return coll

def createdb(database='postgres', user='kenneth', password=None):
	con = psycopg2.connect(database=database, user=user, password=password)
    cur = con.cursor()
    cur.execute("CREATE TABLE bucks (inspection jsonb)")
    cur.execute("idxinspectid" gin ((inspection -> 'inspect_id'::text)))
    con.commit()
    con.close()


def json2db(input_data=test_gather(), database='postgres', user='kenneth', password=None):
    "Add text from initial pdf to text parsing - this loses its structure"
    con = psycopg2.connect(database=database, user=user, password=password)
    cur = con.cursor()
    
    for doc in input_data:
        try:
            cur.execute("INSERT INTO bucks (inspection) VALUES (%s)", 
            (json.dumps(doc.full_record_to_json())))
        except:
            pass
        finally:
            print(doc)
    
    con.commit()
    con.close()

