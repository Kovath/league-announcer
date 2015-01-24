from announcer import AnnouncerMouth
import json

class ClosedMouth(AnnouncerMouth):
	def say(self, events):
		pass

class PrintingMouth(AnnouncerMouth):
	def say(self, events):
		print "[%s] %s -> %s" % (str(events.time), str(events.name), str(events.data))

class LoggingMouth(AnnouncerMouth):
	
	def __init__(self):
		self.log_file = open('log.txt', 'w')
	
	def say(self, events):
		events = json.dumps(events)
		self.log_file.write(events)