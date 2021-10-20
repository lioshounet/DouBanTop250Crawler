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

def saveinDB(arr2,path):
    arr3 = []
    connection = pymysql.connect(host="192.168.75.143",
                                 port=3306,
                                 user="root",
                                 password="ly86036609",
                                 db='DouBanTop250',
                                 charset="utf8",
                                 )

    arrs = ["1","2","3","4","5","6","7"]

    # for arr in arr2:
    #     arr3.append(arr.replace("'", " "))

    cursor = connection.cursor()

    sql = r"CREATE TABLE " + \
          path + \
          "(`link`  varchar(255) NULL ," + \
          "`imglink`  varchar(255) NULL ," + \
          "`point`  varchar(255) NULL ," + \
          "`pointer`  varchar(255) NULL ," + \
          "`info`  varchar(255) NULL ," + \
          "`CnName`  varchar(255) NULL ," + \
          "`OutName`  varchar(255) NULL" + \
          ");"
    print(sql)

    cursor.execute(sql)
    connection.commit()

    # try:

    for i in range(0,1):
        sql = r"INSERT INTO " + path +\
              r"(link,imglink,point,pointer,info,CnName,OutName) VALUES('"+\
              str(arrs[i * 7 + 0]) + "','" + \
              str(arrs[i * 7 + 1]) + "','" + \
              str(arrs[i * 7 + 2]) + "','" + \
              str(arrs[i * 7 + 3]) + "','" + \
              str(arrs[i * 7 + 4]) + "','" + \
              str(arrs[i * 7 + 5]) + "','" + \
              str(arrs[i * 7 + 6]) + "'" +");"
        print(sql)
    # sql = "CREATE TABLE t1(id int not null,name char(20));"
        cursor.execute(sql)
        connection.commit()

    cursor.close()
    connection.close()

# saveinDB([1],"DoubanTop250_2021_10_19___21_37_49")

try:
    print(zzzz)
    print(";;;;")
except:
    print("pass")