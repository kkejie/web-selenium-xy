# coding=utf-8

import time

from framework.logger import Logger
from framework.base_page import BasePage

logger = Logger(logger = "Login").getlog()
class Login():
    @staticmethod
    def log_in(self):
        self.driver.find_element_by_xpath('//*[@id="username"]').clear()
        self.driver.find_element_by_xpath('//*[@id="username"]').send_keys('yangfan5')
        self.driver.find_element_by_xpath('//*[@id="password"]').clear()
        self.driver.find_element_by_xpath('//*[@id="password"]').send_keys('ccs.xiangyun')
        self.driver.find_element_by_xpath('//*[@id="authcode"]').clear()
        self.driver.find_element_by_xpath('//*[@id="authcode"]').send_keys('aaaa')
        self.driver.find_element_by_xpath('//input[@name="submit"]').click()
        time.sleep(2)
        name = self.driver.find_element_by_xpath('//*[@id="_userName"]').text
        loginpage = BasePage(self.driver)
        try:
            assert "杨帆" in name
            logger.info("登录成功。")
        except Exception as e:
            logger.info("登录失败。", e)
            loginpage.get_windows_img()  # 调用基类截图方法