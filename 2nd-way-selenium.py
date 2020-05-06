 ## usiing chrome and selenium for auto youtubr comment 

import pyautogui
from selenium import webdriver
from selenium.webdriver.common.keys import  Keys
import time ,os

os.chdir(r"/home/shubham/Documents/new/project/youtube_auto_comments/youtube-auto-comments/using selenium #2/")

driver = webdriver.Chrome(executable_path="./chromedriver")
username=""         # TODO
password=""         # TODO

driver.get("http://www.youtube.com")       # open Youtube
time.sleep(6)
pyautogui.hotkey("ctrl","l")
pyautogui.write('https:/www.youtube.com/results?search_query=hello')
pyautogui.press("enter")


# driver.quit()

