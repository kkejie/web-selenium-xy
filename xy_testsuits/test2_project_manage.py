# coding=utf-8

import time
import unittest
from framework.logger import Logger
from framework.browser_engine import BrowserEngine
from xy_pageobjects.login import Login
from xy_pageobjects.logout import Logout
from xy_pageobjects.projectManage import ProjectManage

logger = Logger(logger = "Project").getlog()

class Project(unittest.TestCase):

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

    def test1_query_project(self):
        '''
        * 测试用例在这里编写
        * 针对不同的测试用例修改类名及日志标识
        '''
        project = ProjectManage(self.driver)
        project.send_project()
        project.send_config()
        project.switch_to_window()
        time.sleep(1)
        project.switch_to_frame()
        time.sleep(3)
        project.send_unfold()
        name = project.get_template_name2()
        project.input_template_name(name)
        project.send_query_btn()
        self.assertEqual(name, project.get_template_name(), "通过模板名称查询项目结构模板配置失败！")
        try:
            assert name in project.get_template_name()
            logger.info("通过模板名称查询项目结构模板配置成功。")
        except Exception as e:
            logger.error("通过模板名称查询项目结构模板配置失败！", e)
            project.get_windows_img()
        time.sleep(1)
        
if __name__ == '__main__':
    unittest.main()