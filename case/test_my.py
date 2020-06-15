import unittest
from  appium import webdriver
import time
from common.base import BaseApp
from page.mypage import MyPage,YaoQingHaoYou


desired_caps = {
                "platformName": "Android",
                "deviceName": "127.0.0.1:21503",
                "platformVersion": "7.1.2",
                "appPackage": "com.yipiao",
                "noReset": True,
                "appActivity": "com.yipiao.activity.LaunchActivity"
                }
class TestYaoQing(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)
        time.sleep(10)
        cls.app = BaseApp(cls.driver)
        # cls.app.click(MyPage.loc1)  # 点我的


    def test_01(self):
        '''我的-邀请好友'''
        self.app.click({"name": "我的", "by": "text", "value": "我的"})
        time.sleep(3)
        self.app.click(MyPage.loc3)
        # 获取弹出框文本，用做断言
        els = self.app.finds(YaoQingHaoYou.tanchu)
        result = []
        for i in els:
            t = i.text
            result.append(t)
        print("获取结果：%s" % result)

        # 点取消分享
        self.app.click(YaoQingHaoYou.quxiao)

        qiwang = ['微信', '朋友圈', 'QQ', 'QQ空间', '短信']
        self.assertEqual(result, qiwang)
