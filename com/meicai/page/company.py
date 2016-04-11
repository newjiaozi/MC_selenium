# coding=utf-8
'''
Created on 2016 4 7 

@author: Jo 
'''

from basePage import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import logging
from time import sleep

logging.getLogger()

class CompanyManage(BasePage):
    
    ## 查询条件及提交
    CITY_SELECT_XPATH='//*[@id="search_form"]/div[1]/select'  ##城市下拉框
    AREA_SELECT_XPATH='//*[@id="search_form"]/div[2]/select'  ##区域下拉框 
    STATUS_SELECT_XPATH='//*[@id="search_form"]/div[3]/select' ##状态下拉框
    ID_INPUT_XPATH='//*[@id="search_form"]/div[4]/input'       ##商户ID
    NAME_INPUT_XPATH='//*[@id="search_form"]/div[5]/input'     ##商户name
    PHONE_INPUT_XPATH='//*[@id="search_form"]/div[6]/input'      ##商户电话
    ADDR_INPUT_XPATH='//*[@id="search_form"]/div[7]/input'           ##商户地址
    CUSTOMPHONE_INPUT_XPATH='//*[@id="search_form"]/div[8]/input'    ##收货人电话
    SEARCH_BUTTON_ID='search_btn'  ## 提交查询  
    
    
    CITY_RESULT_XPATH='//*[@id="company_grid_index_table"]/tbody/tr[%s]/td[3]' ##检索数据中城市所在列，需要替换到对应行  
    SUM_COMPANY_ID='total'  ## 当前查询的门店数
    SUM_TOTAL=0 ## 查询结果总数
    FIRSTLINE_DATA_COMPANYNAME_XPATH = '//*[@id="company_grid_index_table"]/tbody/tr[1]/td[4]/a'  ## 查询结果的第一条数据，商户名称点击进入的链接
    FIRSTLINE_DATA_COMPANYADDRESS_XPAHT = '//*[@id="company_grid_index_table"]/tbody/tr[1]/td[8]/a' ## 查询结果的第一条数据，商户地址点击进入链接
    COORDINATE_ADDRESS_ID = 'address'    ## coordinate 页面的地址ID
    HANDLE_BUTTON_XPATH = '//*[@id="company_grid_index_table"]/tbody/tr[1]/td[12]/div/div/button' ## 首行的操作按键
    EDIT_HANDLE_BUTTON_XPATH = '//*[@id="company_grid_index_table"]/tbody/tr[1]/td[12]/div/div/ul/li/a'  ##首行的操作按键中的编辑链接

    
    ## 编辑门店信息页面
    
    EDIT_COMPANY_NAME_ID ='company_name_input' ## 门店名称
    EDIT_COMPANY_BRANCH_ID = 'branch_mark_input' ## 分店标志
    EDIT_COMPANY_PERSON_NAME_ID = 'person_name' ## 负责人姓名
    EDIT_COMPANY_PHONE_ID = 'company_phone' ## 电话
    EDIT_COMPANY_CITY_ID = 'city_select' ## 城市
    EDIT_COMPANY_CAIXI_XPATH = '//*[@id="s2id_company_area_total_select"]/a' ## 菜系 
    EDIT_COMPANY_START_TIME_ID = 'company_expect_period_start' ## 最早收货时间
    EDIT_COMPANY_END_TIME_ID = 'company_expect_period_end' ## 最晚收货时间
    EDIT_COMPANY_PAY_ID = 'pay_way' ## 付款方式
    EDIT_COMPANY_ADDR_ID = 'company_address' ## 地址
    EDIT_COMPANY_DESC_ID = 'company_desc' ## 备注
    EDIT_COMPANY_TYPE_ID = 'extend_type' ## 特殊门店
    EDIT_COMPANY_STATUS_ID = 'company_status' ## 门店状态
    EDIT_COMPANY_REASON_ID = 'change_status_reason' ## 变更原因
    
    def __init__(self,driver):
        self.driver = driver
        BasePage.__init__(self, self.driver)

    ## 默认查询功能，
    def searchCompanyCheckDefault(self):
        city = self.driver.find_element(By.XPATH,self.CITY_SELECT_XPATH)        
        area = self.driver.find_element(By.XPATH,self.AREA_SELECT_XPATH)
        status = self.driver.find_element(By.XPATH,self.STATUS_SELECT_XPATH)
        
