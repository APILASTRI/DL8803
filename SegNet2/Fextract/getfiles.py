import os

PATH_TRAIN = "/home/ubuntu/data/SegNet2/Fextract/train_resized/"
PATH_TRAIN_LABEL = "/home/ubuntu/data/SegNet2/Fextract/trainannot_resized/"

PATH_TEST = "/home/ubuntu/data/SegNet2/Fextract/test_resized/"
PATH_TEST_LABEL = "/home/ubuntu/data/SegNet2/Fextract/testannot_resized/"

# generates train.txt
with open("/home/ubuntu/DL8803/SegNet2/Fextract/train.txt","w") as file:
	for files in os.listdir(PATH_TRAIN):
		file.write(PATH_TRAIN+files+" "+PATH_TRAIN_LABEL+files[0:12]+"_gt.png"+"\n")
		print PATH_TRAIN+files+" "+PATH_TRAIN_LABEL+files[0:12]+"_gt.png"

# generates test.txt
with open("/home/ubuntu/DL8803/SegNet2/Fextract/test.txt","w") as file:
	for files in os.listdir(PATH_TEST):
		file.write(PATH_TEST+files+" "+PATH_TEST_LABEL+files[0:12]+"_gt.png"+"\n")
		print PATH_TEST+files+" "+PATH_TEST_LABEL+files[0:12]+"_gt.png"

