import pyautogui
import time
from bs4 import BeautifulSoup
import requests
# from django.utils.encoding import smart_str, smart_unicode

time.sleep(5)
pyautogui.hotkey('ctrl','f')
time.sleep(5)
pyautogui.write("comments")
pyautogui.press('enter')



# # # print(soup.prettify())