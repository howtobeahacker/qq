from selenium import webdriver
url="https://tieba.baidu.com/index.html"
driver=webdriver.Firefox()
driver.get(url)
driver.find_element_by_class_name("u_login").click()
driver.find_element_by_class_name("pass-text-input pass-text-input-password").send_keys("1548314601@qq.com")
driver.find_element_by_class_name("TANGRAM__PSP_10__password").send_keys("sz869993410")
driver.find_element_by_id("TANGRAM__PSP_10__submit").click()
# driver.find_element_by_id()
# driver.find_element_by_id()
