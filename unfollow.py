#to unfollow every account
import pyautogui as pag
import time
from random import randint

j = 0
i = 50 #50 unfollows do not unfollow more than 200 per day, insta may block your account
while True: 
    print(j)
    if j > i: 
        break
    followLocation = pag.locateOnScreen('unfollow.png', confidence = 0.9)
    if followLocation != None:
        followPoint = pag.center(followLocation)
        pag.moveTo(followPoint)
        pag.click()
        j = j + 1
        rand3 = randint(10,30)/25
        time.sleep(rand3)
        ufLocation = pag.locateOnScreen('confirm.png', confidence = 0.9)
        if ufLocation != None:
            ufPoint = pag.center(ufLocation)
            pag.moveTo(ufPoint)
            pag.click() 
            rand3 = randint(10,30)/25
            time.sleep(rand3)
        pag.scroll(-138)
        time.sleep(rand3)
