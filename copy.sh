#!/bin/sh

for i in $(cat pdb_3_list_temp.txt);do
	cp 2_chain_flag/${i}* 2_chain_flag_with_DeepCov
done
