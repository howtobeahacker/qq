import re
import time
from selenium import webdriver
url="https://www.bilibili.com/video/music-coordinate-1.html#!page=1&tagid=14426&tag=%E7%94%B5%E9%9F%B3&days=30&order=hot"
for i in range(1,100):
    driver = webdriver.Firefox()
    driver.get("https://www.bilibili.com/video/music-coordinate-1.html#!page="+str(i)+"&tagid=14426&tag=%E7%94%B5%E9%9F%B3&days=30&order=hot")
    html=driver.page_source
    url=re.findall('''<a href="//www.bilibili.com/video/av([0-9]*?)" target="_blank" class="title" title="【耳机福利】''',html)
    for i in url:
        print("http://www.bilibili.com/video/av" + str(i) + "/")
    driver.close()
    # music=re.findall('''<a href="//www.bilibili.com/video/(.*?)" target="_blank" class="title" title="[【]耳机福利[】]''',driver.page_source)
# lis=[]
# for i in music:
#     a=(re.findall("[0-9]{8}",i[:-11]))
#     for i in a:
#         i=int(i)
#         lis.append(i)
#
# for i in list(set(lis)):
#     print("http://www.bilibili.com/video/av"+str(i)+"/")