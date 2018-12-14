from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

try:
    from urllib.request import urlopen # python 3
except ImportError:
    from urllib2 import urlopen # python 2
import sys
import tarfile
import tempfile
import shutil

dataset = sys.argv[1]
if dataset == "rgbd":
    url = "https://drive.google.com/uc?export=download&id=1b3edhz-jq0rRlLLKZH9UyeGAfoe09jb4"
elif dataset == "ade20k":
    url = "https://drive.google.com/uc?export=download&id=1TDsySv_WP9apfCmiUFwwOckCsFqG8mF9"
else:
    url = "https://people.eecs.berkeley.edu/~tinghuiz/projects/pix2pix/datasets/%s.tar.gz" % dataset

with tempfile.TemporaryFile() as tmp:
    print("downloading", url)
    shutil.copyfileobj(urlopen(url), tmp)
    print("extracting")
    tmp.seek(0)
    tar = tarfile.open(fileobj=tmp)
    tar.extractall()
    tar.close()
    shutil.move("%s/" % dataset, "../data/%s/" %dataset)
    print("done")
