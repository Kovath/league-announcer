# VIDEO FRAME CAPPER
# by Kevin Yang
#
# A quickly made tool to grab intervals of frames of a video and save to disk
# python video_capper <filename> <frame interval>

import cv2, os, sys, string

def makedir(dir):
	try:
		os.makedirs(dir)
	except OSError as e:
		pass	


if __name__ == "__main__":
	# arguments
	filename = sys.argv[1]
	interval = int(sys.argv[2]) # in frames
	checkpoint_count = 20

	# intermediate values
	video = cv2.VideoCapture(filename)
	total_frames = video.get(cv2.cv.CV_CAP_PROP_FRAME_COUNT)
	out_dir = string.join(filename.split(".")[0:-1], ".") + '/'
	checkpoints = map(lambda x: x / float(checkpoint_count), range(1, checkpoint_count + 2))

	# some preliminary setup
	makedir(out_dir)



	# detail output
	print("VIDEO DETAILS")
	print("-------------")
	print("%s: %s" % ("file name", filename.split("/")[-1]))
	print("%s: %d" % ("total frames", total_frames))
	print("%s: %d" % ("fps", video.get(cv2.cv.CV_CAP_PROP_FPS)))
	print("%s: %dx%d" % ("dimensions", video.get(cv2.cv.CV_CAP_PROP_FRAME_WIDTH), video.get(cv2.cv.CV_CAP_PROP_FRAME_HEIGHT)))

	print("")

	# EXECUTE THE CAPPING
	frame_index = 0
	print("PROGRESS")
	print("--------")
	while(video.isOpened()):
		if (float(frame_index) / float(total_frames)) >= checkpoints[0]:
			print("%d%%" % (int(checkpoints.pop(0) * 100)))

		frame = video.read()
		if frame[0] != 1:
			break
		if (frame_index % interval) == 0:
			pass
			cv2.imwrite(out_dir + str(frame_index) + '.jpg', frame[1])
		frame_index += 1
	video.release()

	print("FINISHED")

	# operation output
	# if later want to add time taken, etc.
	#print("OPERATION DETAILS")