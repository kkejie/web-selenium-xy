# conding=utf-8

from framework.base_page import BasePage

class MarketManage(BasePage):
    market = "xpath=>//*[@id='menu-box']/ul/li[5]/a"
    market_order = "xpath=>/html/body/div[1]/div/div/div[4]/div[1]/div/a"
    order_num = "//*[@id='saleOrderList']/div[1]/table/tbody[1]/tr[1]/td[2]/a[2]/strong"
    order_num2 = "//*[@id='saleOrderList']/div[1]/table/tbody[2]/tr[1]/td[2]/a[2]/strong"
    query_order_num = "xpath=>/html/body/div[1]/div/div[2]/div[2]/form/ul/li[1]/input"
    query_btn = "xpath=>//*[@id='SD0100010006']"
    unfold = "xpath=>//*[@class='drop']/a"
    frame = "//iframe[contains(@class,'tabPanels')]"

    def send_market(self):
        self.clicked(self.market)

    def send_market_order(self):
        self.clicked(self.market_order)

    def get_order_num(self):
        return self.driver.find_element_by_xpath(self.order_num).text

    def get_order_num2(self):
        return self.driver.find_element_by_xpath(self.order_num2).text

    def input_order_num(self, text):
        self.type(self.query_order_num, text)

    def send_query_btn(self):
        self.clicked(self.query_btn)

    def send_unfold(self):
        self.clicked(self.unfold)

    def switch_to_frame(self):
        self.driver.switch_to.frame(self.driver.find_element_by_xpath(self.frame))

    def switch_back(self):
        self.driver.switch_to.default_content()