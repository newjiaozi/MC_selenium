# coding=utf-8
'''
Created on 2016��4��7��

@author: Jo
'''

import logging
import time
import unittest
import os



import HTMLTestRunner

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



abs_pardir = os.path.abspath(os.path.pardir)

abs_case_dir = os.path.join(abs_pardir,'testcases')

logging.info(abs_case_dir)


def creatTestSuit():
    testsuit = unittest.TestSuite()
    discover = unittest.defaultTestLoader.discover(abs_case_dir, 'start_*.py', None)
    for i in discover:
        for j in i:
            testsuit.addTest(j)
    return testsuit

if __name__ == '__main__':
    
    testsuits = creatTestSuit()
    logging.info(testsuits)
    filename='%s_Company.html' % now
    fp=file(filename,'wb')
    runner = HTMLTestRunner.HTMLTestRunner(
        stream=fp,
        title=u'测试报告',
        description=u'用例执行情况：')    
      
    runner.run(testsuits)