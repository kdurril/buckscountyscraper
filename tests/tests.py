#!/usr/bin/env python
# -*- coding: utf-8 -*-

import unittest
import re
from sys import path
path.append('/Users/kdurril/Development/buckscounty')
from parse import *

class TestBucksParseMethods(unittest.TestCase):
    def setUp(self):
        with open("./buckscounty/bucks/928471.html","r") as file:
            b = file.read()
            c = BeautifulSoup(b,'lxml')
            self.soup = tableParse(soup=c,record_id="928471")
            self.time_pat = '[0-1]\d:\d{2}'
            self.date_pat = '\d{2}/\d{2}/\d{4}'
            self.travel_pat = '\d{2}\.\d'
            self.digit_pat = '\d+'
            self.binary_list = ["NO","YES","N/A"]

    def test_isSoup(self):
        self.assertTrue(self.soup.alt_parse())
    def test_isRecord_id(self):
        self.assertTrue(self.soup.record_id)
    def test_isParsed(self):
        self.assertTrue(self.soup.parsed)
    def test_isCompliance(self):
        self.assertTrue(self.soup.compliance)
    def test_isSummary(self):
        self.assertTrue(self.soup.summary)
    def test_isFullRecord(self):
        self.assertTrue(self.soup.full_record())
    def test_isFullRecordJson(self):
        self.assertTrue(self.soup.full_record_to_json())
    def test_isViolation(self):
        self.assertRegex(self.soup.summary.violation,self.digit_pat)
    def test_isRiskCount(self):
        self.assertRegex(self.soup.summary.risk_count,self.digit_pat)
    def test_isArrival(self):
        self.assertRegex(self.soup.summary.arrival,self.time_pat)
    def test_isTime(self):
        self.assertRegex(self.soup.summary.ins_time,self.time_pat)
    def test_isDate(self):
        self.assertRegex(self.soup.summary.ins_date,self.date_pat)
    def test_isTravel(self):
        self.assertRegex(self.soup.summary.travel,self.travel_pat)
    def test_isLicensure(self):
        self.assertIn(self.soup.summary.license,self.binary_list)
    def test_isClosure(self):
        self.assertIn(self.soup.summary.closure,self.binary_list)

if __name__ == '__main__':
    unittest.main()