#!/bin/sh
#python3 tools/process.py --operation resize --size 512 --input_dir 2_chain_feature/ --output_dir 2_chain_feature_resize
#python3 tools/process.py --operation resize --size 512 --input_dir 2_chain_flag/ --output_dir 2_chain_flag_resize
#python3 tools/process.py --operation combine --input_dir 2_chain_feature_resize/ --b_dir 2_chain_flag_resize/ --output_dir cm_2_chain_1_14
python3 tools/split.py --dir cm_2_chain_1_14
python3 wpix2pix.py --mode train --input_dir cm_2_chain_1_14/train/ --output_dir OUT.1.14 --batch_size 1 --max_epochs 100
python3 wpix2pix.py --mode test --input_dir cm_2_chain_1_14/val/ --output_dir hh_1_14 --checkpoint OUT.1.14
