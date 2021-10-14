import urllib.request

# get--------------------
response = urllib.request.urlopen("http://www.baidu.com/")
print(response.read().decode('utf-8'))

# post------------------
# 测试网站 http://httpbin.org/

