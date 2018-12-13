import os
from sklearn.model_selection import train_test_split
import shutil
from PIL import Image
import argparse
import urllib.request

"""Script for extracting, and splitting files from original ADE20K dataset
"""

def extract_files():
	img_path = "ADE20K_2016_07_26/images/" 
	imgs = []
	seg_imgs = []

	for split in os.listdir(img_path):
		split_path = os.path.join(img_path, split)
		for alpha in os.listdir(split_path):
			alpha_path = os.path.join(split_path, alpha)
			if alpha != "misc":
				for loc in os.listdir(alpha_path):
					loc_path = os.path.join(alpha_path, loc)
					for img in os.listdir(loc_path):
						if ".jpg" == img[-4:] or "_seg" in img:
							shutil.copyfile(os.path.join(loc_path, img), os.path.join("ADE20K/", img))
			else:
				for img in os.listdir(alpha_path):
					if ".jpg" == img[-4:] or "_seg" in img:
                                                        shutil.copyfile(os.path.join(alpha_path, img), os.path.join("ADE20K/", img))

def save_split(split, split_name):
	img_path = "ADE20K"
	for img in split:
                if img <= 20210:
                        new_name = str(img).zfill(8)
                        name = "ADE_train_" + new_name + ".jpg"
                        seg = "ADE_train_" + new_name + "_seg.png"
                        if os.path.isfile(os.path.join(img_path, name)) and os.path.isfile(os.path.join(img_path, seg)):
                                Image.open(os.path.join(img_path,seg)).convert('RGB').save(os.path.join(img_path,seg[:-4] + '.jpg'))
                                #os.remove(seg)
                                new_seg = seg[:-4] + '.jpg'
                                shutil.move(os.path.join(img_path, name), os.path.join(img_path,"A", split_name, new_name + ".jpg"))
                                shutil.move(os.path.join(img_path, new_seg), os.path.join(img_path,"B", split_name,  new_name+ ".jpg"))
                if img > 20210:
                        img = img - 20210
                        new_name = str(img).zfill(8)
                        name = "ADE_val_" + new_name + ".jpg"
                        seg = "ADE_val_" + new_name + "_seg.png"
                        if os.path.isfile(os.path.join(img_path, name)) and os.path.isfile(os.path.join(img_path, seg)):
                                Image.open(os.path.join(img_path,seg)).convert('RGB').save(os.path.join(img_path,seg[:-4] + '.jpg'))
                                new_seg = seg[:-4] + '.jpg'
                                #os.remove(seg)
                                shutil.move(os.path.join(img_path, name), os.path.join(img_path,"A", split_name, new_name + ".jpg"))
                                shutil.move(os.path.join(img_path, new_seg), os.path.join(img_path,"B", split_name,  new_name + ".jpg"))

	


def split_files():
	img_path = "ADE20K"
	all_files = os.listdir(img_path)
	split = range(1, 20210+1997+1)
	train, test = train_test_split(split, test_size=0.2)
	test, val = train_test_split(test, test_size=0.2)
	save_split(train, "train")
	save_split(test, "test")
	save_split(val, "val")
	
def clean_dir():
	img_path = "ADE20K"
	for d in os.listdir(img_path):
		if d != "A" and d != "B": 
			os.remove(os.path.join(img_path, d))


if __name__ == "__main__":
	extract_files()
	split_files()
		
				
		
		
