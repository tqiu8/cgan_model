# Image-Image Translation with cGANs
EC500/CS591 Final Project
John Curci, Tammy Qiu, Zahid Hasan

A project comparing the performances of pix2pix, BicycleGAN, pix2pix WGAN, VAE GAN, VAE WGAN, and Bicycle WGAN


## Instructions for use:
### To download datasets:
  - `python tools/download-dataset.py facades`
  - `python tools/download-dataset.py cityscapes`
  - `python tools/download-dataset.py maps`
  - `python tools/download-dataset.py edges2shoes`
  - `python tools/download-dataset.py edges2bags`  
  
 ### To run the models:
 
You must first be logged onto the SCC. These models will run on the facades dataset by default. Please make sure you have downloaded the facades dataset before running the models. 

To run Bicycle WGAN and VAE WGAN:
 
 From the main directory: `cd Bicycle_WGAN`
 
Bicycle WGAN: either submit a batch job as: `qsub qsub_bicycle_WGAN_facades.sh` or in an interactive GPU session run: `source qsub_bicycle_WGAN_facades.sh`

VAE GAN: `qsub qsub_vae_WGAN_facades.sh` or in an interactive GPU session run: `source qsub_vae_WGAN_facades.sh`

To run pix2pix WGAN and pix2pix:

From the main directory: `cd pix2pix`

pix2pix: either submit a batch job as: `qsub qsub_p2p_master_no_WGAN.sh` or in an interactive GPU session run: `source qsub_p2p_master_no_WGAN.sh`

pix2pix WGAN: either submit a batch job as: `qsub qsub_p2p_master_WGAN.sh` or in an interactive GPU session run: `source qsub_p2p_master_WGAN.sh`

### To use a different dataset:

In the bash files, change the `--input_dir` to wherever the training examples of your dataset are located. 

### Directory structure:
```
Bicycle_WGAN\
  utils\
    __init__.py   #constructor for datasets
    utils.py    #helper functions
   nnet\
    __init__broken vae.py   #constructor for graphs of model
    __init__.py   #constructor for graphs of model
    __init__working_WGAN.py   #constructor for graphs of wgan model
   config.py    #contains hyperparameters of models
   main.py    #main training script
   setup.py   #bibliographic information of model
   setup_dataset.h    #bash script that performs additional preprocessing to datasets
   requirements.txt     #module requirements for the code
   qsub_vae_WGAN_facades.sh     #bash script for running VAE GAN on facades dataset
   qsub_bicycle_WGAN_facades.sh     #bash script for running bicycle WGAN on facades dataset
pix2pix\
  pix2pix.py    #original pix2pix model
  pix2pix_WGAN.py   #modified pix2pixWGAN model
  qsub_p2p_master_WGAN.sh   #bash script for running pix2pix WGAN on facades
  qsub_p2p_master_no_WGAN.sh    #bash script for running vanilla pix2pix on facades
tools\
  download-dataset.py   #script for downloading datasets
  process.py            #helper functions
  split.py              #splits into train, test, and val sets
  test.py               #tests model
  tfimage.py            #tensorflow functions for image processing
utils\
  preprocess.py         #re-organize and extract ADE20K dataset
  combine_A_and_B.py    #pairs images for training
```

## Acknowledgements:
We used code from: https://github.com/affinelayer/pix2pix-tensorflow for our pix2pix implementation. 

https://github.com/kvmanohar22/img2imgGAN for BicycleGAN.




