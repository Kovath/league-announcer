from announcer import AnnouncerEyes
import os
import cv2, numpy as np

class ClosedEyes(AnnouncerEyes):
	def open(self):
		pass
	
	def see(self):
		pass

class TestEyes(AnnouncerEyes):
	
	def __init__(self, frame_folder):
		self.frame_folder = frame_folder
		self.files = []
		self.stream_index = 0
	
	def open(self):
		for file in os.listdir(self.frame_folder):
			self.files.append(self.frame_folder + file)
		self.files = sorted(self.files, key = lambda s: int(s.split("/")[-1].split(".")[0].split("-")[0]))

	def see(self):
		try:
			frame = cv2.imread(self.files[self.stream_index], 0)
			self.stream_index += 1
			
			return frame
		except IndexError as e:
			exit()
