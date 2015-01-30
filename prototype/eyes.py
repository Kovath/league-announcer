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
		self.files = sorted(self.files, key = lambda s: int(s.split("/")[-1].split(".")[0]))

	def see(self):
		try:
			frame_file = open(self.files[self.stream_index])
			frame = frame_file.read()
			frame_file.close()
			
			self.stream_index += 1
			return frame
		except IndexError as e:
			return None
