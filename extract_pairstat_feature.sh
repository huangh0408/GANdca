#!/bin/sh

#cd ~/huangh/bioinfo_hh/PSICOV
for i in $(cat ~/workspace_1_2/pdb_list.txt);do
#	cd ~/huangh/bioinfo_hh/PSICOV
	pdb_name=`echo $i|cut -d '.' -f 1`	
	~/huangh/bioinfo_hh/metapsicov/bin/alnstats ~/workspace_12_18/feature_ccmpred/${i}.aln ~/workspace_1_2/feature_pairstat/${pdb_name}_single.txt ~/workspace_1_2/feature_pairstat/${pdb_name}_pair.txt
	
done
	
