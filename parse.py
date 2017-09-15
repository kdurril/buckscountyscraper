from bs4 import BeautifulSoup
from itertools import chain, islice
from operator import getitem
from collections import namedtuple
from glob import iglob
from os import path
import json

#with open("/Users/kdurril/Development/buckscounty/bucks/928471.html","r") as file:
#        b = file.read()
#        b = BeautifulSoup(b,'lxml')

class tableParse(object):

    def __init__(self, soup=None,record_id=None):
        "soup is a bs4 object, record_id is the file name"
        self.soup = soup
        self.record_id = record_id
        self.parse = [list(i) for i in self.test_parse(self.soup)]

    def __str__(self):
        return self.record_id

    def __repr__(self):
        return self.record_id
    
    def get_table(self, soup=None):
        "retreive html tables"
        for table in soup.body.find_all('table'):
            if not table.table:            
                yield table
    
    def alt_table(self):
        "retreive html tables"
        count = 0
        for table in self.soup.body.find_all('table'):
            if count in (1,2,3,6,7,8,10,11,12,19,20):            
                yield table
                count += 1
            else:
                count += 1

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

    def alt_parse(self):
        for table in self.alt_table():
            yield self.parse_table(table=table)

    @property
    def parsed(self):
        self.parse = [list(i) for i in self.test_parse(self.soup)]
        return self.parse
    
    def client(self):
        #{'Food Facility', 'Address', 'City/State', 'Zip Code', 'Telephone'}
        Client = namedtuple('Client', ['food_facility', 'address', 'city_state', 'zip_code', 'telephone'])
        #return dict(tuple(x.string.strip() for x in y.children if x.string != None) for y in [list(i) for i in self.alt_parse()][2][0].children if y != '\n')
        coll_1 = []
        for y in [list(i) for i in self.alt_parse()][2][0].children:
            if y != '\n':
                coll_2 = []
                for x in y.children:
                    if x.string != None:
                        coll_2.append(x.string.strip())    
                coll_1.append(tuple(coll_2))
        return Client(*[i[1] for i in coll_1])

    def compliance(self):
        if self.parse:
            comply = list(chain.from_iterable(self.parse[4:9]))
            return [i for i in comply if len(i)>1 and getitem(i,0).isdigit()]
        else:
            comply = chain.from_iterable(self.parsed()[4:9])
            return [i for i in comply if len(i)>1 and getitem(i,0).isdigit()]

    def compliance_tuple(self):
        Compliance = namedtuple('Compliance',['tag','compliance',
                                              'label','cos',
                                              'repeat'])
        return (Compliance(*i) for i in self.compliance())

    @property
    def compliance2(self):
        coll = [list(parse_row(i)) for i in self.alt_parse()]
        comply = chain.from_iterable(coll[3:8])
        return [i for i in comply if len(i)>1 and getitem(i,0).isdigit()]

    @property
    def summary(self):
        Summary = namedtuple('Summary',['violation','risk_count',
                                        'arrival','travel',
                                        'ins_date','ins_time',
                                        'license','closure'])
        smry = Summary(
                self.parse[1][0][2],
                self.parse[1][1][1],
                self.parse[1][2][1],
                self.parse[1][3][1].strip(),
                self.parse[1][0][4],
                self.parse[1][2][1],
                self.parse[1][2][3],
                self.parse[1][3][3])
        return smry

    def full_record(self):
        return (self.summary,self.client(),list(self.compliance_tuple()))

    def full_record_to_json(self):
        record = self.full_record()
        to_json = {'client':{**{'record_id': self.record_id},
                             **record[0]._asdict(),
                             **(record[1]._asdict())},
                   'compliance':[i._asdict() for i in record[2]]}
        return to_json

def test_gather():
    coll = []
    bucks_data = iglob("./bucks/92855*.html")
    for i in bucks_data:
        with open(i,'r') as file:
            soup = BeautifulSoup(file.read(),'lxml')
            record_id = path.basename(file.name[:-5])
            pars = tableParse(soup,record_id)
            coll.append(pars)
    return coll
