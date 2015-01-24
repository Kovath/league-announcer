from announcer import AnnouncerEyes
import os

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
	
	def see(self):
		frame_file = open(self.files[self.stream_index])
		frame = frame_file.read()
		frame_file.close()
		
		print self.stream_index
		self.stream_index += 1
		return frame
