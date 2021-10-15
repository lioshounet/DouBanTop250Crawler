#import bs4 数据获取
from bs4 import BeautifulSoup

import re #正则

import urllib
import urllib.request
import urllib.parse
# 自定义url

import sqlite3 #进行sqlite数据库操作


def main():
    # print("hello")
    baseurl = "https://movie.douban.com/top250?start=0&filter="
    savepath = r"D:\ZPan\QianDuan\自助学习\2021大三上自学\爬虫-任务驱动\豆瓣class01.xlsx"

    # Top250Tab = load_workbook(savepath)
    # Top250sheet = Top250Tab.active
    # Top250Data = tuple(Top250sheet)

    for i in  range (0,10):
        askURL("https://movie.douban.com/top250?start=" + str(i*25))
        

# 爬取网页
def getData(baseurl):
    datalist = []
    return datalist

def askURL(url):
    #用户代理
    head = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.81 Safari/537.36"
    }

    request = urllib.request.Request(url,headers=head)

    try:
        response = urllib.request.urlopen(request)
        html = response.read().decode('utf-8')
        print(html)
    except urllib.error.URLError as e:
        if hasattr(e,"code"):
            print(e.code)
        if hasattr(e,"code"):
            print(e.reason)

    return html


# 保存数据
def saveData(savepath):
    print("123")

if __name__ == "__main__":
    #控制运行流程
    main()