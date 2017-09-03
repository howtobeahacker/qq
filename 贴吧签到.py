from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
import time

nanjingcaijing="http://tieba.baidu.com/f?kw=%E5%8D%97%E4%BA%AC%E8%B4%A2%E7%BB%8F%E5%A4%A7%E5%AD%A6&fr=home"
huaban="https://tieba.baidu.com/f?kw=%E6%BB%91%E6%9D%BF&fr=home"
liningkong="https://tieba.baidu.com/f?kw=%E6%9D%8E%E5%AE%81%E6%8E%A7&fr=home"
zhenchuan="http://tieba.baidu.com/f?kw=%E9%9C%87%E5%B7%9D%E9%AB%98%E7%BA%A7%E4%B8%AD%E5%AD%A6&fr=index&red_tag=d2520360580"
url=[]
url.append(nanjingcaijing)
url.append(huaban)
url.append(liningkong)
url.append(zhenchuan)
while(True):
    driver = webdriver.Firefox()
    driver.get("https://tieba.baidu.com/index.html")
    driver.find_element_by_class_name("u_login").click()
    time.sleep(1)
    driver.find_element_by_id("TANGRAM__PSP_10__userName").send_keys("17327764197")
    driver.find_element_by_id("TANGRAM__PSP_10__password").send_keys("sz869993410")
    driver.find_element_by_id("TANGRAM__PSP_10__submit").click()
    time.sleep(3)
    for i in url:
        driver.get(i)
        ActionChains(driver).move_by_offset(xoffset=980,yoffset=369).perform()
        ActionChains(driver).double_click().perform()
        ActionChains(driver).move_by_offset(xoffset=-980, yoffset=-369).perform()
    driver.close()
    time.sleep(23*3600)
