# coding=utf-8

import time
import unittest
from framework.logger import Logger
from framework.browser_engine import BrowserEngine
from xy_pageobjects.login import Login
from xy_pageobjects.logout import Logout
from xy_pageobjects.systemReport import SystemReport

logger = Logger(logger="System").getlog()


class System(unittest.TestCase):

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

    def test1_query_system(self):
        '''
        * 测试用例在这里编写
        * 针对不同的测试用例修改类名及日志标识
        '''
        system = SystemReport(self.driver)
        system.send_yewuxitong()
        system.send_project()
        system.switch_to_window()
        time.sleep(3)
        # system.switch_to_frame()
        self.assertEqual("项目基本信息查询", system.get_title(), "进入项目基本信息查询页面失败！")
        try:
            assert "项目基本信息查询" in system.get_title()
            logger.info("进入项目基本信息查询页面成功。")
        except Exception as e:
            logger.error("进入项目基本信息查询页面失败！", e)
            system.get_windows_img()
        time.sleep(1)

    def test2_query_system(self):
        '''
        * 测试用例在这里编写
        * 针对不同的测试用例修改类名及日志标识
        '''
        system = SystemReport(self.driver)
        # system.switch_back()
        system.send_xiaoshougl()
        system.send_xiaoshoudingdan()
        time.sleep(3)
        # system.switch_to_frame2()
        self.assertEqual("销售订单查询", system.get_title2(), "进入销售订单查询页面失败！")
        try:
            assert "销售订单查询" in system.get_title2()
            logger.info("进入销售订单查询页面成功。")
        except Exception as e:
            logger.error("进入销售订单查询页面失败！", e)
            system.get_windows_img()
        time.sleep(1)

if __name__ == '__main__':
    unittest.main()