from selenium.webdriver.common.by import By


class MemeberCenterPage:
    def __init__(self,driver):
        self.driver=driver
    webcome_link_loc=(By.CSS_SELECTOR,'.site-nav-right.fr > a:nth-child(1)')
    def get_webcome_link_text(self):
        return self.driver.find_element(*self.webcome_link_loc).text
    my_MemerCenter=(By.LINK_TEXT,'我的会员中心')
    def myMemerCenter(self):
        self.driver.find_element(*self.my_MemerCenter).click()
    Account_Setting=(By.LINK_TEXT,'账号设置')
    def account_Set(self):
        self.driver.find_element(*self.Account_Setting).click()
    My_news=(By.LINK_TEXT,'我的消息')
    def my_News(self):
        self.driver.find_element(*self.My_news).click()

