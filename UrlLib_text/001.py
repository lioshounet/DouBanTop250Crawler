import urllib.request

# get--------------------
# response = urllib.request.urlopen("http://www.baidu.com/")
# print(response.read().decode('utf-8'))

# post--------------------
# 测试网站 http://httpbin.org/
import urllib.parse

# try:
#     data = bytes(urllib.parse.urlencode({"hello":"world"}),encoding="utf-8")
#     response = urllib.request.urlopen("http://douban.com",timeout=5)
#     print(response.read().decode('utf-8'))
#     print(response.status)
# except urllib.error.URLError as e:
#     print("time out")

# data = bytes(urllib.parse.urlencode({"hello": "world"}), encoding="utf-8")
# response = urllib.request.urlopen("http://douban.com", timeout=5)
# print(response.read().decode('utf-8'))
# print(response.status)



# url = "https://www.douban.com"
# headers = {
#     "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.81 Safari/537.36"
# }
# data = bytes(urllib.parse.urlencode({"name": "eric"}), encoding="utf-8")
# req = urllib.request.Request(url=url,data=data,headers=headers,method="POST")
# response = urllib.request.urlopen(req)
# print(response.read().decode('utf-8'))
