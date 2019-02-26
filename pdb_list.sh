#!/bin/sh

for i in $(ls ./image_benchmark_DeepCov);do
	pdb_name=`echo $i|cut -d '_' -f 1`
	echo $pdb_name >>pdb_temp_list.txt
done
cat pdb_temp_list.txt |sort |uniq -d >pdb_benchmark.txt
