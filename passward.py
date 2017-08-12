from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import re
from selenium.webdriver.remote.command import Command
from selenium.webdriver.common.action_chains import ActionChains
def passward(driver):
    ActionChains(driver).move_by_offset(xoffset=650,yoffset=350).perform()
    ActionChains(driver).click().perform()
