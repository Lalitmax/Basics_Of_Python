import pyautogui
import time


i=1
time.sleep(5)
while i<=300:
    pyautogui.typewrite('hii')
    pyautogui.press("enter")
    i=i+1 