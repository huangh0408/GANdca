#!/bin/sh
#python concatenate_matrix_feature_no_random.py
python3 tools/process.py --operation resize --size 256 --input_dir feature_2_21/feature_contact_image/ccmpred --output_dir workspace_2_21/ccmpred_resize
#python3 tools/process.py --operation resize --size 256 --input_dir flag_2_21/flag_contact_image --output_dir workspace_2_21/flag_resize
python3 tools/process.py --operation combine --input_dir workspace_2_21/ccmpred_resize --b_dir workspace_2_21/flag_resize --output_dir workspace_2_21/cm_ccmpred_flag
python3 tools/split.py --dir workspace_2_21/cm_ccmpred_flag
python3 wpix2pix.py --mode train --input_dir workspace_2_21/cm_ccmpred_flag/train/ --output_dir OUT.2.21.2 --batch_size 1 --max_epochs 100
python3 wpix2pix.py --mode test --input_dir workspace_2_21/cm_ccmpred_flag/val/ --output_dir hh_2_21_2 --checkpoint OUT.2.21.2
