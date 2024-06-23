import pyautogui
import time
import pyperclip

def click_on_chrome_icon():
    pyautogui.click(1639, 1412)
    time.sleep(1)

def select_text():
    pyautogui.moveTo(972, 202)
    pyautogui.dragTo(2213, 1278, duration=2.0, button='left')
    pyautogui.hotkey('ctrl', 'c')
    time.sleep(2)

def paste_response():
    pyautogui.click(1808, 1328)
    time.sleep(1)
    pyautogui.hotkey('ctrl', 'v')
    time.sleep(1)
    pyautogui.press('enter')

def click_on_input_box():
    pyautogui.click(1994, 281)
