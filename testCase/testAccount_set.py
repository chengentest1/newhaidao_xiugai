import unittest

import time

from datapack.getExcelData import getData
from myTestCase.myCase import MyTestCase
from package.mamberCenterPage import MemeberCenterPage
from pageElement.accountSetPage import AccountPage
from pageElement.loginPage import LoginPage
from pageElement.personalDataPage import PersonalData
import ddt

data_list=getData(1)
@ddt.ddt
class TestAccount(MyTestCase):
    def primise_Account(self):
        LoginPage(self.driver).user_login('chen123',123456)
        time.sleep(3)
        MemeberCenterPage(self.driver).account_Set()
        time.sleep(3)
        AccountPage(self.driver).personal_Data()
        time.sleep(2)
        personal=PersonalData(self.driver)
        return personal
    @ddt.data(*data_list)
    def testAccount(self,now):
        personal=self.primise_Account()
        personal.input_true_name(now[0])
        personal.sex_select()
        personal.delete_readonly(now[1])
        personal.input_QQ(now[2])
        # personal.click_button()
        # personal.get_wrong_Ture_name()
        # personal.get_wrong_QQ()

if __name__=="__main__":
    unittest.main()