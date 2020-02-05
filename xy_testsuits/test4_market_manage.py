# coding=utf-8

import time
import unittest
from framework.logger import Logger
from framework.browser_engine import BrowserEngine
from xy_pageobjects.login import Login
from xy_pageobjects.logout import Logout
from xy_pageobjects.marketManage import MarketManage

logger = Logger(logger = "Market").getlog()

class Market(unittest.TestCase):

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

    def test1_query_market(self):
        '''
        * 测试用例在这里编写
        * 针对不同的测试用例修改类名及日志标识
        '''
        market = MarketManage(self.driver)
        market.send_market()
        market.send_market_order()
        market.switch_to_window()
        market.switch_to_frame()
        # time.sleep(3)
        market.send_unfold()
        name = market.get_order_num2()
        market.input_order_num(name)
        market.send_query_btn()
        self.assertEqual(name, market.get_order_num(), "通过销售订单号查询销售订单失败！")
        try:
            assert name in market.get_order_num()
            logger.info("通过销售订单号查询销售订单成功。")
        except Exception as e:
            logger.error("通过销售订单号查询销售订单失败！", e)
            market.get_windows_img()
        time.sleep(3)
        
if __name__ == '__main__':
    unittest.main()