from selenium import webdriver
from selenium.webdriver.common.by import By


class LoginPage:
    def __init__(self,drivet):
        # self.driver=webdriver.Chrome()
        self.driver=drivet
        self.url='http://localhost:8001/index.php?m=user&c=public&a=login'
    def open(self):
        self.driver.get(self.url)
    username_input_loc=(By.ID,"username")
    passwd_input_loc=(By.ID,"password")
    def inputName(self,name):
        self.driver.find_element(*self.username_input_loc).send_keys(name)
    def input_password(self,passwd):
        self.driver.find_element(*self.passwd_input_loc).send_keys(passwd)
    button_login=(By.CSS_SELECTOR,".login_btn.fl")
    def login_button(self):
        self.driver.find_element(*self.button_login).click()
        # self.driver.find_element_by_css_selector('.login_btn.fl').click()

    def user_login(self,name,passwd):
        self.open()
        self.inputName(name)
        self.input_password(passwd)
        self.login_button()
