import numpy as np
import os
import json
from skimage import io
from skimage.transform import resize
from scipy.misc import imsave


def priliminary_checks(flags):
   """Checks the existance of directories and creates them if necessary

   Args:
      flags: Flags
   """
   log_dir = os.path.join(flags.root_dir, 'logs')
   if not os.path.exists(log_dir):
      os.makedirs(log_dir)
   if not os.path.exists(flags.dataset_dir):
      print 'Dataset direcstory not found !\nExiting...'
      exit()
   if not os.path.exists(flags.sample_dir):
      os.makedirs(flags.sample_dir)
   if not os.path.exists(flags.summary_dir):
      os.makedirs(flags.summary_dir)

def create_rundirs(flags, id):
   """Creates the directories for the `id`th run of the model

   Args:
      flags: Flags
      id   : index of the run
   """
   os.makedirs(os.path.join(flags.sample_dir, 'Run_{}'.format(id)))
   os.makedirs(os.path.join(flags.summary_dir, 'Run_{}'.format(id)))
   flags.summary_dir = os.path.join(flags.summary_dir, 'Run_{}'.format(id))
   flags.sample_dir = os.path.join(flags.sample_dir, 'Run_{}'.format(id))

def dump_model_params(flags):
   """Writes model params to a file

   Args:
      flags: Flags
   """
   idx = get_runid(flags)
   # TODO : Add the details of the model

def get_runid(flags):
   """Returns the number of the present run of the model

   Args:
      flags: Flags
   """
   summary_dir = flags.summary_dir
   dirs = os.listdir(summary_dir)
   return len(dirs)+1

def imread(img_path):
   """Reads an image

   Args:
      img_path: Path of the image
   """
   img = io.imread(img_path)
   return img

def imwrite(image_path, images, inv_normalize=False):
   """Writes images to a file

   Args:
      image_path   : Base path for the image
      images       : image data
      inv_normalize: Should inverse normalize the images before
                     writing to the file
   """
   try:
      imsave(image_path+'.png', images)
   except:
      for idx, img in enumerate(images):
         if inv_normalize:
            img = inverse_normalize_images(img)
         imsave(image_path+'_{}.png'.format(idx), img)

def normalize_images(images):
   """Normalizes images into the range [-1, 1]

   Args:
      images: ndarray
   """
   return images / 127.5 - 1.0

def inverse_normalize_images(images):
   """Inverse normalize images

   Args:
      images: ndarray
   """
   return (images + 1.0) / 2.

def path_exists(path):
   """Checks if the path exists

   Args:
      path: path to check
   """
   if os.path.exists(path):
      return True
   return False

def log_config(idx, flags):
   """Writes the initial hyperparameters to a file

   Args:
      idx  : Run index
      flags: Flags to dump
   """
   pass
   #print ' - Dumping hyper parameters to file "logs/config_{}"...'.format(idx)
   #with open(os.path.join('logs/config_{}'.format(idx)), 'w') as fp:
   #   json.dump(flags, fp, indent=4)


def read_file_lines(file_name, split_card=None):
   """Reads the contents of a file line by line

   Args:
      file_name : Name of the file to read
      split_card: Wild char at which to split the line
                  if None, it is not split

   Returns:
      Numpy array of all the lines
   """
   try:
      f = open(file_name, 'r')
   except IOError:
      raise IOError("Cannot open the file {}".format(file_name))
   lines = f.readlines()
   lines = [line.strip() for line in lines]
   if split_card is not None:
      lines = [line.split() for line in lines]
   f.close()
   return np.array(lines)
