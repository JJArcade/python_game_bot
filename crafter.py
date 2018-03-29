import pyautogui
import sys, os, time
from PIL import Image

class crafter:
    def __init__(self):
        print("INITIALIZED")
        self.log_im_region = [0,0,884,625]
        #PUT STUFF HERE LATER

    def set_screen(self, icon_loc):
        #find the icon location
        locs = pyautogui.locateOnScreen(icon_loc)
        if locs is not None:
            x = locs[0]
            y = locs[1]
            #move mouse in positions
            pyautogui.moveTo(x+30,y+10)
            #drag screen to corner
            pyautogui.mouseDown()
            pyautogui.moveTo(31,11,duration=.5)
            pyautogui.mouseUp()
        else:
            print("NOT FOUND")

    def slice_Log(self):
        #get crafting image screenshot
        log_loc = pyautogui.locateOnScreen(".\\ff14_crafting_icon.png")
        self.log_im_region[0]=log_loc[0]
        self.log_im_region[1]=log_loc[1]
        self.log_im = pyautogui.screenshot(region=self.log_im_region)
        #get width and height
        w, h = self.log_im.size
        '''for a in range(0,w,20):
            for b in range(h):
                self.log_im.putpixel((a,b),(255,0,0,))'''
        self.log_im.save(".\\sliced_Log.png")
        #SLICE UP THE CRAFTING LOG INTO USEFUL IMAGES

    def craft_loop(self):
        icon_loc = pyautogui.locateOnScreen("dbmg.png")
        pyautogui.moveTo(icon_loc[0]+15,icon_loc[1]+15)
        time.sleep(.5)
        pyautogui.click()
        pyautogui.click()
        time.sleep(.5)
        pyautogui.mouseUp()
        icon_loc = pyautogui.locateOnScreen("pp.png")
        pyautogui.moveTo(icon_loc[0]+40,icon_loc[1]+20,duration=1)
        time.sleep(.5)
        pyautogui.click()
        pyautogui.click()
        time.sleep(1)
        pyautogui.moveTo(1,1,duration=.25)
        pyautogui.mouseUp()
        table_loc = pyautogui.locateOnScreen("Capture.png")
        pyautogui.moveTo(table_loc[0]+20,table_loc[1]+20)
        time.sleep(.5)
        pyautogui.click()
        pyautogui.click()
        time.sleep(.5)
        pyautogui.mouseUp()
        synth_loc = pyautogui.locateOnScreen("synth.png")
        pyautogui.moveTo(synth_loc[0]+30,synth_loc[1]+10)
        time.sleep(.5)
        pyautogui.click()
        pyautogui.click()
        time.sleep(2)
        #craft loop
        log_up = pyautogui.locateOnScreen("ff14_crafting_icon.png")
        while log_up is None:
            pyautogui.press("1")
            time.sleep(3)
            log_up = pyautogui.locateOnScreen("ff14_crafting_icon.png")
        time.sleep(10)


def main():
    c = crafter()
    c.set_screen("FF14_top_left_icon.png")
    c.slice_Log()
    while True:
        c.craft_loop()

main()
