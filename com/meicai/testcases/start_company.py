# coding=utf-8
'''
Created on 2016 4 7

@author: Jo
'''



from com.meicai.page.company import CompanyManage
from com.meicai.page.login import Login

import unittest
from time import sleep

class company(unittest.TestCase):

    def setUp(self):
        self.driver = Login('http://company.stage.yunshanmeicai.com/').login()
        self.cm = CompanyManage(self.driver)

    def tearDown(self):
        self.cm =None
        sleep(2)
        self.driver.quit()


    def test1_searchCompanyCheckDefault(self):
        
        self.assertTrue(self.cm.searchCompanyCheckDefault())
    
    def test2_searchCompanyByCity(self):
         
        self.assertTrue(self.cm.searchCompanyByCity())
     


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    pass