"""
Robotic comment code using python pyAutogui

A code that automatically types comments and presses 'Enter' to send 
the comment. It was developed to annoy my friend.
It sends 5000 comments after 2 seconds delay.

**********************************************************
Warning: DO NOT TRY THIS. THIS MAY BE TAKEN AS CYBER CRIME
**********************************************************
"""
"""
Developed by: Ashraf Minhaj
mail: ashraf_minhaj@yahoo.com
"""

"""
You must have pyautogui installed in your pc.
If not try 'pip install pyautogui'  command.
"""


from time import sleep  #import sleep for delay
import pyautogui      #import pyautui package to use the keyboad in our case
x = 5000              #How many messages do I want to send

while True:     #forever loop
    pyautogui.typewrite("I'll help you buddy")  #type in the messsage
    sleep(.600)   #a bit delay of 600 ms
    pyautogui.typewrite("\n")  #Hit 'Enter' 
    sleep(2)                #delay of 2 seconds
    x = x - 1     #decrement x
    if x == 0:   #if x = 0 break the loop stop the code
        break     #break the loop

"""
It is said again and again not to use this code.
I will not hold any responsibilities for anything if you use this code.
"""
