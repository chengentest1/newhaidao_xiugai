import time
import unittest

import ddt

from datapack.getExcelData import getData
from log.addLog import LOG
from myTestCase.myCase import MyTestCase
from package.mamberCenterPage import MemeberCenterPage

from pageElement.loginPage import LoginPage

data_list=getData()

@ddt.ddt
class RunCase(MyTestCase):
    def setLogin(self,name,passwd):
        LoginPage(self.driver).user_login(name,passwd)
    @ddt.data(*data_list)
    def testopen(self,now):
        try:
            self.setLogin(now[0],now[1])
        except Exception as e:
            LOG.info(e)
        time.sleep(2)
        try:
            webcome=MemeberCenterPage(self.driver).get_webcome_link_text()
            self.assertEqual(webcome,now[2])
        except Exception as e:
            LOG.info(e)
if __name__=="__main__":
    unittest.main()