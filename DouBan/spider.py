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
    # MuTabPathTxt = open("MuTabPath.txt", "w", encoding="utf-8")
    # MuTabPathTxt.write(Dir_choose)

    datalist = getData(baseurl)

# 控制爬取/筛选数据
def getData(baseurl):
    datalist = []
    for i in range(0, 1):
    # for i in range(0, 10):
        html = askURL(baseurl + str(i * 25))
        # datalist.append(html)
        soup = BeautifulSoup(html,"html.parser")
        # 剥离电影div
        for movie_info in soup.find_all('div',class_="item"):
            # print(movie_info)

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

            for o in  datalist:
                print(o)
                print("\n")

            # print(datalist[1])
            break

    return datalist

# 爬取独立函数
def askURL(url):
    #用户代理
    head = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.81 Safari/537.36"
    }

    request = urllib.request.Request(url,headers=head)

    try:
        response = urllib.request.urlopen(request)
        html = response.read().decode('utf-8')
        # print(html)
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