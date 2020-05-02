
# def linkTo(*args):
#     time.sleep(5)
#     pyautogui.hotkey('ctrl', 'l')
#     for i in args:
#         link="https://www.youtube.com/results?search_query"+i
#         pyautogui.write(link)
#         pyautogui.press('enter')
#         page=requests.get("https://www.youtube.com/results?search_query"+i)
#         soup= BeautifulSoup(page.content,'lxml', from_encoding="latin-1")

#         time.sleep(5)
#         pyautogui.hotkey('ctrl','f').sleep(5)
#         pyautogui.write('comments')
#         time.sleep(5)
#         pyautogui.click(x=324, y=478)               # find yourself comment box
#         pyautogui.write(msg)
#         break


# linkTo(*urls_list)