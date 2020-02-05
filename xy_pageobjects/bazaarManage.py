# conding=utf-8

from framework.base_page import BasePage

class BazaarManage(BasePage):
    bazaar = "xpath=>/html/body/div[1]/div/ul/li[8]/a"
    business = "xpath=>/html/body/div[1]/div/div/div[7]/div[1]/div/a[1]"
    business_num = "/html/body/div[1]/div[1]/div[4]/div[1]/div[1]/div[2]/div/div[2]/div[2]/div[1]/div[1]"
    unfold = "xpath=>//*[@class='drop']/a"
    frame = "//iframe[contains(@class,'tabPanels')]"

    def send_bazaar(self):
        self.clicked(self.bazaar)

    def send_business(self):
        self.clicked(self.business)

    def get_business_num(self):
        return self.driver.find_element_by_xpath(self.business_num).text

    def send_unfold(self):
        self.clicked(self.unfold)

    def switch_to_frame(self):
        self.driver.switch_to.frame(self.driver.find_element_by_xpath(self.frame))

    def switch_back(self):
        self.driver.switch_to.default_content()

    toubiaogl = "xpath=>/html/body/div[1]/div/ul/li[2]/a"
    wode = "xpath=>/html/body/div[1]/div/div/div[2]/div[1]/h1/a"
    tou = "/html/body/div[2]/div[1]/div[4]/div[1]/div[1]/div[2]/div/div[2]/div[2]/div[1]/div[1]"
    frame2 = "/html/body/div[2]/div[2]/iframe"

    def send_toubiaogl(self):
        self.clicked(self.toubiaogl)

    def send_wode(self):
        self.clicked(self.wode)

    def get_toubiaonum(self):
        return self.driver.find_element_by_xpath(self.tou).text

    def switch_to_frame2(self):
        self.driver.switch_to.frame(self.driver.find_element_by_xpath(self.frame2))