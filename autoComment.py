import pyautogui
from time import sleep
from random import randint

x = 50

def name():
    """generate random names"""

    nameList = ["Baby", "Shona", "Honey", "Jaan", "Wifey"]
    rand_name = nameList[randint(0, len(nameList) - 1)]

    return rand_name



while True:
    pyautogui.typewrite(f"I love you {name()}")
    sleep(.600)
    pyautogui.typewrite("\n")
    sleep(2)

    x = x - 1

    if x == 0:
        break