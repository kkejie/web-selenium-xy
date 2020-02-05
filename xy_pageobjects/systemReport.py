# conding=utf-8

from framework.base_page import BasePage

class SystemReport(BasePage):
    yewuxitong = "xpath=>/html/body/div[1]/div/ul/li[9]/a"
    project = "xpath=>/html/body/div[1]/div/div/div[8]/div[1]/div/a[1]"
    title = "/html/body/ul/li/a"
    unfold = "xpath=>//*[@class='drop']/a"
    frame = "//iframe[contains(@class,'tabPanels')]"

    def send_yewuxitong(self):
        self.clicked(self.yewuxitong)

    def send_project(self):
        self.clicked(self.project)

    def get_title(self):
        return self.driver.find_element_by_xpath(self.title).text

    def send_unfold(self):
        self.clicked(self.unfold)

    def switch_to_frame(self):
        self.driver.switch_to.frame(self.driver.find_element_by_xpath(self.frame))

    def switch_back(self):
        self.driver.switch_to.default_content()

    xiaoshougl = "xpath=>/html/body/div[1]/div/ul/li[2]/a"
    xiaoshoudingdan = "xpath=>/html/body/div[1]/div/div/div[2]/div[1]/h1/a"
    title2 = "/html/body/ul/li[2]/a"
    frame2 = "/html/body/div[2]/div[2]/iframe"

    def send_xiaoshougl(self):
        self.clicked(self.xiaoshougl)

    def send_xiaoshoudingdan(self):
        self.clicked(self.xiaoshoudingdan)

    def get_title2(self):
        return self.driver.find_element_by_xpath(self.title2).text

    def switch_to_frame2(self):
        self.driver.switch_to.frame(self.driver.find_element_by_xpath(self.frame2))