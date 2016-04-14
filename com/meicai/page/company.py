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
import random



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
    
    ## 检索出的结果数据各个字段对应的列
    ID_RESULT_XPATH='//*[@id="company_grid_index_table"]/tbody/tr[%s]/td[2]'  ## 门店id
    CITY_RESULT_XPATH='//*[@id="company_grid_index_table"]/tbody/tr[%s]/td[3]'     ##城市
    NAME_RESULT_XPATH='//*[@id="company_grid_index_table"]/tbody/tr[%s]/td[4]' ##商户名称
    BRANCH_RESULT_XPATH='//*[@id="company_grid_index_table"]/tbody/tr[%s]/td[5]'##分店标识
    PERSON_NAME_RESULT_XPATH='//*[@id="company_grid_index_table"]/tbody/tr[%s]/td[6]'##负责人姓名
    PHONE_RESULT_XPATH='//*[@id="company_grid_index_table"]/tbody/tr[%s]/td[7]'##电话
    ADDR_RESULT_XPATH='//*[@id="company_grid_index_table"]/tbody/tr[%s]/td[8]'##地址
    TIME_RESULT_XPATH='//*[@id="company_grid_index_table"]/tbody/tr[%s]/td[10]'##收货时间
    STATUS_RESULT_XPATH='//*[@id="company_grid_index_table"]/tbody/tr[%s]/td[11]'##状态

    ## 商户信息和地址页面链接
    RANDLINE_DATA_COMPANYADDRESS_XPATH = '//*[@id="company_grid_index_table"]/tbody/tr[%s]/td[8]/a' ## 查询结果某一列的数据，商户地址点击进入链接
    RANDTLINE_DATA_COMPANYNAME_XPATH = '//*[@id="company_grid_index_table"]/tbody/tr[%s]/td[4]/a' ## 查询结果某一列的数据，商户名称点击进入链接
    ## 操作和编辑的定位，需自定义行
    HANDLE_BUTTON_XPATH = '//*[@id="company_grid_index_table"]/tbody/tr[%]/td[12]/div/div/button' ## 首行的操作按键
    EDIT_HANDLE_BUTTON_XPATH = '//*[@id="company_grid_index_table"]/tbody/tr[%s]/td[12]/div/div/ul/li/a'  ##首行的操作按键中的编辑链接

    
    SUM_COMPANY_ID='total'  ## 当前查询结果的门店数
    SUM_TOTAL=0 ## 查询结果总数
    
    SEARCH_RESULT = '//*[@id="company_grid_index_table"]/tbody/tr' ## 查询有多少tr，就是当前页有多少结果
    
    
    
    ## 首行数据的商户id、商户名称、商户电话、商户地址
    FIRST_DATA_NAME_XPATH ='//*[@id="company_grid_index_table"]/tbody/tr/td[4]/a' ## 门店名称
    FIRST_DATA_PHONE_XPATH = '//*[@id="company_grid_index_table"]/tbody/tr/td[7]' # 门店电话
    FIRST_DATA_ADDR_XPATH= '//*[@id="company_grid_index_table"]/tbody/tr/td[8]/a' # 门店地址
    
    ## 跳转页    
    VIEW_COMPANY_TITLE = 'COMPANY - View Company'  ## 点击商户名称进入的页面的title
    COORDINATE_COMPANY_TITLE = 'COMPANY - Coordinate Company' ## 点击商户地址进入的页面的title
    
    VIEW_COMPANY_CUSTOM_XPATH = '//*[@id="custom_tab"]/a' # view company页面 【收货人】
    
    COORDINATE_ADDRESS_ID = 'address'    ## coordinate 页面的地址ID

    
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
    def searchCompany(self,city=u'全部',area=u'全部',status=u'全部',c_id='',name='',\
                      phone='',addr='',cus_phone=''):
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
            
    
    
    ## 检查检索结果正确性,
    def checkSearchCompanyResult(self,c_id='',city='',area='',name='',branch='',person_name='',\
                                 phone='',addr='',cus_time='',status='',cus_phone=''):
        
        if self.driver.find_element(By.ID,self.SUM_COMPANY_ID) == '0':
            return False
        else:
            results = self.driver.find_element(By.XPATH,self.SEARCH_RESULT)
            
            if c_id:
                for i in range(0,len(results)):
                    if self.driver.find_element(By.XPATH,self.ID_RESULT_XPATH % (i+1)).text != c_id:
                        return False
            if city:
                for i in range(0,len(results)):
                    if self.driver.find_element(By.XPATH,self.CITY_RESULT_XPATH % (i+1)).text != city:
                        return False
            if area and cus_phone:
                random_line_company_name = self.driver.find_element(By.XPATH,self.RANDTLINE_DATA_COMPANYNAME_XPATH % random.randrange(1,len(results)+1))
                return self.getInViewCompany(random_line_company_name, area,cus_phone)
                

            if name:
                for i in range(0,len(results)):
                    if name not in self.driver.find_element(By.XPATH,self.NAME_RESULT_XPATH % (i+1)).text :
                        return False
            if branch:
                for i in range(0,len(results)):
                    if self.driver.find_element(By.XPATH,self.BRANCH_RESULT_XPATH % (i+1)).text != branch:
                        return False
            if person_name:
                for i in range(0,len(results)):
                    if self.driver.find_element(By.XPATH,self.PERSON_NAME_RESULT_XPATH % (i+1)).text != person_name:
                        return False
            if phone:
                for i in range(0,len(results)):
                    if self.driver.find_element(By.XPATH,self.PHONE_RESULT_XPATH % (i+1)).text != phone:
                        return False
            if addr:
                for i in range(0,len(results)):
                    if addr not in self.driver.find_element(By.XPATH,self.ADDR_RESULT_XPATH % (i+1)).text:
                        return False
            if cus_time:
                for i in range(0,len(results)):
                    if self.driver.find_element(By.XPATH,self.TIME_RESULT_XPATH % (i+1)).text != cus_time:
                        return False
            if status:
                for i in range(0,len(results)):
                    if self.driver.find_element(By.XPATH,self.STATUS_RESULT_XPATH % (i+1)).text != status:
                        return False
        return True                           
                                
            
                
                    
    def editNewCompany(self,addr_check='',branck='',start_time='',end_time='',status=u'有效'):
        self.searchCompany(status=u'待处理')
        results = self.driver.find_element(By.XPATH,self.SEARCH_RESULT)
        line_num = len(results)
        if self.checkSearchCompanyResult(status=u'待处理') and line_num:
            line_num = random.randrange(1,line_num+1)
            company_id = self.driver.find_element(By.XPATH,self.ID_RESULT_XPATH % line_num)
            company_id_text = company_id.text
            
            handle_button = self.driver.find_element(By.XPATH,self.HANDLE_BUTTON_XPATH % line_num)
            handle_button_edit = self.driver.find_element(By.XPATH,self.EDIT_HANDLE_BUTTON_XPATH % line_num)
            self.editCompanyInfo(handle_button,handle_button_edit)
            
            
    
    def editValidCompany(self):   
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
    
    ## 点击商户名称，进入相关页面    检查区域和收货人电话
    def getInViewCompany(self,companyname_element,area_text,cus_phone):    
        cw_handle = self.driver.current_window_handle
        sleep(2)
        ## 进入第一行数据的商户名称，查看是否含有城市，和区域信息，比对title，如果都对返回True,有一个不符就返回False
        companyname_element.click()
        sleep(2)
        
        for i in self.driver.window_handles:
            if i != cw_handle:
                self.driver.switch_to_window(i)
                if companyname_element not in self.dirver.page_source:
                    logging.info(u'配送区域检查不通过')
                    return False
                elif self.driver.title != 'COMPANY - View Company':
                    logging.info(self.driver.title)
                    return False
                self.driver.find_element(By.XPATH,self.VIEW_COMPANY_CUSTOM_XPATH).click()
                if cus_phone not in  self.driver.page_source:
                    return False                
                
        self.driver.close()
        self.driver.switch_to_window(cw_handle)

    
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
    def editCompanyInfo(self,handle_button,handle_button_edit,name='',branch='',person_name='',phone='',start_time='',end_time='',addr='',status=''):
        
        handle_button.click()
        handle_button.switch_to(handle_button_edit).click()
        
        
        edit_active_element = self.driver.switch_to_active_element()
        
        edit_caixi = edit_active_element.find_element(By.XPATH,self.EDIT_COMPANY_CAIXI_XPATH)
        edit_name = edit_active_element.find_element(By.ID,self.EDIT_COMPANY_NAME_ID)
        edit_branch = edit_active_element.find_element(By.ID,self.EDIT_COMPANY_NAME_ID)
        edit_person_name = edit_active_element.find_element(By.ID,self.EDIT_COMPANY_NAME_ID)
        edit_phone = edit_active_element.find_element(By.ID,self.EDIT_COMPANY_NAME_ID)
        edit_start_time = edit_active_element.find_element(By.ID,self.EDIT_COMPANY_NAME_ID)
        edit_end_time = edit_active_element.find_element(By.ID,self.EDIT_COMPANY_NAME_ID)
        edit_addr = edit_active_element.find_element(By.ID,self.EDIT_COMPANY_NAME_ID)
        edit_status = edit_active_element.find_element(By.ID,self.EDIT_COMPANY_NAME_ID)
        edit_submit = edit_active_element.find_element(By.LINK_TEXT,u'确定')
        
        if name:
            inputText(edit_name,name)
        
        if branch:
            inputText(edit_branch,branch)
        
        if person_name:
            inputText(edit_person_name,person_name)
        
        if phone:
            inputText(edit_phone,phone)
        
        if start_time:
            Select(edit_start_time).select_by_visible_text(start_time)
        
        if end_time:
            Select(edit_end_time).select_by_visible_text(end_time)
        
        if addr:
            inputText(edit_addr,addr)
        
        if status:
            Select(edit_status).select_by_visible_text(status)
       
        ## 操作菜系，选择四川菜湖南菜和东北菜,没有菜系的时候才会操作；有菜系则不进行该部分操作
        if not edit_caixi.text:       
            edit_active_element.find_element(By.XPATH,self.EDIT_COMPANY_CAIXI_XPATH).click()
            caixi = self.driver.switch_to_active_element()
            caixi.find_element(By.XPATH,self.CAIXI_SICHUAN_XPATH).click()
            caixi.find_element(By.XPATH,self.CAIXI_HUNAN_XPATH).click()
            caixi.find_element(By.XPATH,self.CAIXI_DONGBEI_XPATH).click()
            caixi.find_element(By.LINK_TEXT,u'确定').click()

        ## 提交整体编辑数据
        edit_submit.click()
        
                
        

    
class UserManager(BasePage):
    
    def searchUser(self):
        pass
    def searchUserByPhone(self):
        pass    
    def searchUserById(self):
        pass

## 向element中输入text    
def inputText(element,text):
    element.clear()
    element.send_keys(text)

if __name__ == '__main__':
    pass