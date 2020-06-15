import unittest
from  appium import webdriver
import time
from common.base import BaseApp
from page.pageelement.pages import MyPage, YaoQing


"""主要测试用例中调用 页面元素模板pages.py"""
desired_caps = {
                "platformName": "Android",
                "deviceName": "127.0.0.1:21503",
                "platformVersion": "7.1.2",
                "appPackage": "com.yipiao",
                "noReset": True,
                "appActivity": "com.zt.main.entrance.MainActivity"

                }
class TestYaoQing(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)
        time.sleep(10)
        cls.app = BaseApp(cls.driver)



    def test_01(self):
        '''我的-邀请好友'''
        time.sleep(10)
        self.app.click(MyPage.我的)  # 点我的
