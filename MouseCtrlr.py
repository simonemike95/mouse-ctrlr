import pyautogui
import random

# Moving cursor to top left of screen will kill the script
pyautogui.FAILSAFE = True

try:
    while 1:
        xCurr = random.randint(0, pyautogui.size().width - 100)
        yCurr = random.randint(0, pyautogui.size().height - 100)
        pyautogui.moveTo(xCurr, yCurr, duration = ((xCurr + yCurr) / 120))
        pyautogui.press('shift')
except KeyboardInterrupt:
    print('Key interrupt, stopping...')
