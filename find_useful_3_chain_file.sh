#!/bin/sh

for i in $(cat pdb_list.txt);do
	pdb_name=`echo $i|cut -d '_' -f 1`
	echo $pdb_name >>temp.txt
done
	
