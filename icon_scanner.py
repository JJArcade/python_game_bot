import pyautogui
import sys, os, time

class scanner:
	def __init__(self):
		icon_list = []

	def find_icon(self.icon):
		locs = list(pyautogui.locateAllOnScreen(icon))
		#print(locs)
		return locs
	
	def read_quantities(self):
		#placeholder
