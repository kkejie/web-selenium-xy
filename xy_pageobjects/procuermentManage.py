# conding=utf-8

from framework.base_page import BasePage

class ProcuermentManage(BasePage):
    procuerment = "xpath=>/html/body/div[1]/div/ul/li[6]/a"
    ticket_apply = "xpath=>/html/body/div[1]/div/div/div[5]/div[6]/div/a[1]"
    document_num = "//*[@id='ticketZtBody']/div[2]/div[1]/table/tbody[1]/tr[1]/td[2]/a[2]/strong"
    document_num2 = "//*[@id='ticketZtBody']/div[2]/div[1]/table/tbody[2]/tr[1]/td[2]/a[2]/strong"
    query_document_num = "xpath=>/html/body/div[3]/div[1]/div[2]/form/ul/li[1]/input"
    query_btn = "xpath=>//*[@id='MM0600010006']"
    unfold = "xpath=>//*[@class='drop']/a"
    frame = "//iframe[contains(@class,'tabPanels')]"

    def send_procuerment(self):
        self.clicked(self.procuerment)

    def send_ticket_apply(self):
        self.clicked(self.ticket_apply)

    def get_document_num(self):
        return self.driver.find_element_by_xpath(self.document_num).text

    def get_document_num2(self):
        return self.driver.find_element_by_xpath(self.document_num2).text

    def input_order_num(self, text):
        self.type(self.query_document_num, text)

    def send_query_btn(self):
        self.clicked(self.query_btn)

    def send_unfold(self):
        self.clicked(self.unfold)

    def switch_to_frame(self):
        self.driver.switch_to.frame(self.driver.find_element_by_xpath(self.frame))

    def switch_back(self):
        self.driver.switch_to.default_content()