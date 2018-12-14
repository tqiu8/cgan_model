#!/bin/bash -l
#$ -P dl-course
#$ -N p2p_no_WGAN_facades
#$ -j n
#$ -m bae
#$ -M jcurci92@gmail.com
#$ -V
#$ -pe omp 2
#$ -l gpus=0.5
#$ -l gpu_c=3.5  
#$ -l h_rt=48:00:00

echo "==============================================="
echo "Starting on : $(date)"
echo "Running on node : $(hostname)"
echo "Current directory : $(pwd)"
echo "Current job ID : $JOB_ID"
echo "Current job name : $JOB_NAME"
echo "==============================================="

module purge
module load python/2.7.13
module load cuda/8.0
module load cudnn/6.0
module load tensorflow/r1.4

python pix2pix.py \
  --mode train \
  --output_dir ../results/p2p_no_WGAN_facades \
  --max_epochs 50 \
  --input_dir ../data/facades/train \
  --which_direction BtoA
  
python pix2pix.py \
  --mode test \
  --output_dir ../results/p2p_no_WGAN_facades/1/ \
  --input_dir ../data/facades/val \
  --checkpoint ../results/p2p_no_WGAN_facades

python pix2pix.py \
  --mode test \
  --output_dir ../results/p2p_no_WGAN_facades/2/ \
  --input_dir ../data/facades/val \
  --checkpoint ../results/p2p_no_WGAN_facades

python pix2pix.py \
  --mode test \
  --output_dir ../results/p2p_no_WGAN_facades/3/ \
  --input_dir ../data/facades/val \
  --checkpoint ../results/p2p_no_WGAN_facades

python pix2pix.py \
  --mode test \
  --output_dir ../results/p2p_no_WGAN_facades/4/ \
  --input_dir ../data/facades/val \
  --checkpoint ../results/p2p_no_WGAN_facades

python pix2pix.py \
  --mode test \
  --output_dir ../results/p2p_no_WGAN_facades/5/ \
  --input_dir ../data/facades/val \
  --checkpoint ../results/p2p_no_WGAN_facades

sleep 10
echo "==============================================="
echo "Finished on : $(date)"
echo "========= ============================================"
