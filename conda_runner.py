import pyautogui
import os
import time

location = os.getcwd()
pyautogui.press('win')
pyautogui.typewrite('anaconda prompt')
pyautogui.press('enter')
time.sleep(0.5)
pyautogui.click()
pyautogui.typewrite('cd ' + location)
pyautogui.press('enter')
pyautogui.typewrite('conda activate torchy')
pyautogui.press('enter')
pyautogui.typewrite('code .')
pyautogui.press('enter')