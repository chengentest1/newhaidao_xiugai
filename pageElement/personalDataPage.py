from selenium.webdriver.common.by import By


class PersonalData:
    def __init__(self,driver):
        self.driver=driver

    True_name=(By.ID,'true_name')
    def input_true_name(self,truename):
        self.driver.find_element(*self.True_name).clear()
        self.driver.find_element(*self.True_name).send_keys(truename)

    Sex_select=(By.XPATH,'//input[@id="xb"][@value=1]')
    def sex_select(self):
        self.driver.find_element(*self.Sex_select).click()
    Date_loc=(By.ID,'date')
    def delete_readonly(self,birthday_date):
        self.driver.execute_script("document.getElementById('date').removeAttribute('readonly')")
        self.driver.find_element(*self.Date_loc).clear()
        self.driver.find_element(*self.Date_loc).send_keys(birthday_date)
    def updata_date(self):
        self.driver.execute_script('$("#date").val("1990-12-09")')
    QQ_loc=(By.ID,'qq')
    def input_QQ(self,qq):
        self.driver.find_element(*self.QQ_loc).clear()
        self.driver.find_element(*self.QQ_loc).send_keys(qq)
    regison_button=(By.CLASS_NAME,'btn4')
    def click_button(self):
        self.driver.find_element(*self.regison_button).click()
    def get_wrong_Ture_name(self):
        msg=self.driver.find_element(By.CSS_SELECTOR,' form > li:nth-child(3) > p > span').text
        print(msg)
    def get_wrong_QQ(self):
        msg1=self.driver.find_element(By.CSS_SELECTOR,'form > li:nth-child(6) > p > span').text
        print(msg1)


