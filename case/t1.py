import unittest
from  appium import webdriver
import time
from common.keyevent import key

desired_caps = {
                "platformName": "Android",
                "deviceName": "emulator-5554",  # 作用不大，有bug
                "platformVersion": "5.1.1",
                "appPackage": "com.yipiao",
                "udid": "emulator-5554",  # 指定设备匹配appium
                "noReset": True,  # app的缓存不重置
                "appActivity": "com.yipiao.activity.LaunchActivity"
                }

# localhost
driver = webdriver.Remote('http://192.168.1.100:4724/wd/hub', desired_caps)




# 使用方法参考
driver.start_activity("com.yipiao", "activity名称")