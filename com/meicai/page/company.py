# coding=utf-8
'''
Created on 2016 4 7 

@author: Jo 
'''

from basePage import BasePage
from selenium import webdriver
from selenium.webdriver.common.by import By

class CompanyManage(BasePage):
    
    CITY_SELECT_XPATH='//*[@id="search_form"]/div[1]/select'  ##城市下拉框
    AREA_SELECT_XPATH='//*[@id="search_form"]/div[2]/select'  ##区域下拉框 
    STATUS_SELECT_XPATH='//*[@id="search_form"]/div[3]/select' ##状态下拉框
    ID_INPUT_XPATH='//*[@id="search_form"]/div[4]/input'       ##商户ID
    NAME_INPUT_XPATH='//*[@id="search_form"]/div[5]/input'     ##商户name
    PHONE_INPUT_XPATH='//*[@id="search_form"]/div[6]/input'      ##商户电话
    ADDR_INPUT_XPATH='//*[@id="search_form"]/div[7]/input'           ##商户地址
    CUSTOMPHONE_INPUT_XPATH='//*[@id="search_form"]/div[8]/input'    ##收货人电话
    SEARCH_BUTTON_ID='search_btn'  ## 提交查询   
     

    ## 默认查询功能，
    def searchCompanyCheckDefault(self,driver):
        city = self.driver.find_element(By.XPATH,self.CITY_SELECT_XPATH)
        area = self.driver.find_element(By.XPATH,self.AREA_SELECT_XPATH)
        status = self.driver.find_element(By.XPATH,self.STATUS_SELECT_XPATH)
        if city.text == u'全部' and area.text == u'全部' and status.text == u'有效':
            return True
        else:
            return False
            
    def searchCompanyByCity(self):
        pass
    def searchCompanyByArea(self):
        pass
    def searchCompanyByStatus(self):
        pass
    def searchCompanyById(self):
        pass
    def searchCompanyByName(self):
        pass    
    def searchCompanyByPhone(self):
        pass
    def searchCompanyByAddress(self):
        pass
    def searchCompanyByCustomPhone(self):
        pass
    
class UserManager(BasePage):
    
    def searchUser(self):
        pass
    def searchUserByPhone(self):
        pass
    
    def searchUserById(self):
        pass


if __name__ == '__main__':
    pass