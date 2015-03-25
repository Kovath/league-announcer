from announcer import Announcer
from eyes import *
from brains import *
from mouths import *

import sys

if __name__ == "__main__":
	eyes = TestEyes(sys.argv[1])
	brain = TestBrain()
	mouth = PrintingMouth()
	
	announcer = Announcer(eyes, brain, mouth)
	announcer.begin()