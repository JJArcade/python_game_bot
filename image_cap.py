#import pyscreenshot as ImageGrab	#LINUX VERSION
import re
import ImageGrab
import os, sys
import time
from datetime import datetime
from PIL import Image

class image_grabber:
	def __init__(self):
		self.box_start = (550,200)
		box_size = 300
		self.box = (self.box_start[0],self.box_start[1],self.box_start[0]+box_size+200,self.box_start[1]+box_size)
		self.positions = []
		self.init_pos = (0,0)
		self.found_pos = (0,0)

	def imageOpen(self):
		for a in os.listdir('.'):
			if bool(re.search('.png',a,re.IGNORECASE)):
				print("open\t"+str(a)+"?")
				ans = raw_input("")
				if ans == "y":
					self.im = Image.open(a)
					break

	def screenGrab(self):
	    print("waiting...")
	    #time.sleep(.5)
	    self.im = ImageGrab.grab(self.box)
	    print("image taken")
	    self.im_name = os.getcwd() + '\\screen shots\\full_snap__' + str(datetime.now().strftime("%d%m%y_%H%M%S")) + '.png'
		#self.im_name = os.getcwd() + '/full_snap__' + str(datetime.now().strftime("%d%m%y_%H%M%S")) + '.png'	#LINUX VERSION
	    #self.im.save(self.im_name, 'PNG')  #ALL VERSIONS

	def scan_image(self):
			last_shot = self.im
			#starting coordinates
			x = 0
			y = 0
			match_found = False
			while y<=290 and not match_found:
				for a in list(range(x,490)):
					#test if beginning corner in range
					test_pix = last_shot.getpixel((a,y))
					r_range = range(150,256)
					g_range = range(200,256)
					b_range = range(40,210)
					found = bool((test_pix[0] in r_range) and (test_pix[1] in g_range) and (test_pix[2] in b_range))
					if found:
						#print(test_pix)    #debug line
						test_grid = (a,y,a+3,y+3)
						test_sec = last_shot.crop(test_grid)
						#test_sec.save(os.getcwd()+'\\sections\\test_sec_'+str(a)+str(y)+'.png', 'PNG')
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
							self.found_pos = (a-4,y-4)
							return True
				y+=1
			return None

	def draw_border(self, color):
		last_shot = self.im
		start_corner = self.found_pos
		width, height = last_shot.size
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
			last_shot.putpixel(a,color)
		last_shot.save(os.getcwd() + '\\screen shots\\bordered_' + str(datetime.now().strftime("%d%m%y_%H%M%S")) + '.png', 'PNG')
		#last_shot.save(os.getcwd() + '/bordered_' + str(datetime.now().strftime("%d%m%y_%H%M%S")) + '.png', 'PNG')	#LINUX VERSION
		print("BORDER DRAWN AND SAVED.")

	def pos_change(self):
		pos_info = {"old_pos":(), "new_pos":(), "diff":(), "bite":False}
		if self.init_pos == (0,0):
			print("First Position")
			self.init_pos = self.found_pos
		pos_info["old_pos"] = self.init_pos
		pos_info["new_pos"] = self.found_pos
		delta_pos = (self.init_pos[0]-self.found_pos[0], self.init_pos[1]-self.found_pos[1])
		pos_info["diff"] = delta_pos
		out_str = "x change:\t% d\ny change:\t% d" % pos_info["diff"]
		print(out_str)
		#record possible event
		if abs(pos_info["diff"][0])>10 or abs(pos_info["diff"][1])>10:
			pos_info["bite"] = True
			print("BITE")
		self.init_pos = self.found_pos
		self.positions.append(pos_info)
		return pos_info

def main_loop():
	im_main = image_grabber()
	im_main.screenGrab()
	if bool(im_main.scan_image()):
		im_main.draw_border((255,0,0))

def debug_loop():
	im_main = image_grabber()
	im_main.imageOpen()
	if bool(im_main.scan_image()):
		im_main.draw_border((255,0,0))

def continous_loop():
	i = 0
	im_main = image_grabber()
	start_time = time.time()
	time_delta = 0
	while bool(time_delta<=30):
		im_main.screenGrab()
		im_main.scan_image()
		im_main.pos_change()
		if im_main.positions[len(im_main.positions)-1]["bite"]:
			im_main.draw_border((50,255,50))
		time_delta = time.time() - start_time
		print('---------------------')
	f = open(os.getcwd()+"\\output_.csv", 'w+')
	for a in im_main.positions:
		out_str = "% d,% d,%s\n" % (a["diff"][0],a["diff"][1],a["bite"])
		f.write(out_str)
	f.close()

def main():
	print "HERE WE GO"
	if len(sys.argv)>1:
		if str(sys.argv[1]) == "--debug":
			debug_loop()
		elif str(sys.argv[1]) == "--cont":
			continous_loop()
		else:
			main_loop()
	else:
		main_loop()

if __name__ == '__main__':
    main()
