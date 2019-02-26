#!/bin/sh


for i in $(cat ~/workspace_1_2/pdb_list.txt);do
	cd ~/workspace_12_18/feature_ccmpred
	cat ${i}.a3m | sed 's/[a-z]//g'  > ~/huangh/bioinfo_hh/plmDCA/plmDCA_asymmetric_v2/aln_files/${i}.aln
done
	
#cd ~/huangh/bioinfo_hh/plmDCA/plmDCA_asymmetric_v2


	
