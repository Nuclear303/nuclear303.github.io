import pyautogui
import time

time.sleep(3)
for i in range(10):
    pyautogui.write("m!m")
    pyautogui.press("enter")
    time.sleep(3)

