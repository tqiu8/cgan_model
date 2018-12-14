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
  - `python tools/download-dataset.py rgbd`
  - `python tools/download-dataset.py ADE20k`
  
  
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




