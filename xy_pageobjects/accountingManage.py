# conding=utf-8

from framework.base_page import BasePage

class AccountingManage(BasePage):
    accounting = "xpath=>/html/body/div[1]/div/ul/li[7]/a"
    pay = "xpath=>/html/body/div[1]/div/div/div[6]/div[4]/div/a[4]"
    pay_num = "/html/body/div[1]/div[1]/div[3]/div[2]/div[1]/table/tbody/tr[1]/td[2]/a"
    pay_num2 = "/html/body/div[1]/div[1]/div[3]/div[2]/div[1]/table/tbody/tr[2]/td[2]/a"
    query_pay_num = "xpath=>/html/body/div[1]/div[1]/div[3]/div[1]/div[2]/form/ul/li[1]/input"
    query_btn = "xpath=>//*[@id='body']/div[2]/div/div/a[4]"
    unfold = "xpath=>//*[@class='drop']/a"
    frame = "//iframe[contains(@class,'tabPanels')]"

    def send_accounting(self):
        self.clicked(self.accounting)

    def send_pay(self):
        self.clicked(self.pay)

    def get_pay_num(self):
        return self.driver.find_element_by_xpath(self.pay_num).text

    def get_pay_num2(self):
        return self.driver.find_element_by_xpath(self.pay_num2).text

    def input_pay_num(self, text):
        self.type(self.query_pay_num, text)

    def send_query_btn(self):
        self.clicked(self.query_btn)

    def send_unfold(self):
        self.clicked(self.unfold)

    def switch_to_frame(self):
        self.driver.switch_to.frame(self.driver.find_element_by_xpath(self.frame))

    def switch_back(self):
        self.driver.switch_to.default_content()