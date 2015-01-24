from announcer import AnnouncerBrain, Event
import datetime, random, string

class RandomBrain(AnnouncerBrain):
	
	def analyse(self, frame):
		def id_generator(size=6, chars=string.ascii_uppercase + string.digits):
			return ''.join(random.choice(chars) for _ in range(size))
		return Event(str(datetime.datetime.now().time().strftime("%H:%M:%S")), id_generator(), {})
