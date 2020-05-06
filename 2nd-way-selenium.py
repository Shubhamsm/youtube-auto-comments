 ## usiing chrome and selenium for auto youtubr comment 

import pyautogui
from selenium import webdriver
from selenium.webdriver.common.keys import  Keys
import time ,os

os.chdir(r"/home/shubham/Documents/new/project/Github/youtube-auto-comments/")

driver = webdriver.Chrome(executable_path="./chromedriver")
username=""         # TODO
password=""         # TODO

driver.get("http://www.youtube.com")       # open Youtube
time.sleep(6)
pyautogui.hotkey("ctrl","l")    ; time.sleep(2)
pyautogui.write('https:/www.youtube.com/results?search_query=hello')
pyautogui.press("enter")
time.sleep(5)

element=driver.find_element_by_xpath('//*[@id="video-title"]/yt-formatted-string')
element.click()


# driver.quit()

