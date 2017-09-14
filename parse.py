from bs4 import BeautifulSoup
from itertools import chain
from operator import getitem
from collections import namedtuple
from os import path

#with open("/Users/kdurril/Development/buckscounty/bucks/928471.html","r") as file:
#        b = file.read()
#        b = BeautifulSoup(b,'lxml')

class tableParse(object):

    def __init__(self, soup=None,record_id=None):
        self.soup = soup
        self.record_id = record_id
        self.parse = None

    def __str__():
        return 
    
    def get_table(self, soup=None):
        "retreive html tables"
        for table in soup.body.find_all('table'):
            if not table.table:            
                yield table
            #if table.table.table:
            #else:
            #    [[y.string for y in i.children] for i in ca[3].find_all('td')]

    def parse_table(self, table=None):
        for element in table:
            if element != '\n':
                yield element

    def parse_row(self, table_element=None):
        for row in table_element:
            yield tuple(cell.string for cell in row.find_all('td'))

    def test_parse(self, soup=None):
        for table in self.get_table(soup):
            yield self.parse_row(table_element=self.parse_table(table=table))

    @property
    def parsed(self):
        self.parse = [list(i) for i in self.test_parse(self.soup)]
        return self.parse
    
    @property
    def compliance(self):
        if self.parse:
            comply = list(chain.from_iterable(self.parse[4:9]))
            return [i for i in comply if len(i)>1 and getitem(i,0).isdigit()]
        else:
            comply = chain.from_iterable(self.parsed()[4:9])
            return [i for i in comply if len(i)>1 and getitem(i,0).isdigit()]

    @property
    def summary(self):
        Summary = namedtuple('Summary',['violation','risk_count',
                                        'arrival','travel',
                                        'ins_date','ins_time',
                                        'license','closure'])
        
        smry = Summary(self.parse[1][0][2],
                self.parse[1][1][1],
                self.parse[1][3][1].strip(),
                self.parse[1][0][2],
                self.parse[1][1][3],
                self.parse[1][2][3],
                self.parse[1][3][3])
        return smry
 
def get_table(soup=None):
        "treive html tables"
        for table in soup.body.find_all('table'):
            if not table.table:            
                yield table

def parse_table(table=None):
        for element in table:
            if element != '\n':
                yield element

def parse_row(table_element=None):
        for row in table_element:
            yield tuple(cell.string for cell in row.find_all('td'))

def test_parse(soup=None):
        for table in get_table(soup):
            yield parse_row(table_element=parse_table(table=table))

def test_gather():
    coll = []
    for i in bucks_data:
        with open(i,'r') as file:
            soup = BeautifulSoup(file.read(),'lxml')
            record_id = path.basename(file.name[:-5])
            pars = tableParse(soup,record_id)
            coll.append(pars)
    return coll


#d = [list(i) for i in c.parsed]
#compliance = chain.from_iterable(d[4:9])
#compliance = [i for i in compliance if len(i)>1 and getitem(i,0).isdigit()]

#[[y.string for y in i.children] for i in ca[3].find_all('td')]

