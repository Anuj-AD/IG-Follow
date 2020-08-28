#to like every post
import pyautogui as pag
import time
from random import randint

j = 0
i = 50 #50 follows
while True: 
    print(j)
    if j > i: 
        break
    followLocation = pag.locateOnScreen('follow.png', confidence = 0.9)
    if followLocation != None:
        followPoint = pag.center(followLocation)
        pag.moveTo(followPoint)
        pag.click()
        j = j + 1
        rand3 = randint(10,30)/25
        time.sleep(rand3)
        pag.scroll(-138)
        time.sleep(rand3)
