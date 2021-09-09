import pyautogui
from time import sleep
sleep(5
      )

f = open("beemovie.txt")
for word in f:
    sleep(1)
    pyautogui.typewrite(word)
    pyautogui.press("enter")