#         sum_total = WebDriverWait(self.dirver,10).until(EC.presence_of_element_located((By.ID,self.SUM_COMPANY_ID))) 
#         
#         self.SUM_TOTAL = int(sum_total.text)
        

        logging.info(Select(city).first_selected_option.text+Select(area).first_selected_option.text+Select(status).first_selected_option.text )
        if Select(city).first_selected_option.text == u'全部' and \
            Select(area).first_selected_option.text == u'全部' and \
            Select(status).first_selected_option.text == u'有效':
            return True
        else:
            return False
        
    ## 通过城市检索商户       
    def searchCompanyByCity(self):
        city = self.driver.find_element(By.XPATH,self.CITY_SELECT_XPATH)
        Select(city).select_by_visible_text(u'上海')
        submit = self.dirver.find_element(By.ID,self.SEARCH_BUTTON_ID)
        submit.click()
        
#         sum_total = WebDriverWait(self.dirver,10).until(EC.presence_of_element_located((By.ID,self.SUM_COMPANY_ID)))        
#         
#         previous_sum = self.SUM_TOTAL
#         self.SUM_TOTAL = sum_total.text
#         
#         if previous_sum < self.SUM_TOTAL:
#             return False              
        
        sleep(3)
        for i in range(1,21):
            city = self.driver.find_element(By.XPATH,self.CITY_RESULT_XPATH % i)
            if city.text != u'上海':
                return False
        return True        
        
    ## 通过选择区域检索数据    
    def searchCompanyByArea(self):
        city = self.driver.find_element(By.XPATH,self.CITY_SELECT_XPATH)
        Select(city).select_by_visible_text(u'北京')
        area = self.driver.find_element(By.XPATH,self.AREA_SELECT_XPATH)
        Select(area).select_by_visible_text(u'亦庄')
        submit = self.dirver.find_element(By.ID,self.SEARCH_BUTTON_ID)
        submit.click()        
