import pyautogui
import random
import time
import screeninfo

# Moving cursor to top left of screen will kill the script
# Otherwise just killing the process with ctrl+c will work as well
pyautogui.FAILSAFE = True

def get_primary_screen():
    for display in screeninfo.get_monitors():
        if display.is_primary:
            return display

def get_screen_center():
    '''
    Screen coords look like this:
    #############################
    #x_min, y_min               #
    #                           #
    #                           #
    #                           #
    #                           #
    #               x_max, y_max#
    #############################
    '''

    display = get_primary_screen()
    center_h = display.height / 2
    center_w = display.width / 2
    center = [center_w, center_h]
    return center

try:
    start_point = get_screen_center()
    x_min = start_point[0] - 100
    x_max = start_point[0] + 100
    y_min = start_point[1] - 100
    y_max = start_point[1] + 100

    while 1:
        # Move back to our starting spot just in case
        pyautogui.moveTo(x_min, y_min)

        # Move from x_min to x_max (left to right)
        while pyautogui.position()[0] < x_max:
            pyautogui.moveTo(x_max, y_min, duration = 2)
        time.sleep(10)

        # move from y_min to y_max (top to bottom)
        while pyautogui.position()[1] < y_max:
            pyautogui.moveTo(x_max, y_max, duration = 2)
        time.sleep(10)

        # Move from x_max to x_min (right to left)
        while pyautogui.position()[0] > x_min:
            pyautogui.moveTo(x_min, y_max, duration = 2)
        time.sleep(10)

        # Move from y_max to y_min (bottom to top)
        while pyautogui.position()[1] > y_min:
            pyautogui.moveTo(x_min, y_min, duration = 2)
        time.sleep(10)

        pyautogui.press('shift')
except pyautogui.FailSafeException:
    print("Mouse moved to top left corner, stopping...")
except KeyboardInterrupt:
    print('Key interrupt, stopping...')