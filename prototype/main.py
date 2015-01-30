from announcer import Announcer
from eyes import *
from brains import *
from mouths import *

if __name__ == "__main__":
	print "Hello Kevin!"
	eyes = TestEyes("../videos/lol_example1/")
	brain = RandomBrain()
	mouth = ClosedMouth()
	
	announcer = Announcer(eyes, brain, mouth)
	announcer.begin()