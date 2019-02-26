#!/bin/sh
#source activate tensorflow2.7
#python generate_train_feature.py /home/huanghe/workspace_12_18/feature/ /home/huanghe/workspace_12_18/pdb_dict.txt train.pkl
python plot_feature.py /home/huanghe/workspace_12_18/feature/ /home/huanghe/workspace_12_18/pdb_dict.txt test.pkl /home/huanghe/workspace_1_2/feature_ccmpred /home/huanghe/workspace_1_2/flags
