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

#     def setUp(self):
#         self.driver = Login('http://company.stage.yunshanmeicai.com/').login()
#         self.cm = CompanyManage(self.driver)
# 
#     def tearDown(self):
#         self.cm =None
#         sleep(2)
#         self.driver.quit()

    @classmethod
    def setUpClass(cls):
        cls.driver= Login('http://company.stage.yunshanmeicai.com/').login()
        cls.cm = CompanyManage(cls.driver)
        
    
    @classmethod
    def tearDownClass(cls):
        cls.cm = None
        sleep(2)
        cls.driver.quit()

#     def test001_searchCompanyCheckDefault(self):         
#         self.assertTrue(self.cm.searchCompanyCheckDefault())    
#     
#     def test002_searchCompanyByCity(self):
#         self.cm.searchConditionReset()
#         self.cm.searchCompany(city=u'上海')    
#         self.assertTrue(self.cm.checkSearchCompanyResult(city=u'上海'))  
#         
#     def test003_searchCompanyByArea(self):
#         self.cm.searchConditionReset()
#         self.cm.searchCompany(city=u'北京',area =u'惠新里') 
#         self.assertTrue(self.cm.checkSearchCompanyResult(area =u'惠新里'))
#      
#     def test004_searchCompanyByCusPhone(self):
#         self.cm.searchConditionReset()
#         self.cm.searchCompany(cus_phone='13600112233') 
#         self.assertTrue(self.cm.checkSearchCompanyResult(cus_phone='13600112233'))
#         
#     
#     def test005_searchCompanyByStatus_Valid(self):
#         self.cm.searchConditionReset()
#         self.cm.searchCompany(status=u'有效')
#         self.assertTrue(self.cm.checkSearchCompanyResult(status=u'有效'))
#     
#     def test006_searchCompanyByStatus_Invalid(self):
#         self.cm.searchConditionReset()
#         self.cm.searchCompany(status=u'无效')
#         self.assertTrue(self.cm.checkSearchCompanyResult(status=u'无效'))        
# 
#     def test007_searchCompanyByStatus_Stop(self):
#         self.cm.searchConditionReset()
#         self.cm.searchCompany(status=u'停用')
#         self.assertTrue(self.cm.checkSearchCompanyResult(status=u'停用'))  
# 
#     def test008_searchCompanyByStatus_Delete(self):
#         self.cm.searchConditionReset()
#         self.cm.searchCompany(status=u'已删除')
#         self.assertTrue(self.cm.checkSearchCompanyResult(status=u'已删除'))  
# 
#     def test009_searchCompanyByStatus_Ready(self):
#         self.cm.searchConditionReset()
#         self.cm.searchCompany(status=u'待处理')
#         self.assertTrue(self.cm.checkSearchCompanyResult(status=u'待处理')) 
#         
#     def test010_searchCompanyById(self):
#         self.cm.searchConditionReset()
#         self.cm.searchCompany(c_id='228828')
#         self.assertTrue(self.cm.checkSearchCompanyResult(c_id='228828'))
#         
#     def test011_searchCompanyByName(self):
#         self.cm.searchConditionReset()
#         self.cm.searchCompany(name='AUTO')
#         self.assertTrue(self.cm.checkSearchCompanyResult(name='AUTO'))  
#     
#     def test012_searchCompanyByPhone(self):
#         self.cm.searchConditionReset()
#         self.cm.searchCompany(phone='13683581996')
#         self.assertTrue(self.cm.checkSearchCompanyResult(phone='13683581996'))
#         
#     def test013_searchCompanyByAddr(self):               
#         self.cm.searchConditionReset()
#         self.cm.searchCompany(addr='AUTO')
#         self.assertTrue(self.cm.checkSearchCompanyResult(addr='AUTO'))    

    def test014_handleNewCompany(self):               
        self.assertTrue(self.cm.editCompany(branch='AUTO',start_time='7:00',end_time='11:00',status=u'待处理'))
        
    def test015_handleOldCompany(self):               
        self.assertTrue(self.cm.editCompany(addr=u'中电信息大厦',branch='AUTO',start_time='8:00',end_time='11:00',status=u'有效'))         

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    pass