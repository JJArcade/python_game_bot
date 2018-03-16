from image_cap import image_grabber
import ImageGrab
import sys, os
import pyautogui
import re
import time

class main_bot:
    def __init__(self):
        self.im = image_grabber()

    def set_box(self):
        box_size = 300
        approved = False
        screen = ImageGrab.grab()
        while not approved:
            #define box points around crop area
            crop_box = []
            for a in list(range(self.im.box[0],self.im.box[2]+1)):  #x-points
                for b in (self.im.box[1], self.im.box[3]):
                    loc = (a,b)
                    crop_box.append(loc)
            for a in list(range(self.im.box[1],self.im.box[3]+1)):  #y-points
                for b in (self.im.box[0], self.im.box[2]):
                    loc = (b,a)
                    crop_box.append(loc)
            #draw box around potential border
            for a in crop_box:
                screen.putpixel(a,(255,0,255))
            sPath = os.getcwd() + "\\test_crop.png"
            screen.save(sPath, 'PNG')
            #open test crop for review
            os.system(sPath)
            #check if area is satisfactory
            answer = raw_input("Is this area ok?")
            if bool(re.search(answer, "y", re.IGNORECASE)):
                print("Area approved and saved.")
                approved = True
            else:
                newX = raw_input("Enter the new x:\t")
                newY = raw_input("Enter the new y:\t")
                self.im.box_start = (int(newX), int(newY))
                self.im.box = (self.im.box_start[0],self.im.box_start[1],self.im.box_start[0]+box_size+200,self.im.box_start[1]+box_size)

    def cast_rod(self):
        pyautogui.press('2')
        time.sleep(8)
        print("Rod cast.")

    def strike_rod(self):
        pyautogui.press('3')
        time.sleep(15)
        print("Fish reeled.")

    def main_loop(self):
        self.cast_rod()
        while True:
            self.im.screenGrab()
            self.im.scan_image()
            x = self.im.pos_change()
            if bool(x["bite"]):
                self.strike_rod()
                self.cast_rod()
                #do initial scan to reset position
                self.im.screenGrab()
                self.im.scan_image()
                self.im.pos_change()

if __name__ == "__main__":
    bot = main_bot()
    for a in sys.argv:
        if a == '--set-box':
            bot.set_box()
    print("Bot starting in 5 seconds.")
    time.sleep(5)
    bot.main_loop()
