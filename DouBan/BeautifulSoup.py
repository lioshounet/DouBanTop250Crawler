from bs4 import BeautifulSoup
import re
file = open("../HTML/百度.html","rb")
html = file.read().decode("utf-8")
bs = BeautifulSoup(html,"html.parser")

#查找所有的a---字符串完全一样
# t_list = bs.find_all("a")
# print(t_list)

# 包含子标签
# 有a就行
# t_list = bs.find_all(re.compile("a"))
# print(t_list)

#参数---id---class
# t_list = bs.find_all(id="head")
# for item in t_list:
#     print(item)


#参数 ----text
# t_list = bs.find_all(text=["hao123","地图","贴吧"])
# for item in t_list:
#     print(item)

#使用正则
# t_list = bs.find_all(text=re.compile("\d"))
# for item in t_list:
#     print(item)

#限制个数
# t_list = bs.find_all("a",limit=3)
# for item in t_list:
#     print(item)

# css选择器 包括id class 等标签可携带的属性
# t_list = bs.select("title")
# t_list = bs.select(".mnav")
# t_list = bs.select("#ul")
# t_list = bs.select("a[class='text-color']")
# # 子节点
# t_list = bs.select("head > meta")
# 兄弟节点
# t_list = bs.select(".mnav ~ .bri")
# for item in t_list:
#     print(item)

# 正则
pat = re.compile("AA")
# 创建模式对象
m = pat.search("AABCAADCCAAA")
print(m)

m = re.search("AA","AABCAADCCAAA")
print(m)

m = re.search("[A-Z]+","AABCAADCCAAA")
print(m)

# a换A
m = re.sub("a","A","abcdfghj")
print(m)