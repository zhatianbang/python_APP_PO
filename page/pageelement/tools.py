# coding:utf-8
import yaml
import os
import jinja2

"""读取所有yaml文件的元素"""

# 当前脚本路径
basepath = os.path.dirname(os.path.realpath(__file__))
print(basepath)

def parseyaml(yamlPagesPath=basepath):
    """
    读取所有yaml文件的元素
    :param yamlPagesPath: yaml文件所在路径
    :return: 所有yaml文件元素组成的list如：
    {"MyPage": ["我的-出行服务", "我的-邀请好友"],
    "DingDan": ["订单-火车票", "订单-机票"],
    }
    """
    pageElements = {}  # 定义字典存储所有页面元素
    # 遍历读取yaml文件
    for fpath, dirname, fnames in os.walk(yamlPagesPath):
        for name in fnames: # 文件名称是个list，[mypage.yaml,pages.py]
            # yaml文件绝对路径
            yaml_file_path = os.path.join(fpath, name)
            # 排除一些非.yaml的文件
            if ".yaml" in str(yaml_file_path):
                with open(yaml_file_path, 'r', encoding='utf-8') as f:
                    page = yaml.load(f,Loader=yaml.Loader) # 字符串转为字典
                    pageElements.update(page)
    return pageElements

def get_page_list(yamlpage):
    """
    :param yamlpage: 所有yaml文件元素组成的list如：
    {"MyPage": ["我的-出行服务", "我的-邀请好友"],
    "DingDan": ["订单-火车票", "订单-机票"],
    }
    :return: 字典如，{'页面名称1': ['元素name1', '元素name2'], '页面名称2': ['元素name1', '元素name2']}
    """
    page_object = {}
    for page, names in yamlpage.items():
        loc_names = []
        # 获取loctors定位方法
        locs = names['locators']
        # 添加定位name到列表
        for loc in locs:
            loc_names.append(loc['name'])
        page_object[page] = loc_names
    return page_object

def creat_pages_py(page_list):
    '''
    用jinja2把tempetpage模板生成pages.py
    :param pagelist:get_page_list返回内容
    {"MyPage": ["我的-出行服务", "我的-邀请好友"],
    "DingDan": ["订单-火车票", "订单-机票"],
    }
    :return:
    '''
    # print(os.path.join(basepath, "templetpage"))
    template_loader = jinja2.FileSystemLoader(searchpath=basepath)
    template_env = jinja2.Environment(loader=template_loader)

    templateVars ={
                    'page_list': page_list
                    }
    template = template_env.get_template("templetpage")
    with open(os.path.join(basepath, "pages.py"), "w", encoding="utf-8") as f:
        f.write(template.render(templateVars))

if __name__ == "__main__":
    # 1、获取所有的yaml元素
    a = parseyaml()

    # 2、读取每一个yaml文件元素定位的名称作为一个list，放到字典中。{'页面名称1': ['元素name1', '元素name2'], '页面名称2': ['元素name1', '元素name2']}
    pagelists = get_page_list(a)

    # 3、创建页面元素模板，如果有新的就写入，有修改的就覆盖
    creat_pages_py(pagelists)
