import pyscreenshot as ImageGrab
import os
import time

def screenGrab():
    box = ()
    print("waiting...")
    time.sleep(5)
    im = ImageGrab.grab()
    print("image taken")
    im.save(os.getcwd() + '//full_snap__' + str(int(time.time())) + '.png', 'PNG')

def main():
    screenGrab()

if __name__ == '__main__':
    main()
