import pyautogui
import random

try:
    while 1:
        xCurr = random.randint(100, 250)
        yCurr = random.randint(100, 250)
        pyautogui.moveTo(xCurr, yCurr, duration = ((xCurr + yCurr) / 120))
except KeyboardInterrupt:
    print('Key interrupt, stopping...')
