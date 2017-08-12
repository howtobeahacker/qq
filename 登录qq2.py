from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import re
driver = webdriver.Firefox()
# driver.find_element_by_class_name()
driver.get("http://w.qq.com/")
a=input("请扫描二维码")
while(True):
    a=input("请输入:")
    if(a=="搜索群"):
        b=input("搜索：")
        driver.find_element_by_id("panelRightButton-2").click()
        driver.find_element_by_id("searchInput").send_keys(b)
        id = re.findall('"search-item-group-(.*?)"', driver.page_source)
        driver.find_element_by_id("search-item-group-"+(id[0])).click()
    if (a == "搜索好友"):
        b = input("搜索：")
        driver.find_element_by_id("panelRightButton-2").click()
        driver.find_element_by_id("searchInput").send_keys(b)
        id = re.findall('"search-item-friend-(.*?)"', driver.page_source)
        driver.find_element_by_id("search-item-friend-" + (id[0])).click()

    if(a=="填写搜索栏："):
        b=input("搜索：")
        driver.find_element_by_id("searchInput").send_keys(b)
    if(a=="联系人"):
        driver.find_element_by_id("contact").click()
    if(a=="返回"):
        driver.find_element_by_id("panelRightButton-6").click()  # 关闭当前聊天页面，
    if(a=="清楚搜索栏"):
        driver.find_element_by_id("searchClear").click()  # 清楚搜索栏
    if(a=="发消息"):
        b=input("输入消息:")
        driver.find_element_by_id("chat_textarea").send_keys(b)
        driver.find_element_by_id("send_chat_btn").click()
    if(a=="发消息重复"):
        b=input("输入消息:")
        c=input("输入几次:")
        for i in range(int(c)):
            driver.find_element_by_id("chat_textarea").send_keys(b)
            driver.find_element_by_id("send_chat_btn").click()
            time.sleep(0.2)
    if(a=="存活确认"):
        b=input("输入对方：")
        if(b[:2]=="好友"):
            driver.find_element_by_id("contact").click()
            driver.find_element_by_id("panelRightButton-2").click()
            driver.find_element_by_id("searchInput").send_keys(b[2:])
            id = re.findall('"search-item-friend-(.*?)"', driver.page_source)
            driver.find_element_by_id("search-item-friend-" + (id[0])).click()
            time_night = ["23:00", "00:00", "01:00", "02:00", "03:00", "04:00", "05:00", "06:00"]
            while (True):
                if (time.asctime()[11:16] in time_night):
                    driver.find_element_by_id("chat_textarea").send_keys("存活确认")
                    driver.find_element_by_id("send_chat_btn").click()
                    time.sleep(1800)

        else:
            driver.find_element_by_id("contact").click()
            driver.find_element_by_id("panelRightButton-2").click()
            driver.find_element_by_id("searchInput").send_keys(b)
            id = re.findall('"search-item-group-(.*?)"', driver.page_source)
            driver.find_element_by_id("search-item-group-" + (id[0])).click()
            time_night = ["23:00", "00:00", "01:00", "02:00", "03:00", "04:00", "05:00", "06:00"]
            while (True):
                if (time.asctime()[11:16] in time_night):
                    driver.find_element_by_id("chat_textarea").send_keys("study make me happy")
                    driver.find_element_by_id("send_chat_btn").click()
                    time.sleep(1800)








                # driver.find_element_by_id("search-item-friend-2941087381").click()
# for i in range(100):
#     driver.find_element_by_id("chat_textarea").send_keys("你好帅，么么哒")
#     driver.find_element_by_id("send_chat_btn").click()
# driver.get("https://user.qzone.qq.com/625025493?ptlang=2052&source=aiostar")
# a=input("点击头像")
# print(driver.page_source)
# driver.find_element_by_class_name("face").click()
# webdriver.ActionChains(driver).move_to_element()
# print(driver.get_cookies())
# data=driver.page_source
# print(data)
# driver.get("https://user.qzone.qq.com/625025493/311")

    #
# driver.find_element_by_id("recent-item-group-4096120496").click()
# for i in range(1000):
#     driver.find_element_by_id("chat_textarea").send_keys("张宗远好帅")
#     driver.find_element_by_id("send_chat_btn").click()