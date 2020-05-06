import pyautogui
import time
from bs4 import BeautifulSoup
import requests




# def inputString:
# time.sleep(10)
# f=str(input("Term"))
# f.replace(" ","+")




msg="hello BakchodGang"          # message to comment


# to get all video links on searching 
urls_list=[]
page = requests.get("https://www.youtube.com/results?search_query=data+science+simplilearn")
soup = BeautifulSoup(page.content,'lxml', from_encoding="latin-1") 


vids = soup.findAll('a',attrs={'class':'yt-uix-tile-link'})
for x in vids:
    y=x['href']
    if y[0]=="/":
        urls_list.append(y.encode('latin-1').decode('utf-8'))



def linkTo(*args):
    count=0
    time.sleep(5)
    pyautogui.hotkey('ctrl', 'l')
    for i in args:
        link="https://www.youtube.com"+i
        time.sleep(5)
        pyautogui.write(link) ; time.sleep(3)
        pyautogui.press('enter')

        time.sleep(8)
        pyautogui.scroll(-100)
        time.sleep(10)

        pyautogui.hotkey('ctrl','f')
        time.sleep(5)
        pyautogui.write("comments")
        time.sleep(10)
        
        pyautogui.click(x=324, y=478)               # find yourself comment box
        pyautogui.write(msg) ; time.sleep(3)
        pyautogui.hotkey('ctrl','enter')
        

        count+=1;
        if count==3:
            break;
        time.sleep(5)


linkTo(*urls_list)