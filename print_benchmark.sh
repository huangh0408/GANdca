#!/bin/sh

for i in $(cat pdb_benchmark.txt);do
	printf $i
	printf ","
done
