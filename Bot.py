from pynput.mouse import Button, Controller as MouseController
from time import sleep
mouse = MouseController()
# mouse.position = (1338, 158)
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
    sleep(1)
    mouse.press(Button.left)
    mouse.release(Button.left)
    sleep(1)
    mouse.press(Button.left)
    mouse.release(Button.left)
    sleep(1)
    mouse.position = (1043, 479)
    mouse.press(Button.left)
    mouse.move(0, -8)
    mouse.release(Button.left)
    sleep(0.5)
    mouse.press(Button.left)
    mouse.release(Button.left)
    mouse.press(Button.left)
    mouse.release(Button.left)
    sleep(0.2)
    mouse.position = (1000, 107)
    sleep(1.2)
    mouse.press(Button.left)

    mouse.release(Button.left)
    mouse.position = (1204, 121)
    sleep(1.2)
    mouse.press(Button.left)
    mouse.release(Button.left)
    sleep(1)
    mouse.position = (1162, 194)
    sleep(1.2)
    mouse.press(Button.left)
    for i in range(0, 36):
        mouse.position = (1162, 194 - i)
        sleep(0.005)
    sleep(1)
    mouse.position = (1227, 154)
    mouse.release(Button.left)

def unFollow():
    mouse.position = (839, 76)
    sleep(0.1)
    mouse.click(Button.left)
    mouse.release(Button.left)
    sleep(1)
    mouse.position = (848, 468)
    sleep(0.1)
    mouse.click(Button.left)
    mouse.release(Button.left)
    sleep(3)
    mouse.position = (869, 151)
    for i in range(0, 8):
        for i in range(0, 16):
            mouse.position = (869, 151)
            mouse.press(Button.left)
            mouse.release(Button.left)
            sleep(0.8)
        sleep(80)

n = 158
for l in range (0,5)
    for v in range (0,4):
        for q in range (0,3):
            n = 158
            for i in range (0,10):
                mouse.position = (1338, n)
                mouse.press(Button.left)
                mouse.release(Button.left)
                sleep(0.2)
                n = n +58
                f = 738
            sleep(10)
            scroll(f)
        sleep(120)
        goBack()
    unFollow()