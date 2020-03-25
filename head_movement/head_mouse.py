import headmovement
from pynput.mouse import Controller
import cv2

mouse = Controller()

while True:

    pos = headmovement.getHeadOrientation()

    print(pos)

    if pos == "up":
        mouse.move(0,-1)
    elif pos == "down":
        mouse.move(0,1)
    elif pos == "left":
        mouse.move(-1,0)
    elif pos == "right":
        mouse.move(1,0)

    if cv2.waitKey(1) == 27:
        break