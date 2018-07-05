from selenium.webdriver.common.by import By


class AccountPage:
    def __init__(self,driver):
        self.driver=driver
    account_Information_button=(By.CSS_SELECTOR,'.hover')
    def account_Information(self):
        self.driver.find_element(*self.account_Information_button).click()

    personal_data=(By.LINK_TEXT,'个人资料')
    def personal_Data(self):
        self.driver.find_element(*self.personal_data).click()

    Head_set=(By.LINK_TEXT,'头像设置')
    def head_Set(self):
        self.driver.find_element(*self.Head_set).click()

    Account_security = (By.LINK_TEXT, '个人资料')
    def account_Security(self):
        self.driver.find_element(*self.Account_security).click()
