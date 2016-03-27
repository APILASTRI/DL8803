import os
import cv2

path = '/home/ubuntu/data/SegNet/ISBI/trainannot_all/'
for file in os.listdir(path):
	image = cv2.imread(path+file)
	if image is not None: 
		print file
		image[image>0] = 1	
		resized_image = cv2.resize(image, (256, 192))
		cv2.imwrite(path + 'transformed/' + file, resized_image)
