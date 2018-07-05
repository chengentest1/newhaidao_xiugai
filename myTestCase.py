import unittest
import os

import time

from package.HTMLTestRunner import HTMLTestRunner
from tool.mail import send_email

path=os.path.dirname(__file__)

if __name__=="__main__":
    now = time.strftime('%Y-%m-%d %H-%M-%S')
    suite=unittest.defaultTestLoader.discover('./pageElement',pattern='testuu.py')
    # unittest.TextTestRunner().run(suite)
    base_path=path+'/report/'+now+'test_report.html'
    file=open(base_path,'wb')
    HTMLTestRunner(stream=file, verbosity=1, title="博为峰测试报告", description="测试环境: Server 2008; 浏览器:'Chrome'").run(suite)
    file.close()
    # send_email(base_path)

