# conding=utf-8

from framework.base_page import BasePage

class FlowManage(BasePage):
    flow = "xpath=>//*[@id='menu-box']/ul/li[10]/a"
    mine_approve = "xpath=>/html/body/div[1]/div/div/div[9]/div/div/a[3]"
    flow_title = "//*[@id='processRunItem']/tbody/tr[1]/td[1]/a"
    flow_title2 = "//*[@id='processRunItem']/tbody/tr[2]/td[1]/a"
    query_flow_title = "xpath=>//*[@id='searchForm']/ul/li[1]/input"
    query_btn = "xpath=>//*[@id='btnSearch']"
    unfold = "xpath=>//*[@class='drop']/a"
    frame = "//iframe[contains(@class,'tabPanels')]"

    def send_flow(self):
        self.clicked(self.flow)

    def send_mine_approve(self):
        self.clicked(self.mine_approve)

    def get_flow_title(self):
        return self.driver.find_element_by_xpath(self.flow_title).text

    def get_flow_title2(self):
        return self.driver.find_element_by_xpath(self.flow_title2).text

    def input_query_flow_title(self, text):
        self.type(self.query_flow_title, text)

    def send_query_btn(self):
        self.clicked(self.query_btn)

    def send_unfold(self):
        self.clicked(self.unfold)

    def switch_to_frame(self):
        self.driver.switch_to.frame(self.driver.find_element_by_xpath(self.frame))

    def switch_back(self):
        self.driver.switch_to.default_content()