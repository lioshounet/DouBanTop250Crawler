import os
import time

path = str(time.strftime('%Y-%m-%d_%H-%M-%S', time.localtime()))
os.makedirs("../HTML/DoubanTop250"+path)
print(path)