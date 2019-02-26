#!/bin/sh

for i in $(cat temp_.txt);do
	num=`echo $i|cut -d ' ' -f 2`
	pdb_name=`echo $i|cut -d ' ' -f 3`
	echo $num
	echo $pdb_name
#	if [ $num -gt 2 ];then
#		echo $pdb_name >>pdb_3_list
#	fi
done
	
