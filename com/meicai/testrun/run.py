# coding=utf-8
'''
Created on 2016��4��7��

@author: Jo
'''

import logging
import time
import unittest
import os

from ..page.login import Login

import HTMLTestRunner
from _imagingmath import abs_I

now=time.strftime('%Y%m%d-%H%M%S',time.localtime())

logging.basicConfig(level=logging.DEBUG,
                format='%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s',
                datefmt='%a, %d %b %Y %H:%M:%S',
                filename='web_%s.log' % now,
                filemode='w')

console = logging.StreamHandler()
console.setLevel(logging.INFO)
formatter = logging.Formatter('%(name)-12s: %(levelname)-8s %(message)s')
console.setFormatter(formatter)
logging.getLogger().addHandler(console)



abs_current_dir = os.path.abspath(os.path.curdir)
asb_case_dir = os.path.abspath('abs_current_dir%stestcases' % os.pathsep)


def creatTestSuit():
    testsuit = unittest.TestSuite()
    discover = unittest.defaultTestLoader.discover(asb_case_dir, 'test*.py', None)


if __name__ == '__main__':
    
    testunit=unittest.TestSuite()
    testunit.addTest(unittest.makeSuite(Company))
    filename='%s_Company.html' % now
    fp=file(filename,'wb')
    runner = HTMLTestRunner.HTMLTestRunner(
        stream=fp,
        title=u'测试报告',
        description=u'用例执行情况：')    
      
    runner.run(testunit)