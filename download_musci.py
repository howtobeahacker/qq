from selenium import webdriver
import re
f=open("url.txt","r")
driver = webdriver.Firefox()
for url in f:
    url=url.split("/")[-2]
    url="http://www.bilibilijj.com/video/"+str(url)+"/"
    driver.get(url)
    driver.refresh()
    print(url)
    url=re.findall('''<a href="/Files/DownLoad/([0-9]*).mp3" target="_blank" title="MP3下载''',driver.page_source)

    for i in url:
        try:
            driver.get("http://www.jijidown.com/Files/DownLoad/"+i+".mp3")
            # driver.refresh()
            driver.find_element_by_class_name("putong").click()
        except Exception:
            pass
    # down_load
    # driver.get
# '''http://www.jijidown.com/Files/DownLoad/20082010.mp3'''
# driver = webdriver.Firefox()
# driver.get("http://www.bilibilijj.com/video/av9942036/")
# driver.refresh()
# url=re.findall('''<a href="/Files/DownLoad/([0-9]*).mp3" target="_blank" title="MP3下载''',driver.page_source)
# for i in url:
#     driver.get("http://www.jijidown.com/Files/DownLoad/"+i+".mp3")
#     driver.refresh()
#     driver.find_element_by_class_name("putong").click()
# down_load
