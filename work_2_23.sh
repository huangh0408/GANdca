#!/bin/sh
#python concatenate_matrix_feature_no_random.py
#python3 tools/process.py --operation resize --size 256 --input_dir feature_2_23 --output_dir workspace_2_23/DeepCov_resize
#python3 tools/process.py --operation resize --size 256 --input_dir flag_2_23 --output_dir workspace_2_23/flag_resize
#python3 tools/process.py --operation combine --input_dir workspace_2_23/DeepCov_resize --b_dir workspace_2_23/flag_resize --output_dir workspace_2_23/cm_DeepCov_flag
#python3 tools/split.py --dir workspace_2_23/cm_DeepCov_flag
python3 wpix2pix.py --mode train --input_dir workspace_2_23/cm_DeepCov_flag/train/ --output_dir OUT.2.23 --batch_size 1 --max_epochs 100
python3 wpix2pix.py --mode test --input_dir workspace_2_23/cm_DeepCov_flag/val/ --output_dir hh_2_23 --checkpoint OUT.2.23
