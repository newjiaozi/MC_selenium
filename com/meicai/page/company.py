# coding=utf-8
'''
Created on 2016 4 7 

@author: Jo 
'''

from basePage import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select


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
    
    SEARCH_RESULT = '//*[@id="company_grid_index_table"]/tbody/tr' ## 查询有多少tr，就是当前页有多少结果
    
    
    ## 随机选择一行进入 商户信息和地址页面
    RANDLINE_DATA_COMPANYADDRESS_XPATH = '//*[@id="company_grid_index_table"]/tbody/tr[%s]/td[8]/a' ## 查询结果某一列的数据，商户地址点击进入链接
    RANDTLINE_DATA_COMPANYNAME_XPATH = '//*[@id="company_grid_index_table"]/tbody/tr[%s]/td[4]/a' ## 查询结果某一列的数据，商户名称点击进入链接
    
    ## 首行数据的商户id、商户名称、商户电话、商户地址
    FIRST_DATA_NAME_XPATH ='//*[@id="company_grid_index_table"]/tbody/tr/td[4]/a' ## 门店名称
    FIRST_DATA_PHONE_XPATH = '//*[@id="company_grid_index_table"]/tbody/tr/td[7]' # 门店电话
    FIRST_DATA_ADDR_XPATH= '//*[@id="company_grid_index_table"]/tbody/tr/td[8]/a' # 门店地址
    
    ## 跳转页
    
    VIEW_COMPANY_TITLE = 'COMPANY - View Company'  ## 点击商户名称进入的页面的title
    COORDINATE_COMPANY_TITLE = 'COMPANY - Coordinate Company' ## 点击商户地址进入的页面的title
    
    
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
    
    
    ## 选择菜系页面
    CAIXI_SICHUAN_XPATH = '//*[@id="class_body"]/div[5]/div[1]' ## 四川菜
    CAIXI_HUNAN_XPATH = '//*[@id="class_body"]/div[5]/div[2]' ## 湘(湖南)菜
    CAIXI_DONGBEI_XPATH = '//*[@id="class_body"]/div[5]/div[2]' ## 东北菜
    
    
    
    def __init__(self,driver):
        self.driver = driver
        BasePage.__init__(self, self.driver)

    ## 默认查询功能，
    def searchCompanyCheckDefault(self):
        city = self.driver.find_element(By.XPATH,self.CITY_SELECT_XPATH)        
        area = self.driver.find_element(By.XPATH,self.AREA_SELECT_XPATH)
        status = self.driver.find_element(By.XPATH,self.STATUS_SELECT_XPATH)
      

        logging.info(Select(city).first_selected_option.text+Select(area).first_selected_option.text+Select(status).first_selected_option.text )
        if Select(city).first_selected_option.text == u'全部' and \
            Select(area).first_selected_option.text == u'全部' and \
            Select(status).first_selected_option.text == u'有效':
            return True
        else:
            return False
        
    ## 通过城市检索商户       
    def searchCompanyByCity(self,city_text=u'北京'):
        city = self.driver.find_element(By.XPATH,self.CITY_SELECT_XPATH)
        Select(city).select_by_visible_text(city_text)
        submit = self.dirver.find_element(By.ID,self.SEARCH_BUTTON_ID)
        submit.click()              
        sleep(3)
        
        results = self.driver.find_elements(By.XPATH,self.SEARCH_RESULT)
        
        for i in range(0,len(results)):
            city = self.driver.find_element(By.XPATH,self.CITY_RESULT_XPATH % (i+1))
            if city.text != city:
                return False
        return True        
        
    ## 通过选择区域检索数据    
    def searchCompanyByArea(self,city_text=u'北京',area_text=u'亦庄'):
        city = self.driver.find_element(By.XPATH,self.CITY_SELECT_XPATH)
        Select(city).select_by_visible_text(city_text)
        area = self.driver.find_element(By.XPATH,self.AREA_SELECT_XPATH)
        Select(area).select_by_visible_text(area_text)
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
        

    ## 检索数据，通过 选择城市，区域，状态，id，名称，电话，地址，收货人电话 各个条件检索
    def searchCompany(self,city=u'全部',area=u'全部',status=u'全部',c_id='',name='',phone='',addr='',cus_phone=''):
        city_element = self.driver.find_element(By.XPATH,self.CITY_SELECT_XPATH)
        Select(city_element).select_by_visible_text(city)
        area_element = self.driver.find_element(By.XPATH,self.AREA_SELECT_XPATH)
        Select(area_element).select_by_visible_text(area) 
        status_element = self.driver.find_element(By.XPATH,self.STATUS_SELECT_XPATH)
        Select(status_element).select_by_visible_text(status)
        submit_element = self.driver.find_element(By.XPATH,self.SEARCH_BUTTON_ID) 
        
        
        if c_id:
            id_element = self.driver.find_element(By.XPATH,self.ID_INPUT_XPATH)
            inputText(id_element, c_id)
        if name:
            name_element = self.driver.find_element(By.XPATH,self.ID_INPUT_XPATH)
            inputText(name_element, name)
        if phone:
            phone_element = self.driver.find_element(By.XPATH,self.ID_INPUT_XPATH)
            inputText(phone_element, phone)
        if addr:
            addr_element = self.driver.find_element(By.XPATH,self.ID_INPUT_XPATH)
            inputText(addr_element, addr)
        if cus_phone:
            cus_phone_element = self.driver.find_element(By.XPATH,self.ID_INPUT_XPATH)
            inputText(cus_phone_element, cus_phone)            
        submit_element.click()    
            
    
    
    ## 检查检索结果正确性
    def checkSearchResult(self,c_id='',name='',phone='',addr='',cus_phone=''):
        if c_id:
            self.driver.find_element()
        
        
        
        
            
            
            
          
        
    
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
        edit_active_element = self.driver.switch_to_active_element()
        edit_name = edit_active_element.find_element(By.ID,self.EDIT_COMPANY_NAME_ID)
        edit_name.clear()
        edit_name.sendkeys(u'Jo_web_测试')
        
        edit_status = edit_active_element.find_element(By.ID,self.EDIT_COMPANY_STATUS_ID)
        Select(edit_status).select_by_visible_text(u'有效')          

        edit_active_element.find_element(By.XPATH,self.EDIT_COMPANY_CAIXI_XPATH).click()
        caixi = self.driver.switch_to_active_element()
        caixi.find_element(By.XPATH,self.CAIXI_SICHUAN_XPATH).click()
        caixi.find_element(By.XPATH,self.CAIXI_HUNAN_XPATH).click()
        caixi.find_element(By.XPATH,self.CAIXI_DONGBEI_XPATH).click()
        caixi.find_element(By.LINK_TEXT,u'确定').click()
#         edit_cancel = edit_active_element.find_element(By.LINK_TEXT,u'取消')
        edit_submit = edit_active_element.find_element(By.LINK_TEXT,u'确定')
        
        edit_submit.click()        
        

    
class UserManager(BasePage):
    
    def searchUser(self):
        pass
    def searchUserByPhone(self):
        pass    
    def searchUserById(self):
        pass
    
def inputText(element,text):
    element.clear()
    element.send_keys(text)

if __name__ == '__main__':
    pass