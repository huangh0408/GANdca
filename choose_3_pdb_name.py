from numpy import *
import numpy as np
import os,sys

filename="temp_.txt"
f=open(filename,"r")
lines=f.readlines()
L=len(lines)
dic={}
file_pdb=open('./pdb_3_list.txt',"w")
for line in lines:
	list_1=line.split()
	nn=int(list_1[0])
	ff=list_1[1]
	if nn ==3 :
		file_pdb.write(ff)
		file_pdb.write('\n')	
file_pdb.close()
				
