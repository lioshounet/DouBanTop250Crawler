#import bs4 数据获取
from bs4 import BeautifulSoup

import re #正则

import urllib
# 自定义url

import sqlite3 #进行sqlite数据库操作




def main():
    # print("hello")
    baseurl = "https://movie.douban.com/top250?start=0&filter="
    savepath = r"D:\ZPan\QianDuan\自助学习\2021大三上自学\爬虫-任务驱动\豆瓣class01.xlsx"
    Top250Tab = load_workbook(savepath)
    Top250sheet = Top250Tab.active
    Top250Data = tuple(Top250sheet)

# 爬取网页
def getData(baseurl):
    datalist = []
    return datalist

# 保存数据
def saveData(savepath):
    print("123")

if __name__ == "__main__":
    #控制运行流程
    main()