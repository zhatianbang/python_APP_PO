import yaml
import os

"""获取指定页面的指定元素"""
def read_page_loctor(ymname="pg_mypage.yaml", pagename="MyPage", locname="我的"):
    """
    获取指定页面的指定元素
    :param ymname: yaml文件名字
    :param pagename: yaml文件内容中的第一个名字
    :param locname: yaml文件内容中的元素的name
    :return:
    """

    curPath = os.path.dirname(os.path.realpath(__file__))
    ymPath = os.path.join(curPath, ymname)

    f = open(ymPath, "r", encoding='utf-8')
    cfg = f.read()
    f.close()

    a = yaml.load(cfg,Loader=yaml.Loader)
    # print(a)

    # 输出yaml文件的元素定位
    for i in a[pagename]["locators"]:
        if i["name"] == locname:
            return i

if __name__ == '__main__':
    loc= read_page_loctor(locname="我的_出行服务")
    print(loc)