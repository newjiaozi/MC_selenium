# coding=utf-8
'''
Created on 2016 4 7

@author: Jo
'''

from ..page.company import CompanyManage
from ..page.login import Login

import unittest

class company(unittest.TestCase):

    def setUp(self):
        self.driver = Login('http://company.stage.yunshanmeicai.com/')
        self.cm = CompanyManage()

    def tearDown(self):
        self.cm =None
        self.driver.quit()


    def test1_searchCompanyCheckDefault(self):
        
        self.assertTrue(self.cm.searchCompanyCheckDefault(self.driver))
    
    def test2_searchCompanyByCity(self):
        
        self.assertTrue(self.cm.searchCompanyByCity(self.driver))
        


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    pass