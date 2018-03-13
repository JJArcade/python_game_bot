#import pyscreenshot as ImageGrab   #LINUX VERSION
import ImageGrab
import os
import time
from datetime import datetime
from PIL import Image

class image_grabber:
	def __init__(self):
		self.box = (648,363,941,597)
	    
	def screenGrab(self):
	    print("waiting...")
	    time.sleep(5)
	    self.im = ImageGrab.grab(self.box)
	    print("image taken")
	    self.im_name = os.getcwd() + '\\full_snap__' + str(datetime.now().strftime("%d%m%y_%H%M%S")) + '.png'
		#self.im_name = os.getcwd() + '/full_snap__' + str(datetime.now().strftime("%d%m%y_%H%M%S")) + '.png'	#LINUX VERSION
	    im.save(im_name, 'PNG')  #WINDOWS VERSION
	    #im.save(os.getcwd() + '/full_snap__' + str(int(time.time())) + '.png', 'PNG')   #LINUX VERSION

	def scan_image(self, image_name):
			last_shot = self.im
			#starting coordinates
			x = 0
			y = 0
			match_found = False
			while y<=231 and not match_found:
				for a in list(range(x,290)):
					#test if beginning corner in range
					test_pix = last_shot.getpixel((a,y))
					r_range = range(145,256)
					g_range = range(145,256)
					b_range = range(0,100)
					found = bool((test_pix[0] in r_range) and (test_pix[1] in g_range) and (test_pix[2] in b_range))
					if found:
						#print(test_pix)    #debug line
						test_grid = (a,y,a+3,y+3)
						test_sec = last_shot.crop(test_grid)
						test_sec.save(os.getcwd()+'\\sections\\test_sec_'+str(a)+str(y)+'.png', 'PNG')
						c=0
						match = False
						for b in list(range(0,3)):
							test_pix = test_sec.getpixel((b,c))
							found = bool((test_pix[0] in r_range) and (test_pix[1] in g_range) and (test_pix[2] in b_range))
							if not found:
								match=False
								break
							else:
								c+=1
								match=True
						if match:
							print("MATCH FOUND!")
							border_corner = (a-4,y-4)
							#draw_border(border_corner,last_shot)
							#match_found = True
							return border_corner
				y+=1
			return None



'''def screenGrab():
    box = (648,363,941,597)
    #box = ()
    print("waiting...")
    time.sleep(5)
    im = ImageGrab.grab(box)
    print("image taken")
    im_name = os.getcwd() + '\\full_snap__' + str(int(time.time())) + '.png'
    im.save(im_name, 'PNG')  #WINDOWS VERSION
    #im.save(os.getcwd() + '/full_snap__' + str(int(time.time())) + '.png', 'PNG')   #LINUX VERSION
    return im_name'''

def scan_image(image_name):
    last_shot = Image.open(image_name,'r')
    #starting coordinates
    x = 0
    y = 0
    match_found = False
    while y<=231 and not match_found:
        for a in list(range(x,290)):
            #test if beginning corner in range
            test_pix = last_shot.getpixel((a,y))
            r_range = range(145,256)
            g_range = range(145,256)
            b_range = range(0,100)
            found = bool((test_pix[0] in r_range) and (test_pix[1] in g_range) and (test_pix[2] in b_range))
            if found:
                #print(test_pix)    #debug line
                test_grid = (a,y,a+3,y+3)
                test_sec = last_shot.crop(test_grid)
                test_sec.save(os.getcwd()+'\\sections\\test_sec_'+str(a)+str(y)+'.png', 'PNG')
                c=0
                match = False
                for b in list(range(0,3)):
                    test_pix = test_sec.getpixel((b,c))
                    found = bool((test_pix[0] in r_range) and (test_pix[1] in g_range) and (test_pix[2] in b_range))
                    if not found:
                        match=False
                        break
                    else:
                        c+=1
                        match=True
                if match:
                    print("MATCH FOUND!")
                    border_corner = (a-4,y-4)
                    #draw_border(border_corner,last_shot)
                    #match_found = True
                    return border_corner
        y+=1
    return None

def draw_border(start_corner, image_name):
    last_shot = Image.open(image_name)
    width, height = last_shot.size
    #print(str(width)+'\t'+str(height))  #debug line
    mark_list=[]
    x = start_corner[0]
    y = start_corner[1]
    #top and bottom border
    for a in list(range(x,x+11)):
        mark_list.append((a,y))
        mark_list.append((a,y+10))
    #left and right border
    for a in list(range(y,y+11)):
        mark_list.append((x,a))
        mark_list.append((x+10,a))
    #mark all points
    for a in mark_list:
        #print(a)
        last_shot.putpixel(a,(255,0,0))
    last_shot.save(os.getcwd() + '\\bordered_' + str(int(time.time())) + '.png', 'PNG')
    print("BORDER DRAWN AND SAVED.")

def main():
    z = screenGrab()
    x = scan_image(z)
    if bool(x):
        draw_border(x,z)

if __name__ == '__main__':
    main()
