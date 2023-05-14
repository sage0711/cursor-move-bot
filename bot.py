import pyautogui
import random
import win32api
import win32con
import ctypes

# Set up the screen size
screenWidth, screenHeight = pyautogui.size()

# Define the hook callback function
def hook_callback(event):
    # If a mouse or keyboard event is detected, exit the loop
    if event.Message == win32con.WM_MOUSEMOVE or \
       event.Message == win32con.WM_LBUTTONDOWN or \
       event.Message == win32con.WM_RBUTTONDOWN or \
       event.Message == win32con.WM_KEYDOWN:
        ctypes.windll.user32.PostQuitMessage(0)
        return False
    else:
        return True

# Install the hook callback function
hook_handle = ctypes.windll.user32.SetWindowsHookExA(
    win32con.WH_MOUSE_LL, 
    ctypes.cast(hook_callback, ctypes.c_void_p),
    ctypes.windll.kernel32.GetModuleHandleW(None), 0)

# Infinite loop that moves the mouse cursor randomly on the screen
while True:
    # Generate random x and y positions within the screen boundaries
    x = random.randint(0, screenWidth)
    y = random.randint(0, screenHeight)

    # Move the mouse cursor to the new position
    pyautogui.moveTo(x, y)

    # Process Windows messages to detect user input
    win32api.PumpWaitingMessages()

    # Check if the hook callback function has exited the loop
    if not ctypes.windll.user32.GetQueueStatus(win32con.QS_ALLEVENTS):
        break

# Uninstall the hook callback function
ctypes.windll.user32.UnhookWindowsHookEx(hook_handle)