#!/bin/sh

module load anaconda3
source $ANACONDA3_SH

# Activate the base environment
conda activate /nics/b/home/hzhan101/py3_env

# Run assignment1.py
python assignment1.py
