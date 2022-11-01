import pyautogui
import random
import time
import screeninfo
import sys
import threading
import queue


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

def add_input(input_queue):
    while 1:
        input_queue.put(sys.stdin.read(1))

def check_input(input_queue):
    # TODO: Check individual characters and handle
    #  e.g. 'q' will quit, 'p' will pause, 'r' will resume
    if not input_queue.empty():
        input = input_queue.get()
        print(f"\nGot input: {input}")
        print(f"Exiting.")
        return True

    return False

def sleep_and_check_input(input_queue, sleep_time):
    time_slept = 0

    print("Starting sleep...")
    while time_slept <= sleep_time:
        if not input_queue.empty():
            input = input_queue.get()
            print(f"\nGot input: {input}")
            print(f"Exiting.")
            return True
        else:
            print(f"Time slept: {time_slept}/{sleep_time} seconds")
            time_slept += 1
            time.sleep(1)

    return False

def mouse_movement():
    start_point = get_screen_center()
    x_min = start_point[0] - 100
    x_max = start_point[0] + 100
    y_min = start_point[1] - 100
    y_max = start_point[1] + 100

    while 1:
        while pyautogui.position()[0] < x_max:
            pyautogui.moveTo(x_max, y_min, duration = 2)

        while pyautogui.position()[1] < y_max:
            pyautogui.moveTo(x_max, y_max, duration = 2)

        while pyautogui.position()[0] > x_min:
            pyautogui.moveTo(x_min, y_max, duration = 2)

        while pyautogui.position()[1] > y_min:
            pyautogui.moveTo(x_min, y_min, duration = 2)

        time.sleep(10)

try:
    input_queue = queue.Queue()

    input_thread = threading.Thread(target=add_input, args=(input_queue,))
    input_thread.daemon = True
    input_thread.start()

    last_update = time.time()

#### TODO: Make all mouse movements use built in libraries instead of pyautogui ####

    # Move back to our starting spot just in case
    pyautogui.moveTo(get_screen_center()[0] - 100, get_screen_center()[1] - 100)
    mouse_thread = threading.Thread(target=mouse_movement)
    mouse_thread.daemon = True
    mouse_thread.start()

    while 1:
        if time.time() - last_update > 0.5:
            last_update = time.time()

        if check_input(input_queue):
            break

        time.sleep(0.5)
except pyautogui.FailSafeException:
    print("Mouse moved to top left corner, stopping...")
except KeyboardInterrupt:
    print('Key interrupt, stopping...')
finally:
    pass