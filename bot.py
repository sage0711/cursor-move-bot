import pyautogui
import random

while True:

    x, y = pyautogui.position()
    new_x = x + random.randint(-100, 100)
    new_y = y + random.randint(-100, 100)
    pyautogui.moveTo(new_x, new_y, duration=0.25)

    