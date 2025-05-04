# 导入 requests 库，用于发送 HTTP 请求
import requests
# 从 bs4 库中导入 BeautifulSoup 类，用于解析 HTML 文档
from bs4 import BeautifulSoup
# 导入 bs4 库，用于后续的元素类型判断
import bs4

# 定义一个函数，用于获取指定 URL 的 HTML 文本内容


def getHtmlText(url):
    try:
        # 发送 GET 请求，设置超时时间为 30 秒
        r = requests.get(url, timeout=30)
        # 检查请求状态码，如果不是 200 则抛出 HTTPError 异常
        r.raise_for_status()  # 如果状态不是200，引发HTTPError异常
        # 将响应内容的编码设置为根据内容推测的编码
        r.encoding = r.apparent_encoding
        # 打印获取到的 HTML 文本内容
        print(r.text)
        # 返回获取到的 HTML 文本内容
        return r.text
    except:
        # 若发生异常，返回空字符串
        return ""

# 定义一个函数，用于从 HTML 文本中提取大学信息并填充到列表中


def fillunivlist(ulist, html):
    # 使用 BeautifulSoup 解析 HTML 文本
    soup = BeautifulSoup(html, "html.parser")
    # 遍历 HTML 文档中 tbody 标签下的所有子元素
    for tr in soup.find('tbody').children:
        # 判断子元素是否为标签类型
        if isinstance(tr, bs4.element.Tag):
            # 获取当前 tr 标签下的所有 td 标签
            tds = tr('td')
            # 将排名、学校名称和总分信息添加到列表中
            ulist.append([tds[0].string, tds[1].string, tds[3].string])

# 定义一个函数，用于打印大学信息列表


def printunivlist(ulist, num):
    tplt = "{0:^10}\t{1:{3}^10}\t{2:^10}"
    # 打印表头
    print(tplt.format("排名", "学校名称", "总分", chr(12288)))
    # 遍历前 num 个大学信息
    for i in range(num):
        # 获取当前大学信息
        u = ulist[i]
        # 打印当前大学的排名、学校名称和总分信息
        print(tplt.format(u[0], u[1], u[3], chr(12288)))

# 定义主函数，程序的入口点


def main():
    # 初始化一个空列表，用于存储大学信息
    uinfo = []
    # 定义要爬取的 URL
    url = 'https://www.shanghairanking.cn/rankings/bcur/202511'
    # 调用 getHtmlText 函数获取 HTML 文本内容
    html = getHtmlText(url)
    # 调用 fillunivlist 函数填充大学信息到列表中
    fillunivlist(uinfo, html)
    # 调用 printunivlist 函数打印前 20 个大学信息
    printunivlist(uinfo, 20)  # 20 univs


# 判断当前脚本是否作为主程序运行
if __name__ == '__main__':
    # 调用主函数
    main()
