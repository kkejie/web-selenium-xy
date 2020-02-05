# coding=utf-8

import time
import unittest
from framework.logger import Logger
from framework.browser_engine import BrowserEngine
from xy_pageobjects.login import Login
from xy_pageobjects.logout import Logout
from xy_pageobjects.contractManage import ContractManage

logger = Logger(logger = "Contract").getlog()

class Contract(unittest.TestCase):

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

    def test1_query_contract(self):
        '''
        * 测试用例在这里编写
        * 针对不同的测试用例修改类名及日志标识
        '''
        contract = ContractManage(self.driver)
        contract.send_contract()
        contract.send_contract_maintain()
        contract.switch_to_window()
        contract.switch_to_frame()
        time.sleep(3)
        contract.send_unfold()
        name = contract.get_contract_template2()[0:14]
        contract.input_query_template(name)
        contract.send_query_btn()
        self.assertIn(name, contract.get_contract_template(), "通过合同模板名称查询合同模板失败！")
        try:
            assert name in contract.get_contract_template()
            logger.info("通过合同模板名称查询合同模板成功。")
        except Exception as e:
            logger.error("通过合同模板名称查询合同模板失败！", e)
            contract.get_windows_img()
        time.sleep(1)
        
if __name__ == '__main__':
    unittest.main()