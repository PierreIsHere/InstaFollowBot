from pynput.mouse import Button, Controller as MouseController
import pyautogui
from time import sleep
import cv2
import numpy as np
mouse = MouseController()

def locator(image):
    t = pyautogui.screenshot('test.png')
    img_rgb = cv2.imread('test.png')
    template = cv2.imread(image +'.png')
    w, h = template.shape[:-1]

    res = cv2.matchTemplate(img_rgb, template, cv2.TM_CCOEFF_NORMED)
    threshold = .8
    loc = np.where(res >= threshold)
    temp = []
    coords = []
    for pt in zip(*loc[::-1]):
        temp.append(pt)
    if(len(temp) > 0):
        n = temp[0][0]
        # print(temp)
        for i in range (0,len(temp)):
            # print(temp[i])
            if(len(coords) == 0):
                coords.append(temp[i])
            if(coords[-1][1] == temp[i][1]):
                # print(temp[i])
                continue
            elif(((coords[-1][1] - 5) < temp[i][1]) and ((coords[-1][1] + 5 ) > temp[i][1])):
                # print(temp[i])
                continue
            else:
                coords.append(temp[i])
        return coords
    else:
        print("Cannot Locate")

def scroll(loc):
    x = loc[-1][0] - 50
    y = loc[-1][1]
    mouse.position = (x, y)
    mouse.press(Button.left)
    for i in range (0, y - loc[0][1]):
        mouse.position = (x, y-i)
        sleep(0.0005)
    sleep(1)
    mouse.release(Button.left)
# ufollow = locator("unfollow")
# print(ufollow)
x2 = 860
y2 = 519
sumfoll = 0 
for i in range (0,100):
    print("Iteration Number: "+str(i))
    sleep(1)
    loc = locator("following")
    # print(loc)
    if(loc == None):
        scroll([(954, 200),(954, 776)])
    if(loc != None):
        for i in loc:
            sumfoll+= 1
            print(sumfoll)
            x = i[0]+15
            y = i[1]+10
            mouse.position = (x,y)
            mouse.press(Button.left)
            mouse.release(Button.left)
            sleep(0.1)
            mouse.position = (x2,y2)
            mouse.press(Button.left)
            mouse.release(Button.left)
            sleep(0.1)
        scroll([(954, 200),(954, 776)])
    # sleep(0.1)
