from appium import webdriver
from common.base import BaseApp


# 所有的Page页面都集成基类  BaseApp
class MyPage(BaseApp):
    '''订单-全部订单'''
    loc1 = {"name": "火车票", "by": "text", "value": "火车票" }
    loc2 = {"name": "机票", "by": "text", "value": "机票"}
    loc3 = {"name": "汽车票", "by": "text", "value": "汽车票"}
    loc4 = {"name": "酒店", "by": "text", "value": "酒店"}
    loc5 = {"name": "专车订单", "by": "text", "value": "专车订单"}
    loc6 = {"name": "船票订单", "by": "text", "value": "船票订单"}
    loc7 = {"name": "门票订单", "by": "text", "value": "门票订单"}

    def click_huochepiao(self):
        '''订单-火车票'''
        self.click(self.loc1)

    def click_jipiao(self):
        '''订单-机票'''
        self.click(self.loc2)

    def click_qichepiao(self):
        '''订单-汽车票'''
        self.click(self.loc3)

    def click_jiudian(self):
        '''订单-酒店'''
        self.click(self.loc4)



