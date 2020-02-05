# coding=utf-8

import time
import unittest
from framework.logger import Logger
from framework.browser_engine import BrowserEngine
from xy_pageobjects.login import Login
from xy_pageobjects.logout import Logout
from xy_pageobjects.flowManage import FlowManage

logger = Logger(logger="Flow").getlog()


class Flow(unittest.TestCase):

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

    def test1_query_flow(self):
        '''
        * 测试用例在这里编写
        * 针对不同的测试用例修改类名及日志标识
        '''
        flow = FlowManage(self.driver)
        flow.send_flow()
        flow.send_mine_approve()
        flow.switch_to_window()
        flow.switch_to_frame()
        time.sleep(3)
        flow.send_unfold()
        name = flow.get_flow_title2()
        flow.input_query_flow_title(name)
        flow.send_query_btn()
        self.assertEqual(name, flow.get_flow_title(), "通过流程标题查询我审批的流程失败！")
        try:
            assert name in flow.get_flow_title()
            logger.info("通过流程标题查询我审批的流程成功。")
        except Exception as e:
            logger.error("通过流程标题查询我审批的流程失败！", e)
            flow.get_windows_img()
        time.sleep(1)

if __name__ == '__main__':
    unittest.main()