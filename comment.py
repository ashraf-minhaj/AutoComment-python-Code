from time import sleep
import pyautogui
x = 5000

while True:
    pyautogui.typewrite("I'll help you buddy")
    sleep(.600)
    pyautogui.typewrite("\n")
    sleep(2)
    x = x - 1
    if x == 0:
        break