from appium import webdriver
from common.base import BaseApp

# 读取yaml元素定位
import os
import yaml
path = os.path.dirname(os.path.realpath(__file__))
elepath = os.path.join(path, "pageelement", "mypage.yaml")

f = open(elepath, "r", encoding="utf-8")
ele = f.read()

page = yaml.load(ele,Loader=yaml.Loader)
all = page['MyPage']['locator']
for i in all:
    print(i)

def get_locater(clazz_name, method_name):
    locators = page[clazz_name]['locators']
    for locator in locators:
        if locator['name'] == method_name:
            return locator


class HomePage:
    城市选择 = get_locater('HomePage', '城市选择')
    首页搜索 = get_locater('HomePage', '首页搜索')


class LoginPage:
    微信登录 = get_locater('LoginPage', '微信登录')
    手机号登录 = get_locater('LoginPage', '手机号登录')
    其它登录 = get_locater('LoginPage', '其它登录')
    QQ = get_locater('LoginPage', 'QQ')
    微博 = get_locater('LoginPage', '微博')
    账号密码 = get_locater('LoginPage', '账号密码')
    输入账号 = get_locater('LoginPage', '输入账号')
    输入密码 = get_locater('LoginPage', '输入密码')
    登录按钮 = get_locater('LoginPage', '登录按钮')


# 所有的Page页面都集成基类  BaseApp
class MyPage(BaseApp):
    '''我的-菜单页面'''
    loc1 = {"name": "我的", "by": "text", "value": "我的" }
    loc2 = {"name": "我的-出行服务", "by": "text", "value": "出行服务"}
    loc3 = {"name": "我的-邀请好友", "by": "text", "value": "一起来抢票"}
    loc4 = {"name": "我的-消息中心", "by": "text", "value": "消息中心"}
    loc5 = {"name": "我的-产品意见", "by": "text", "value": "产品意见"}
    loc6 = {"name": "我的-微信通知", "by": "text", "value": "微信通知"}
    loc7 = {"name": "我的-微信通知", "by": "text", "value": "更多"}
    loc8 = {"name": "我的-加速包", "by": "text", "value": "加速包"}
    loc9 = {"name": "我的-优惠券", "by": "text", "value": "优惠券"}
    loc10 = {"name": "我的-抢票券", "by": "text", "value": "抢票券"}
    loc11 = {"name": "我的-中间banner", "by": "id", "value": "com.yipiao:id/vip_recommend_image"}
    def click_my(self):
        '''点tab-我的'''
        self.click(self.loc1)

    def click_jiasubao(self):
        '''点加速包'''
        self.click(self.loc8)

    def click_chuxingfuwu(self):
        '''出行服务'''
        self.click(self.loc2)

    def click_yaoqinghaoyou(self):
        self.click(self.loc3)

    def click_chanpinyijian(self):
        '''产品意见'''
        self.click(self.loc5)



class YaoQingHaoYou(BaseApp):
    """页面元素抓取"""

    tanchu = {"by":"id", "vavlue":"com.yipiao:id/socialize_text_view"}
    quxiao = {"name":"取消分享","by":"text","value":"取消"}

