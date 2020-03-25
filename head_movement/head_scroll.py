from headmovement import classify
from pynput.mouse import Controller
import cv2

mouse = Controller()

while True:
    pos = classify()

    print(pos)

    if pos == 0:
        mouse.scroll(0, .1)
    elif pos == 2:
        mouse.scroll(0, -.1)

    if cv2.waitKey(1) == 27:
        break
    
cv2.destroyAllWindows()