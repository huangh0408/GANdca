#!/bin/sh
python concatenate_matrix_feature_no_random.py
python3 tools/process.py --operation resize --size 512 --input_dir 2_chain_feature_no_random/ --output_dir 2_chain_feature_no_random_resize
#python3 tools/process.py --operation resize --size 512 --input_dir 2_chain_flag/ --output_dir 2_chain_flag_resize
python3 tools/process.py --operation combine --input_dir 2_chain_feature_no_random_resize/ --b_dir 2_chain_flag_resize/ --output_dir cm_2_chain_1_16
python3 tools/split.py --dir cm_2_chain_1_16
python3 wpix2pix.py --mode train --input_dir cm_2_chain_1_16/train/ --output_dir OUT.1.16 --batch_size 1 --max_epochs 100
python3 wpix2pix.py --mode test --input_dir cm_2_chain_1_16/val/ --output_dir hh_1_16 --checkpoint OUT.1.16
