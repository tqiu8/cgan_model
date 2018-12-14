#!/bin/bash -l
#$ -P dl-course
#$ -N vae_WGAN_facades
#$ -j y
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
module load tensorflow/r1.3

bash setup_dataset.sh

python main.py --train \
--model cvae-gan \
--direction b2a \
--dataset facades \
--niter 500 \
--niter_decay 500 \
--ckpt_frq 50 \
--gen_frq 1000 \
--sample_dir ../results/vae_WGAN_facades/sample \
--summary_dir ../results/vae_WGAN_facades/summary

sleep 10
echo "==============================================="
echo "Finished on : $(date)"
echo "========= ============================================"
