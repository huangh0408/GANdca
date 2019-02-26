#!/bin/sh
#python concatenate_matrix_feature_no_random.py
python3 tools/process.py --operation resize --size 512 --input_dir 2_chain_feature_with_DeepCov/ --output_dir 2_chain_feature_with_DeepCov_resize
python3 tools/process.py --operation resize --size 512 --input_dir 2_chain_flag_with_DeepCov/ --output_dir 2_chain_flag_with_DeepCov_resize
python3 tools/process.py --operation combine --input_dir 2_chain_feature_with_DeepCov_resize/ --b_dir 2_chain_flag_with_DeepCov_resize/ --output_dir cm_2_chain_1_17
python3 tools/split.py --dir cm_2_chain_1_17
python3 wpix2pix.py --mode train --input_dir cm_2_chain_1_17/train/ --output_dir OUT.1.17 --batch_size 1 --max_epochs 100
python3 wpix2pix.py --mode test --input_dir cm_2_chain_1_17/val/ --output_dir hh_1_17 --checkpoint OUT.1.17
