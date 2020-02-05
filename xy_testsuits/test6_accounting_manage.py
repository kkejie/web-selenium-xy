# coding=utf-8

import time
import unittest
from framework.logger import Logger
from framework.browser_engine import BrowserEngine
from xy_pageobjects.login import Login
from xy_pageobjects.logout import Logout
from xy_pageobjects.accountingManage import AccountingManage

logger = Logger(logger="Accounting").getlog()


class Accounting(unittest.TestCase):

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

    def test1_query_accounting(self):
        '''
        * 测试用例在这里编写
        * 针对不同的测试用例修改类名及日志标识
        '''
        accounting = AccountingManage(self.driver)
        accounting.send_accounting()
        accounting.send_pay()
        accounting.switch_to_window()
        accounting.switch_to_frame()
        time.sleep(3)
        accounting.send_unfold()
        name = accounting.get_pay_num2()
        accounting.input_pay_num(name)
        accounting.send_query_btn()
        self.assertEqual(name, accounting.get_pay_num(), "通过支付单据号查询付款支付失败！")
        try:
            assert name in accounting.get_pay_num()
            logger.info("通过支付单据号查询付款支付成功。")
        except Exception as e:
            logger.error("通过支付单据号查询付款支付失败！", e)
            accounting.get_windows_img()
        time.sleep(1)

if __name__ == '__main__':
    unittest.main()