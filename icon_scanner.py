import pyautogui
import sys, os, time

def find_icon(icon):
    locs = list(pyautogui.locateAllOnScreen(icon))
    print(locs)
    return locs

time.sleep(3)
x = find_icon('.\cotton_t.png')
print(x[0])
a = x[0][0]
b = x[0][1]
pyautogui.click(a,b)

find_icon('synth.png')
