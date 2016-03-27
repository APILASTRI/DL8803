import numpy as np
import matplotlib.pyplot as plt
plt.switch_backend('agg')

import os.path
import json
import scipy
import argparse
import math
import pylab
from sklearn.preprocessing import normalize
from sklearn.metrics import jaccard_similarity_score
caffe_root = '/home/ubuntu/caffe-segnet/' 			# Change this to the absolute directoy to SegNet Caffe
import sys
sys.path.insert(0, caffe_root + 'python')

import caffe

# Import arguments
parser = argparse.ArgumentParser()
parser.add_argument('--model', type=str, required=True)
parser.add_argument('--weights', type=str, required=True)
parser.add_argument('--iter', type=int, required=True)
args = parser.parse_args()

caffe.set_mode_gpu()

net = caffe.Net(args.model,
                args.weights,
                caffe.TEST)

scores=[]

for i in range(0, args.iter):

	net.forward()

	image = net.blobs['data'].data
	label = net.blobs['label'].data
	predicted = net.blobs['prob'].data

	image = np.squeeze(image[0,:,:,:])
	label = np.squeeze(label[0,:,:,:])
	output = np.squeeze(predicted[0,:,:,:])
	ind = np.argmax(output, axis=0)

	r = ind.copy()
	g = ind.copy()
	b = ind.copy()
	r_gt = label.copy()
	g_gt = label.copy()
	b_gt = label.copy()

	Skin = [0,0,0]
	Lesion = [255,255,255]

	label_colours = np.array([Skin,Lesion])
	for l in range(0,2):
		r[ind==l] = label_colours[l,0]
		g[ind==l] = label_colours[l,1]
		b[ind==l] = label_colours[l,2]
		r_gt[label==l] = label_colours[l,0]
		g_gt[label==l] = label_colours[l,1]
		b_gt[label==l] = label_colours[l,2]

	rgb = np.zeros((ind.shape[0], ind.shape[1], 3))
	rgb[:,:,0] = r/255.0
	rgb[:,:,1] = g/255.0
	rgb[:,:,2] = b/255.0
	rgb_gt = np.zeros((ind.shape[0], ind.shape[1], 3))
	rgb_gt[:,:,0] = r_gt/255.0
	rgb_gt[:,:,1] = g_gt/255.0
	rgb_gt[:,:,2] = b_gt/255.0

	image = image/255.0

	image = np.transpose(image, (1,2,0))
	output = np.transpose(output, (1,2,0))
	image = image[:,:,(2,1,0)]

	# print image.shape,rgb_gt.shape,rgb.shape
	#scipy.misc.toimage(rgb, cmin=0.0, cmax=255).save(IMAGE_FILE+'_segnet.png')

	plt.figure()
	plt.imshow(image,vmin=0, vmax=1)
	plt.figure()
	plt.imshow(rgb_gt,vmin=0, vmax=1)
	plt.figure()
	plt.imshow(rgb,vmin=0, vmax=1)
	plt.show()

	y_true = label.flatten()
	y_pred = ind.flatten()

	score = jaccard_similarity_score(y_true, y_pred)
	scores.append(score)
	print "image ",i," score: ",score


print 'Success!'
print "mean accuracy: ",np.array(scores).mean()
