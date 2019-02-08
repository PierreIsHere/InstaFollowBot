from pynput.mouse import Button, Controller as MouseController
from time import sleep
mouse = MouseController()
def scroll(f):
    mouse.position = (1227, f)
    mouse.press(Button.left)
    for i in range (0, 583):
        mouse.position = (1227, f-i)
        sleep(0.005)
    sleep(1)
    mouse.position = (1227, 154)
    mouse.release(Button.left)
    mouse.position = (1338, 158)


def goBack():
    mouse.position =(939, 67)
    mouse.press(Button.left)
    mouse.release(Button.left)
    sleep(0.05)
    mouse.press(Button.left)
    mouse.release(Button.left)
    sleep(0.05)
    mouse.press(Button.left)
    mouse.release(Button.left)
    mouse.position = (1043, 479)
    mouse.press(Button.left)
    mouse.move(0, -8)
    mouse.release(Button.left)
    sleep(0.09)
    mouse.press(Button.left)
    mouse.release(Button.left)
    mouse.press(Button.left)
    mouse.release(Button.left)
    mouse.position = (1000, 107)
    sleep(0.1)
    mouse.press(Button.left)
    mouse.release(Button.left)
    mouse.position = (1204, 121)
    sleep(0.5)
    mouse.press(Button.left)
    mouse.release(Button.left)
    sleep(0.5)
    mouse.position = (1162, 194)
    sleep(0.3)
    mouse.press(Button.left)
    for i in range(0, 36):
        mouse.position = (1162, 194 - i)
        sleep(0.005)
    sleep(1)
    mouse.position = (1227, 154)
    mouse.release(Button.left)

n = 158
for v in range (0,2):
    for q in range (0,2):
        n = 158
        for i in range (0,10):
            print(i)
            mouse.position = (1338, n)
            mouse.press(Button.left)
            mouse.release(Button.left)
            sleep(0.15)
            n = n +58
            # print(mouse.position)
            f = 738
            # if i == 10:
            #     mouse.position = (1338, f)
        print(q)
        scroll(f)
    goBack()
