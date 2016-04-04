import numpy as np
import cv2
import os
from sklearn.metrics import jaccard_similarity_score
import scipy

#gt_dir = "/home/ubuntu/data/SegNet/ISBI/trainannot_all/"

#home_dir = "/home/ubuntu/data/SegNet/ISBI/test_output/"
home_dir = "/home/ubuntu/data/SegNet/ISBI/test_ISBI/"

test_dir = home_dir + "output/"
size_dir = home_dir + "input/"
#size_dir = "/home/ubuntu/data/SegNet/ISBI/train_all/"
 
paths = os.listdir(test_dir)
#print paths[1]
#get labels for ground truth files
scores =[]
scores_original =[]
i = 0
for path in paths:	
	i = i+1
	print i,path

	'''TEST
	image_gt = cv2.imread(gt_dir+path)
	
	image_gt_resized = cv2.resize(image_gt, (256,192))
	label_gt = np.sum(image_gt, axis = 2)/765
	label_gt_resized = np.sum(image_gt_resized, axis =2)/765
	'''

	image_size = cv2.imread(size_dir + path)
	image_test = cv2.imread(test_dir + path)
	
	#filtered_image = cv2.GaussianBlur(image_test, (5,5),0)
	#ret, filtered_image = cv2.threshold(filtered_image, 0,255,cv2.THRESH_BINARY) 

	image_test_resized = cv2.resize(image_test, (image_size.shape[1], image_size.shape[0]),interpolation=cv2.INTER_AREA)
	#image_test_resized = cv2.resize(image_test, (label_gt.shape[1], label_gt.shape[0]), interpolation=cv2.INTER_AREA)
	ret, filtered_image = cv2.threshold(image_test_resized, 0,255,cv2.THRESH_BINARY)
	
	kernel = np.ones((16,16), np.uint8)
	opening = cv2.morphologyEx(filtered_image, cv2.MORPH_OPEN, kernel)
	
	#closing = cv2.morphologyEx(opening, cv2.MORPH_CLOSE, kernel)
	#cv2.imwrite("/home/ubuntu/" + path + "g.png",  image_gt)
	#cv2.imwrite("/home/ubuntu/" + path + "gr.png", image_gt_resized)
	#cv2.imwrite("/home/ubuntu/" + path + "bound.png", filtered_image)
	#cv2.imwrite(home_dir + "final_output/" + path.split('.')[0] + '_1.png' , image_test_resized)
	#cv2.imwrite(home_dir + "final_output/" + path.split('.')[0] + '_2.png' , filtered_image)
	#cv2.imwrite(home_dir + "final_output/" + path.split('.')[0] + '_3.png' , closing)
	#cv2.imwrite(home_dir + "final_output/" + path.split('.')[0] + '_4.png' , opening)
	
	print(opening.dtype)
	scipy.misc.imsave(home_dir + "final_output/" + path.split('.')[0] + '_Segmentation.png' , opening)
	'''#Metrics
	label_test = np.sum(image_test, axis = 2)/765
	label_test_resized = np.sum(opening, axis = 2)/765
	
	#print image_test.shape, image_size.shape, image_size.shape, label_test.shape

	#print np.sum(image_gt), np.sum(image_test)

	y_true = label_gt_resized.flatten()
	y_pred = label_test.flatten()
	
	y_true_all = label_gt.flatten()
	y_pred_all = label_test_resized.flatten()
	
	scores.append(jaccard_similarity_score(y_true, y_pred))
	scores_original.append(jaccard_similarity_score(y_true_all, y_pred_all))

	print np.mean(scores), np.mean(scores_original)
	'''
	

	 

