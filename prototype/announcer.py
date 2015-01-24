# GOALS
# 1. build fake eyes (just produce linear set of same images)
# 2. build event logging
# 3. write analyzer

class Announcer:

	# league = input
	# event = output 
	def __init__(self, eyes, brain, mouth):
		# modules
		self.eyes = eyes
		self.brain = brain
		self.mouth = mouth
	
	def begin(self):
		# open the video stream to be read
		self.eyes.open()
		
		# two routes: just grab in main thread, or spawn new thread that grabs and pushes into a queue
		
		# initial will just grab in main thread for now
		while True:
			# announcer takes look at stream
			frame = self.eyes.see()
			
			# announcer brain processes things
			events = self.brain.analyse(frame)
			
			# announcer says / commentates on events going on
			self.mouth.say(events)

			
			
			
			
class AnnouncerEyes:
	def open(self):
		raise NotImplementedError()

	def see(self):
		raise NotImplementedError()

class AnnouncerBrain:
	def analyse(self, frame):
		raise NotImplementedError()

class AnnouncerMouth:
	def say(self):
		raise NotImplementedError()
		
		
		

		
# INTERFACE STRUCTURES
class Event:
	def __init__(self, time, name, data):
		self.time = time
		self.name = name
		self.data = data
		
	def __getitem__(self, key):
		return getattr(self, key, self.data[key])
		
class Frame:
	pass