#         cw_handle = self.driver.current_window_handle
#         sleep(2)
#         ## 进入第一行数据的商户名称，查看是否含有城市，和区域信息，比对title，如果都对返回True,有一个不符就返回False
#         firstline_company_name = self.driver.find_element(By.XPATH,self.FIRSTLINE_DATA_COMPANYNAME_XPATH)
#         firstline_company_name.click()
#         sleep(2)
#         
#         for i in self.driver.window_handles:
#             if i != cw_handle:
#                 self.driver.switch_to_window(i)
# 
#                 if u'北京 ' not in self.dirver.page_source:
#                     logging.info(u'北京 not in')
#                     return False
#                 elif u'亦庄' not in self.dirver.page_source:
#                     logging.info(u'亦庄 not in')
#                     return False
#                 elif self.driver.title != 'COMPANY - View Company':
#                     logging.info(self.driver.title)
#                     return False
#         self.driver.close()
#         self.driver.switch_to_window(cw_handle)  
#                 
#         sleep(2)
#         ## 进入第一行数据的商户地址，查看title，以及地址与进入之前是否一致，都正确则返回True，有一项不符就返回False
#         fistline_company_address =  self.driver.find_element(By.XPATH,self.FIRSTLINE_DATA_COMPANYADDRESS_XPAHT)
#         fistline_company_address_text = fistline_company_address.text  
#         fistline_company_address.click()
#         sleep(2)
#         for i in self.driver.window_handles:
#             if i != cw_handle:
#                 self.driver.switch_to_window(i)
# 
#                 c_addr = self.driver.find_element(By.ID,self.COORDINATE_ADDRESS_ID)
#                 
#                 
#                 
#                 if self.driver.title != 'COMPANY - Coordinate Company':
#                     logging.info(self.driver.title)
#                     return False
#                 
#                 
#                 elif c_addr.get_attribute('value') not in fistline_company_address_text:
#                     logging.info(c_addr.get_attribute('value')+"##"+fistline_company_address_text)
#                     return False
#              
#         self.driver.close()
#         self.driver.switch_to_window(cw_handle)          
        
        if self.getInViewCompany():
            if self.getInCoordinateCompany():
                return True
        return False
            
        
          
        
        
        
        
                
        
    def searchCompanyByStatus(self):
        pass
    def searchCompanyById(self):
        pass
    def searchCompanyByName(self):
        pass    
    def searchCompanyByPhone(self):
        self.driver
    def searchCompanyByAddress(self):
        pass
    def searchCompanyByCustomPhone(self):

        pass
    
    ## 将城市选择全部，配送区域选择全部，门店状态为全部，其他输入框都清空
    def searchConditionReset(self):
        city = self.driver.find_element(By.XPATH,self.CITY_SELECT_XPATH)
        area = self.driver.find_element(By.XPATH,self.AREA_SELECT_XPATH)
        status = self.driver.find_element(By.XPATH,self.STATUS_SELECT_XPATH)
        c_id = self.driver.find_element(By.XPATH,self.ID_INPUT_XPATH)
        c_name = self.driver.find_element(By.XPATH,self.NAME_INPUT_XPATH)
        c_phone = self.driver.find_element(By.XPATH,self.PHONE_INPUT_XPATH)
        c_addr = self.driver.find_element(By.XPATH,self.ADDR_INPUT_XPATH)
        c_cus_phone = self.driver.find_element(By.XPATH,self.CUSTOMPHONE_INPUT_XPATH)
                        
        Select(city).select_by_index(1)
        Select(area).select_by_index(1)
        Select(status).select_by_index(1)
        c_id.clear()
        c_name.clear()
        c_phone.clear()
        c_addr.clear()
        c_cus_phone.clear()    
    
    ## 点击商户名称，进入相关页面    
    def getInViewCompany(self):    
        cw_handle = self.driver.current_window_handle
        sleep(2)
        ## 进入第一行数据的商户名称，查看是否含有城市，和区域信息，比对title，如果都对返回True,有一个不符就返回False
        firstline_company_name = self.driver.find_element(By.XPATH,self.FIRSTLINE_DATA_COMPANYNAME_XPATH)
        firstline_company_name.click()
        sleep(2)
        
        for i in self.driver.window_handles:
            if i != cw_handle:
                self.driver.switch_to_window(i)

                if u'北京 ' not in self.dirver.page_source:
                    logging.info(u'北京 not in')
                    return False
                elif u'亦庄' not in self.dirver.page_source:
                    logging.info(u'亦庄 not in')
                    return False
                elif self.driver.title != 'COMPANY - View Company':
                    logging.info(self.driver.title)
                    return False
        self.driver.close()
        self.driver.switch_to_window(cw_handle)
        return True  
    
    ## 点击商户地址，进入相关页面
    def getInCoordinateCompany(self):
        cw_handle = self.driver.current_window_handle
        sleep(2)
        ## 进入第一行数据的商户地址，查看title，以及地址与进入之前是否一致，都正确则返回True，有一项不符就返回False
        fistline_company_address =  self.driver.find_element(By.XPATH,self.FIRSTLINE_DATA_COMPANYADDRESS_XPAHT)
        fistline_company_address_text = fistline_company_address.text  
        fistline_company_address.click()
        sleep(2)
        for i in self.driver.window_handles:
            if i != cw_handle:
                self.driver.switch_to_window(i)
                c_addr = self.driver.find_element(By.ID,self.COORDINATE_ADDRESS_ID)        
                if self.driver.title != 'COMPANY - Coordinate Company':
                    logging.info(self.driver.title)
                    return False
                
                elif c_addr.get_attribute('value') not in fistline_company_address_text:
                    logging.info(c_addr.get_attribute('value')+"##"+fistline_company_address_text)
                    return False
             
        self.driver.close()
        self.driver.switch_to_window(cw_handle) 
        return True 
    
    ## 点击操作，选择编辑
    def editCompanyInfo(self):
        c_handle = self.driver.find_element(By.XPATH,self.HANDLE_BUTTON_XPATH)
        c_handle.click()
        c_edit = self.driver.find_element(By.XPATH,self.EDIT_HANDLE_BUTTON_XPATH)
        c_handle.switch_to(c_edit).click()
          
    
class UserManager(BasePage):
    
    def searchUser(self):
        pass
    def searchUserByPhone(self):
        pass    
    def searchUserById(self):
        pass


if __name__ == '__main__':
    pass