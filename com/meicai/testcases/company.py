# coding=utf-8
'''
Created on 2016 4 7

@author: Jo
'''

from ..page.company import CompanyManage

import unittest

class company(unittest.TestCase):

    def setUp(self):
        self.cm = CompanyManage()

    def tearDown(self):
        self.cm =None


    def test_searchCompanyCheckDefault(self):
        
        self.assertTrue(True, self.cm.searchCompanyCheckDefault(self.driver))
        


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()