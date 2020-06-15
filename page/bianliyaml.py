# coding:utf-8
import os

import yaml

# 当前脚本路径
basepath = os.path.dirname(os.path.realpath(__file__))
# yaml文件夹
yamlPagesPath = os.path.join(basepath, "pageelement")

def parseyaml():
    '''
    # 作者：上海-悠悠 QQ交流群：330467341
    遍历读取yaml文件
    '''
    pageElements = {}
    # 遍历读取yaml文件
    for fpath, dirname, fnames in os.walk(yamlPagesPath):
        for name in fnames:
            # yaml文件绝对路径
            yaml_file_path = os.path.join(fpath, name)
            # 排除一些非.yaml的文件
            if ".yaml" in str(yaml_file_path):
                with open(yaml_file_path, 'r', encoding='utf-8') as f:
                    page = yaml.load(f)
                    pageElements.update(page)
    return pageElements

if __name__ == "__main__":
    a = parseyaml()
    print(a)
    for i in a["HomePage"]['locators']:
        print(i)

# -*- coding: utf-8 -*-

from page.pageelement import tools

pages = tools.parseyaml()

# 上海-悠悠 QQ交流群：330467341

def get_locater(clazz_name, method_name):
    locators = pages[clazz_name]['locators']
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


class MyPage:
    我的 = get_locater('MyPage', '我的')
    请点击登录 = get_locater('MyPage', '请点击登录')