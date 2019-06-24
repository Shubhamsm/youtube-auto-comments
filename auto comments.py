import pyautogui as x
import time

   
def autotype():
        x.moveTo(1013,533)
        time.sleep(1)
        x.click(2)
        time.sleep(2)
        x.press("space")
        time.sleep(2)
        x.scroll(-1400)


        time.sleep(4)
        x.moveTo(169,500)
        x.doubleClick()
        x.typewrite("click -> https://www.youtube.com/watch?v=CJVkvY_F9UY&t=7s")


        if x.locateOnScreen("comment.png")!=None:
            a,b,c,d =(x.locateOnScreen("comment.png"))
            x.moveTo(a+20,b)
            time.sleep(1) 
	

            time.sleep(1)
            x.typewrite("https://www.youtube.com/watch?v=CJVkvY_F9UY&t=7s")

        else :
            print("lol")
                        

                

while True:
    time.sleep(2)
    autotype()
 



