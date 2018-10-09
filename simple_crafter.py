import pyautogui
import sys, os, time
from PIL import Image
from datetime import datetime

def exit_game():
    #escape till system menu
    menu_up = False
    exitLoc = None
    while not menu_up:
        pyautogui.press("esc")
        time.sleep(2)
        exitLoc = pyautogui.locateOnScreen(".\\pics\\exit_game.png")
        time.sleep(2)
        if exitLoc is not None:
            menu_up = True
    #move to exit button
    time.sleep(1)
    pyautogui.moveTo(exitLoc[0]+exitLoc[2]/2, exitLoc[1]+exitLoc[3]/2, duration=.25)
    pyautogui.click()
    pyautogui.click()
    time.sleep(1)
    #hit ok
    time.sleep(1)
    ok_loc = pyautogui.locateOnScreen(".\\pics\\ok_button.png")
    time.sleep(1)
    pyautogui.moveTo(ok_loc[0]+ok_loc[2]/2, ok_loc[1]+ok_loc[3]/2, duration=.25)
    pyautogui.click()
    pyautogui.click()

##get sys argv
if len(sys.argv)<=1:
    print("Need a quantity argument.")
    quit()

##get start time
startTime = datetime.now()
print("Starting in 5 seconds...")
time.sleep(1)
for a in range(1,5):
    print(str(5-a)+"...")
    time.sleep(1)
##main main_loop
#item to craft always ctrl+5
pyautogui.keyDown("ctrl")
pyautogui.press('5')
pyautogui.keyUp("ctrl")
time.sleep(.5)
#find synthesize button
synth_loc = pyautogui.locateOnScreen(".\\pics\\synth_2.png", grayscale=True)
#craft loop
crafted = 0
to_craft = int(sys.argv[1])
while crafted<to_craft:
    pyautogui.moveTo(synth_loc[0]+synth_loc[2]/2,synth_loc[1]+synth_loc[3]/2, duration=.25)
    time.sleep(1)
    pyautogui.click()
    pyautogui.click()
    time.sleep(1)
    pyautogui.moveTo(600,600)
    pyautogui.keyDown("ctrl")
    pyautogui.press('4')
    pyautogui.keyUp("ctrl")
    done = False
    while not done:
        time.sleep(1)
        synth_loc = pyautogui.locateOnScreen(".\\pics\\synth_2.png", grayscale=True)
        if synth_loc is not None:
            crafted+=1
            print("Crafted\n%s:%s" %(crafted,to_craft))
            done = True
#end of main_loop
print("Crafting done.")
print(datetime.now() - startTime)
for a in sys.argv:
    if a == "--quit-game":
        exit_game()
