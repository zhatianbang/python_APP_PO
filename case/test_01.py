import unittest
from  appium import webdriver
import time
from common.base import BaseApp
desired_caps = {
                "platformName": "Android",
                "deviceName": "emulator-5554",
                "platformVersion": "5.1.1",
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
        cls.app.click({"name": "我的", "by": "text", "value": "我的"})


    def test_01(self):
        '''我的-邀请好友'''
        # self.app.click({"name": "我的", "by": "text", "value": "我的"})
        time.sleep(3)
        self.app.click({"name": "我的-邀请好友", "by": "text", "value": "一起来抢票"})
        # 获取弹出框文本，用做断言
        els = self.app.finds({"by": "id", "value": "com.yipiao:id/socialize_text_view"})
        result = []
        for i in els:
            t = i.text
            result.append(t)
        print("获取结果：%s" % result)

        # 点取消分享
        self.app.click({"name": "取消分享", "by": "text", "value": "取消分享"})

        qiwang = ['微信', '朋友圈', 'QQ', 'QQ空间', '短信']
        self.assertEqual(result, qiwang)

    def test_02(self):
        '''消息中心-火车票订单查询'''
        time.sleep(3)
        self.app.click({"name": "消息中心", "by": "text", "value": "消息中心"})

        # 火车票订单查询
        self.app.click({"name": "火车票订单咨询", "by": "text", "value": "火车票订单咨询"})

        # 判断 预订指南在webview里 //android.view.View[@content-desc="1.预订指南"]
        t = self.app.is_element_exist({"by": "xpath", "value": '//android.view.View[@content-desc="1.预订指南"]'})
        print("获取结果：%s" % t)

        self.app.click({"name": "返回", "by": "desc", "value": "返回"})
        self.app.click({"name": "back", "by": "id", "value": "com.yipiao:id/flayBackLayout"})
        self.assertTrue(t)

    def test_03(self):
        '''消息中心-在线客服'''
        time.sleep(3)
        self.app.click({"name": "消息中心", "by": "text", "value": "消息中心"})
        # 在线客服
        self.app.click({"name": "在线客服", "by": "text", "value": "在线客服"})

        print(self.driver.page_source)

        # 判断元素
        t = self.app.is_element_exist({"by": "desc", "value": '您好，请选择您要咨询的产品，小二会尽快为您解答。'})
        print("获取结果：%s" % t)

        self.app.click({"name": "返回", "by": "desc", "value": "返回"})
        self.app.click({"name": "back", "by": "id", "value": "com.yipiao:id/flayBackLayout"})
        self.assertTrue(t)


    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

if __name__ == "__main__":
    unittest.main()