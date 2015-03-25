from announcer import AnnouncerBrain, Event
from util import drawMatches
import datetime, random, string
import cv2, numpy as np

def match(img1, img2, feature_count=500):
	# Initiate SIFT detector
	orb = cv2.ORB(nfeatures=feature_count)

	# find the keypoints and descriptors with SIFT
	kp1, des1 = orb.detectAndCompute(img1, None)
	kp2, des2 = orb.detectAndCompute(img2, None)

	# FLANN_INDEX_KDTREE = 0
	# index_params = dict(algorithm = 6, table_number = 20, key_size = 15, multi_probe_level = 2)
	# search_params = dict(checks=50)   # or pass empty dictionary

	# flann = cv2.FlannBasedMatcher(index_params,search_params)
	# matches = flann.knnMatch(des1, des2, k=2)

	if des2 == None:
		des2 = np.zeros(des1.shape, dtype = des1.dtype)

	# create BFMatcher object
	bf = cv2.BFMatcher(cv2.NORM_HAMMING)
	matches = bf.knnMatch(des1, des2, k = 2)

	good = []
	for m, n in matches:
		if m.distance < 0.75 * n.distance:
			good.append(m)

	ratio = float(len(good)) / float(feature_count)
	img3 = drawMatches(img1, kp1, img2, kp2, good)
	if ratio > 0.1:
		cv2.imshow('dst', img3)
		cv2.waitKey(0)
		cv2.destroyAllWindows()

	return ratio





class RandomBrain(AnnouncerBrain):
	
	def analyse(self, frame):
		def id_generator(size=6, chars=string.ascii_uppercase + string.digits):
			return ''.join(random.choice(chars) for _ in range(size))
		return Event(str(datetime.datetime.now().time().strftime("%H:%M:%S")), id_generator(), {})

class TestBrain(AnnouncerBrain):

	def __init__(self):
		self.frame_index = 0

		# openCV stuff
		self.training_dir = "training/"
		self.victory_icon = cv2.imread(self.training_dir + "victory_icon.jpg", 0)
		self.turret_icon = cv2.imread(self.training_dir + "turret_icon.jpg", 0)

	def analyse(self, frame):
		# ANALYSIS
		start = cv2.getTickCount()
		
		victory_ratio = match(self.victory_icon, frame)
		# turret_ratio = match(self.turret_icon, frame)

		end = cv2.getTickCount()
		time_spent = (end - start)/cv2.getTickFrequency() * 1000

		event = Event(self.frame_index, "", {
			# "turret_ratio" : turret_ratio, 
			"victory_ratio" : victory_ratio, 
			"time" : time_spent,
		})

		if victory_ratio > 0.05:
			event.event = "victory"
		# elif turret_ratio > 0.05:
			# event.event = "turret"

		self.frame_index += 1
		return event