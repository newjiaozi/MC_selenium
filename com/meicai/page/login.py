# coding=utf-8
'''
Created on 2016 4 7 

@author: Jo
'''

import os
import logging

from selenium import webdriver

logging.getLogger()
class Login():
    def __init__(self,url_addr):
        self.url_addr = url_addr
    def login(self):
        ## 获取chrome默认设置，这样就可以免除登录，使用已有的cookie进行登录；
        ## 因为识别验证码不好识别，所以使用免登陆方式；
#         profile_dir=r'C:\Users\Administrator\AppData\Local\Google\Chrome\User Data'
#         chrome_options = webdriver.ChromeOptions()
#         chrome_options.add_argument("user-data-dir="+os.path.abspath(profile_dir))         
#         browser=webdriver.Chrome(chrome_options=chrome_options) 

        firefox_profile = webdriver.FirefoxProfile(r'C:\Users\Administrator\AppData\Roaming\Mozilla\Firefox\Profiles\a5dra0qm.default')
        
        browser = webdriver.Firefox(firefox_profile=firefox_profile)
        browser.implicitly_wait(10)
        browser.maximize_window()  
        browser.get(self.url_addr)
        logging.info(self.url_addr) 
        return browser
    
if __name__ == '__main__':
    pass