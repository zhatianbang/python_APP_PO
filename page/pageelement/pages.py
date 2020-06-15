# -*- coding: utf-8 -*-

from page.pageelement import tools

#模板页面，不要删除

pages = tools.parseyaml()


def get_locater(clazz_name, method_name):
    locators = pages[clazz_name]['locators']
    for locator in locators:
        if locator['name'] == method_name:
            return locator


class DingDan:
    订单 = get_locater('DingDan', '订单')
    订单_火车票 = get_locater('DingDan', '订单_火车票')
    订单_机票 = get_locater('DingDan', '订单_机票')
    订单_汽车票 = get_locater('DingDan', '订单_汽车票')
    订单_酒店 = get_locater('DingDan', '订单_酒店')

    
class MyPage:
    我的 = get_locater('MyPage', '我的')
    我的_出行服务 = get_locater('MyPage', '我的_出行服务')
    我的_邀请好友 = get_locater('MyPage', '我的_邀请好友')
    我的_消息中心 = get_locater('MyPage', '我的_消息中心')
    我的_产品意见 = get_locater('MyPage', '我的_产品意见')
    我的_微信通知 = get_locater('MyPage', '我的_微信通知')
    我的_更多 = get_locater('MyPage', '我的_更多')
    我的_加速包 = get_locater('MyPage', '我的_加速包')

    
class YaoQing:
    弹出 = get_locater('YaoQing', '弹出')
    取消分享 = get_locater('YaoQing', '取消分享')

if __name__ == '__main__':
    print(MyPage.我的)
    print(DingDan.订单)
    print(YaoQing.取消分享)