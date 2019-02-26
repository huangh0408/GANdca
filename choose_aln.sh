#!/bin/sh

#cd ~/huangh/bioinfo_hh/PSICOV
for i in $(cat ~/workspace_1_2/pdb_list.txt);do
#	cd ~/huangh/bioinfo_hh/PSICOV
#	./psicov -p -d 0.03 ~/workspace_12_18/feature_ccmpred/${i}.aln >~/workspace_1_2/feature_psicov/${i}.psicov
	cp ~/workspace_12_18/feature_ccmpred/${i}.aln aln_DeepCov
	
done
	
