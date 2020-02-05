# coding=utf-8

from framework.base_page import BasePage
import time
from framework.logger import Logger

logger = Logger(logger = "Logout").getlog()

class Logout():
    @staticmethod
    def log_out(self):
        self.driver.find_element_by_xpath('//*[@id="topFrame"]/ul/li[4]/a/i').click()
        time.sleep(1)
        self.driver.find_element_by_xpath('/html/body/div[6]/div[2]/div[2]/button[2]').click()
        time.sleep(1)
        txt = self.driver.find_element_by_xpath('/html/body/div[1]/div/div/div/form/div/div[2]/a').text
        logoutpage = BasePage(self.driver)
        try:
            assert "修改密码" in txt
            logger.info("登出成功。")
        except Exception as e:
            logger.error("登出失败。", e)
            logoutpage.get_windows_img()  # 调用基类截图方法