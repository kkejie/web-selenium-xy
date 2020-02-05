# coding=utf-8

import time
import unittest
from framework.logger import Logger
from framework.browser_engine import BrowserEngine
from xy_pageobjects.login import Login
from xy_pageobjects.logout import Logout
from xy_pageobjects.bazaarManage import BazaarManage

logger = Logger(logger="Bazaar").getlog()


class Bazaar(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        browser = BrowserEngine(cls)
        cls.driver = browser.open_browser(cls)
        # 登录
        login = Login()
        login.log_in(cls)

    @classmethod
    def tearDownClass(cls):
        # 登出
        cls.driver.switch_to.default_content()
        logout = Logout()
        logout.log_out(cls)
        cls.driver.quit()

    def test1_query_bazaar(self):
        '''
        * 测试用例在这里编写
        * 针对不同的测试用例修改类名及日志标识
        '''
        bazaar = BazaarManage(self.driver)
        bazaar.send_bazaar()
        bazaar.send_business()
        bazaar.switch_to_window()
        bazaar.switch_to_frame()
        time.sleep(3)
        self.assertEqual("商机编号", bazaar.get_business_num(), "进入我的商机页面失败！")
        try:
            assert "商机编号" in bazaar.get_business_num()
            logger.info("进入我的商机页面成功。")
        except Exception as e:
            logger.error("进入我的商机页面失败！", e)
            bazaar.get_windows_img()
        time.sleep(2)

    def test2_query_bazaar(self):
        '''
        * 测试用例在这里编写
        * 针对不同的测试用例修改类名及日志标识
        '''
        bazaar = BazaarManage(self.driver)
        bazaar.switch_back()
        bazaar.send_toubiaogl()
        bazaar.send_wode()
        bazaar.switch_to_frame2()
        time.sleep(3)
        self.assertEqual("投标编号", bazaar.get_toubiaonum(), "进入我的投标页面失败！")
        try:
            assert "投标编号" in bazaar.get_toubiaonum()
            logger.info("进入我的投标页面成功。")
        except Exception as e:
            logger.error("进入我的投标页面失败！", e)
            bazaar.get_windows_img()
        time.sleep(1)

if __name__ == '__main__':
    unittest.main()