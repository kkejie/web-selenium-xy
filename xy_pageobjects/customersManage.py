# coding=utf-8

from framework.base_page import BasePage

class CustomersManage(BasePage):
    customers = "xpath=>/html/body/div[1]/div/ul/li[2]/a"
    contact_query = "xpath=>/html/body/div[1]/div/div/div[1]/div[1]/div/a[2]"
    unfold = "xpath=>//*[@class='drop']/a"
    tel = "//table/tbody/tr[1]/td[6]"
    tel2 = "//table/tbody/tr[2]/td[6]"
    query_tel = "xpath=>//form/ul/li[5]/input"
    query_btn = "xpath=>//*[@id='btnSearch']"
    frame = "//iframe[contains(@class,'tabPanels')]"

    def send_customers(self):
        self.clicked(self.customers)

    def send_contact_query(self):
        self.clicked(self.contact_query)

    def send_unfold(self):
        self.clicked(self.unfold)

    def get_tel(self):
        return self.driver.find_element_by_xpath(self.tel).text


    def get_tel2(self):
        return self.driver.find_element_by_xpath(self.tel2).text

    def input_query_tel(self, text):
        self.type(self.query_tel, text)

    def send_query_btn(self):
        self.clicked(self.query_btn)

    def switch_to_frame(self):
        self.driver.switch_to.frame(self.driver.find_element_by_xpath(self.frame))

    def switch_back(self):
        self.driver.switch_to.default_content()