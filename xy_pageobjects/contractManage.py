# conding=utf-8

from framework.base_page import BasePage

class ContractManage(BasePage):
    contract = "xpath=>//*[@id='menu-box']/ul/li[4]/a"
    contract_maintain = "xpath=>/html/body/div[1]/div/div/div[3]/div[3]/div/a"
    query_template = "xpath=>//*[@id='searchForm']/ul/li[5]/input"
    # contract_template = "//*[@class='ui-grid-canvas']/div[2]/div/div[1]/div[2]/div[2]/div/span/a"
    contract_template = "//*[@class='ui-grid-canvas']/div/div/div/div/span/a"
    contract_template2 = "//*[@class='ui-grid-canvas']/div/div/div/div/span/a"
    unfold = "xpath=>//*[@class='drop']/a"
    query_btn = "xpath=>//*[@id='CM0200020004']"
    frame = "//iframe[contains(@class,'tabPanels')]"

    def send_contract(self):
        self.clicked(self.contract)

    def send_contract_maintain(self):
        self.clicked(self.contract_maintain)

    def input_query_template(self, text):
        self.type(self.query_template, text)

    def get_contract_template(self):
        return self.driver.find_element_by_xpath(self.contract_template).text

    def get_contract_template2(self):
        return self.driver.find_element_by_xpath(self.contract_template2).text

    def send_unfold(self):
        self.clicked(self.unfold)

    def send_query_btn(self):
        self.clicked(self.query_btn)

    def switch_to_frame(self):
        self.driver.switch_to.frame(self.driver.find_element_by_xpath(self.frame))

    def switch_back(self):
        self.driver.switch_to.default_content()