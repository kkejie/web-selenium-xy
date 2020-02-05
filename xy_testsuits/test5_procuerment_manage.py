# coding=utf-8

import time
import unittest
from framework.logger import Logger
from framework.browser_engine import BrowserEngine
from xy_pageobjects.login import Login
from xy_pageobjects.logout import Logout
from xy_pageobjects.procuermentManage import ProcuermentManage

logger = Logger(logger="Procuerment").getlog()


class Procuerment(unittest.TestCase):

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

    def test1_query_procuerment(self):
        '''
        * 测试用例在这里编写
        * 针对不同的测试用例修改类名及日志标识
        '''
        procuerment = ProcuermentManage(self.driver)
        procuerment.send_procuerment()
        procuerment.send_ticket_apply()
        time.sleep(2)

        procuerment.switch_to_window()
        time.sleep(2)
        procuerment.switch_to_frame()
        time.sleep(3)
        procuerment.send_unfold()
        name = procuerment.get_document_num2()
        procuerment.input_order_num(name)
        procuerment.send_query_btn()
        self.assertEqual(name, procuerment.get_document_num(), "通过收票单据号查询收票申请失败！")
        try:
            assert name in procuerment.get_document_num()
            logger.info("通过收票单据号查询收票申请成功。")
        except Exception as e:
            logger.error("通过收票单据号查询收票申请失败！", e)
            procuerment.get_windows_img()
        time.sleep(1)

if __name__ == '__main__':
    unittest.main()