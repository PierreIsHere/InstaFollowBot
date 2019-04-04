from pynput.mouse import Button, Controller as MouseController
from time import sleep
import pyautogui
mouse = MouseController()

def colourCheck():
    img = pyautogui.screenshot()
    colour = img.getpixel(pyautogui.position())
    return colour
def init():
    n = pyautogui.locateOnScreen('follow.png')
    if(n is None):
        print("Cannot Locate Follow Button")
        exit()
    mouse.position = (n[0]+20, n[1]+20)
    loc = [n[0]+20,n[1]+20]
    return loc

follow =(56, 151, 240)

loc = init()
print(loc);
for i in range (0,5):
    print(i)
    if(colourCheck() == follow):
        print("sadsdd")
        mouse.press(Button.left)
        sleep(0.2)
        mouse.release(Button.left)
    mouse.scroll(0,-1)
    sleep(1)
# //(56, 151, 240)

