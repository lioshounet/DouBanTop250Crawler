#import bs4 数据获取
from bs4 import BeautifulSoup

import re #正则

import urllib
import urllib.request
import urllib.parse
# 自定义url

# import sqlite3
#进行sqlite数据库操作
import numpy #二维数组操作


import os
import time
import openpyxl
from openpyxl import load_workbook

import pymysql.cursors

def main():
    baseurl = "https://movie.douban.com/top250?start="

    # 母excel
    TabSavepath = r"D:\ZPan\QianDuan\自助学习\2021大三上自学\爬虫-任务驱动\豆瓣\保存的表格\class01.xlsx"

    path = str(time.strftime('%Y_%m_%d___%H_%M_%S', time.localtime()))
    datalist = getData(baseurl,path)

    DBTabName = "Top250__" + path

    # 保存的excel的名字，数据库表的名称
    saveData(TabSavepath, datalist , DBTabName)

# 控制爬取/筛选数据
def getData(baseurl ,path):
    Top250data = [[""]]
    datalist = []

    # 根据时间创建文件夹，装html，以txt的格式
    os.makedirs("../HTML/DoubanTop250" + path)

    for i in range(0, 10):
    # for i in range(0, 10):
        html = askURL(baseurl + str(i * 25))

        #html保存
        HtmlTxt = open("../HTML/DoubanTop250"+path+"/"+str(i * 25) + ".txt", "w", encoding="utf-8")
        HtmlTxt.write(html)
        print(str(i * 25)+"HTML写入成功")

        # datalist.append(html)
        soup = BeautifulSoup(html,"html.parser")
        # 剥离电影div
        for movie_info in soup.find_all('div',class_="item"):

            # a连接的正则搜索
            findLink = re.compile(r'<a href="(.*?)">')
            findImg = re.compile(r'<img.*src="(.*?)" ',re.S)
            findTilte = re.compile(r'<span.*class="title">(.*)</span>')
            findPoint = re.compile(r'<span.*class="rating_num" property="v:average">(.*)</span>')
            findPointer = re.compile(r'<span>(.*)</span>')
            findBd = re.compile(r'<p class="">(.*?)</p>',re.S)

            movie_info = str(movie_info)
            # 这个[0]指的是每个信息div出一个
            link = re.findall(findLink,movie_info)[0]
            findImg = re.findall(findImg, movie_info)[0]
            findPoint = re.findall(findPoint, movie_info)[0]
            findPointer = re.findall(findPointer, movie_info)[0]
            findBd = re.findall(findBd, movie_info)[0]
            findBd = re.sub('<br(\s+)?/>(\s+)?'," ",findBd)

            # 搜索信息加入数组
            datalist.append(link)
            datalist.append(findImg)
            datalist.append(findPoint)
            datalist.append(findPointer)
            datalist.append(findBd.strip())
            #.strip()去掉空格
            findTilte = re.findall(findTilte, movie_info)
            if(len(findTilte) == 2):
                CnTitle = findTilte[0]
                datalist.append(CnTitle)
                OuTitle = findTilte[1]
                datalist.append(OuTitle)
            else:
                datalist.append(findTilte[0])
                datalist.append("")

            Top250data = numpy.array(datalist)

    return Top250data

# 爬取独立函数
def askURL(url):
    #用户代理
    head = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.81 Safari/537.36"
    }

    request = urllib.request.Request(url,headers=head)

    try:
        print("执行一次独立爬取,获取原始HTML")
        response = urllib.request.urlopen(request)
        html = response.read().decode('utf-8')
        print("原始HTML获取成功")

    except urllib.error.URLError as e:
        print("原始HTML获取出错")
        if hasattr(e,"code"):
            print(e.code)
        if hasattr(e,"code"):
            print(e.reason)

    return html

# 保存数据
def saveData(savepath,arr2 ,DBTabName):

    try:
        #写入表格
        Top250Tab = load_workbook(savepath)
        Top250sheet = Top250Tab.active
        Top250Data = tuple(Top250sheet)
    except:
        print("打开excel表格出错")

    try:
        for y in range(0,250):
            Top250Data[y][0].value = arr2[y * 7 + 0]
            Top250Data[y][1].value = arr2[y * 7 + 1]
            Top250Data[y][2].value = arr2[y * 7 + 2]
            Top250Data[y][3].value = arr2[y * 7 + 3]
            Top250Data[y][4].value = arr2[y * 7 + 4]
            Top250Data[y][5].value = arr2[y * 7 + 5]
            Top250Data[y][6].value = arr2[y * 7 + 6]

        Top250Tab.save(savepath + "豆瓣Top250.xlsx")
        print("excel已保存")

    except:
        print("写入excel出错")

    saveinDB(arr2,DBTabName)

def saveinDB(arr2,tabname):
    arr3 = []
    try:
        connection = pymysql.connect(host="192.168.75.143",
                                     port=3306,
                                     user="root",
                                     password="ly86036609",
                                     db='DouBanTop250',
                                     charset="utf8",
                                     )

        print("已经成功连接数据库")

    except :
        print("数据库DouBanTop250连接失败")

    # 分号替换
    for arr in arr2:
        arr3.append(arr.replace("'", " "))

    cursor = connection.cursor()

    # 创建表格
    try:
        sql = r"CREATE TABLE "+\
                tabname +\
                "(`link`  varchar(255) NULL ,"+\
                "`imglink`  varchar(255) NULL ,"+\
                "`point`  varchar(255) NULL ,"+\
                "`pointer`  varchar(255) NULL ,"+\
                "`info`  varchar(255) NULL ,"+\
                "`CnName`  varchar(255) NULL ,"+\
                "`OutName`  varchar(255) NULL"+\
                ");"
        cursor.execute(sql)
        connection.commit()

    except :
        print("表格创建失败")

    for i in range(0, 250):
        sql = r"INSERT INTO " + tabname + \
              r"(link,imglink,point,pointer,info,CnName,OutName) VALUES('" + \
              str(arr3[i * 7 + 0]) + "','" + \
              str(arr3[i * 7 + 1]) + "','" + \
              str(arr3[i * 7 + 2]) + "','" + \
              str(arr3[i * 7 + 3]) + "','" + \
              str(arr3[i * 7 + 4]) + "','" + \
              str(arr3[i * 7 + 5]) + "','" + \
              str(arr3[i * 7 + 6]) + "'" + ");"


        try:
            cursor.execute(sql)
            connection.commit()

            print(str(i * 7 + 0) + "-" + str(i * 7 + 6) + "数据插入成功")
        except:
            print(str(i * 7 + 0) + "-" + str(i * 7 + 6) + "数据插入失败")

    #数据库关闭连接
    cursor.close()
    connection.close()

if __name__ == "__main__":
    #控制运行流程
    main()