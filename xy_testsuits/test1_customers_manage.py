# coding=utf-8

import time
import unittest
import sys
from framework.logger import Logger
from framework.browser_engine import BrowserEngine
from xy_pageobjects.login import Login
from xy_pageobjects.logout import Logout
from xy_pageobjects.customersManage import CustomersManage

logger = Logger(logger = "Customers").getlog()

class Customers(unittest.TestCase):

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

    def test1_query_customers(self):
        '''
        * 测试用例在这里编写
        * 针对不同的测试用例修改类名及日志标识
        '''
        customers = CustomersManage(self.driver)
        customers.send_customers()
        customers.send_contact_query()
        customers.switch_to_window()
        time.sleep(2)
        customers.switch_to_frame()
        time.sleep(10)
        customers.send_unfold()
        tel = customers.get_tel2()
        customers.input_query_tel(tel)
        customers.send_query_btn()
        time.sleep(2)
        self.assertEqual(tel, customers.get_tel(), "通过电话查询失败！")
        try:
            assert tel in customers.get_tel()
            logger.info("通过电话查询成功。")
        except Exception as e:
            logger.error("通过电话查询失败！", e)
            customers.get_windows_img()
        time.sleep(2)

if __name__ == '__main__':
    unittest.main()