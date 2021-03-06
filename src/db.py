#!/usr/bin/env python
# -*- coding: utf-8 -*-
import psycopg2
import glob
import json

def createdb(database='db', user='user', password=None):
    con = psycopg2.connect(database=database, user=user, password=password)
    cur = con.cursor()
    cur.execute("CREATE TABLE bucks (inspection jsonb)")
    con.commit()
    con.close()

def json2db(input_data=None, database='db', user='user', password=None):
    "Add parseTable object"
    con = psycopg2.connect(database=database, user=user, password=password)
    cur = con.cursor()
    
    for doc in input_data:
        try:
            cur.execute("INSERT INTO bucks (inspection) VALUES (%s)",
            ([json.dumps(doc.full_record_to_json())]))
        except:
            pass
        finally:
            print(doc)
    
    con.commit()
    con.close()
    
#cur.execute('''CREATE INDEX idxinspectid ON inspection USING GIN ((inspection -> 'inspect_id'::text))''')
#    con.commit()

