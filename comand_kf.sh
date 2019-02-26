#!/bin/sh

python3 wpix2pix.py --mode train --input_dir CM_IDF/train/ --output_dir OUT.1.11 --batch_size 1 --max_epochs 100

python3 wpix2pix.py --mode test --input_dir reCMB/val/ --output_dir hh_1_11 --checkpoint OUT.1.7

 python3 tools/process.py --operation resize --size 256 --input_dir image_DeepCov/ --output_dir RE_ID

python3 tools/process.py --operation combine --input_dir RE_ID/ --b_dir RE_flages/ --output_dir CM_IDF

python3 tools/split.py --dir CM_IDF/
