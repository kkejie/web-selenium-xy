# coding=utf-8

from framework.base_page import BasePage

class ProjectManage(BasePage):
    project_manage = "xpath=>/html/body/div[1]/div/ul/li[3]/a"
    project_cogfig = "xpath=>/html/body/div[1]/div/div/div[2]/div[1]/div/a[2]"
    unfold = "xpath=>//*[@class='drop']/a"
    query_btn = "xpath=>//*[@id='PM0900020002']"
    template_name = "//*[@id='workOperation']/div[2]/div/div[1]/div[1]/div[2]/a"
    template_name2 = "//*[@id='workOperation']/div[2]/div/div[2]/div[1]/div[2]/a"
    query_template = "xpath=>//*[@id='structureList']/div[2]/div[2]/ul/li[1]/input"
    frame = "//iframe[contains(@class,'tabPanels')]"

    def send_project(self):
        self.clicked(self.project_manage)

    def send_config(self):
        self.clicked(self.project_cogfig)

    def send_unfold(self):
        self.clicked(self.unfold)

    def send_query_btn(self):
        self.clicked(self.query_btn)

    def get_template_name(self):
        return self.driver.find_element_by_xpath(self.template_name).text


    def get_template_name2(self):
        return self.driver.find_element_by_xpath(self.template_name2).text

    def input_template_name(self, text):
        self.type(self.query_template, text)

    def switch_to_frame(self):
        self.driver.switch_to.frame(self.driver.find_element_by_xpath(self.frame))

    def switch_back(self):
        self.driver.switch_to.default_content()