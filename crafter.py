import pyautogui
import sys, os, time
from PIL import Image

class crafter:
    def __init__(self):
        print("INITIALIZED")
        self.log_im = Image.open("FF14_CRAFTING_MENU.png")
        self.log_im = self.log_im.copy()
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
        #get width and height
        w, h = self.log_im.size
        for a in range(0,w,20):
            for b in range(h):
                self.log_im.putpixel((a,b),(255,0,0,))
        self.log_im.save(".\sliced_Log.png")
        #SLICE UP THE CRAFTING LOG INTO USEFUL IMAGES

def main():
    c = crafter()
    c.set_screen("FF14_top_left_icon.png")
    c.slice_Log()

main()
