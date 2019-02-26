#! /usr/bin/env python
#################################################################################
#     File Name           :     
#     Created By          :     huangh
#     Creation Date       :     [2018-12-3 16:59]
#     Last Modified       :     []
#     Description         :      
#################################################################################
import yaml, h5py, os, sys
import cPickle
import numpy as np
from scipy.misc import imsave
DTYPE='float32'

def generate_feature(feature_dir,pdb_list,output_filename,feature_ccmpred_dir,flags_dir):
	feature_1d_dir=os.path.join(feature_dir,'feature_1d')
	feature_2d_dir=os.path.join(feature_dir,'feature_2d')
	flag_dir=os.path.join(feature_dir,'true_contact')
	with open(pdb_list,'r') as f:
		dic=[]
		for line in f.readlines():
			line=line.strip('\n')
			hh=line.split(' ')
			dic.append(hh)
	pdb_dict=dict(dic)
	print type(pdb_dict)
#	for j in pdb_dict.keys():
	dict_all={}
	k=0
	for j in range(0,699):
		pdb_name=pdb_dict[str(j)]
		file_1d_name=os.path.join(feature_1d_dir,pdb_name+".txt")
		file_2d_name=os.path.join(feature_2d_dir,pdb_name+".ccmpred")
		file_flag_name=os.path.join(flag_dir,pdb_name+".contact_matrix")
#		with open(file_1d_name) as fin_1d:
		try:
			data_1d=np.loadtxt(open(file_1d_name))
		#with open(file_2d_name) as fin_2d:
        	        data_2d=np.loadtxt(open(file_2d_name))
		#with open(file_flag_name) as fin_flag:
                	data_flag=np.loadtxt(open(file_flag_name))
			a=len(data_1d)
			b=len(data_2d)
			c=len(data_flag)
		except:
			continue
		#k=0
		#dict_all={}
		if a<= 50:
			continue

		if a==b and a==c:
			flags_name=os.path.join(flags_dir,pdb_name+".jpg")
			feature_ccmpred_name=os.path.join(feature_ccmpred_dir,pdb_name+".jpg")
			imsave(flags_name,data_flag)
			imsave(feature_ccmpred_name,data_2d)
	
#			temp={}
#			temp['name']=pdb_name
#			temp['seqLen']=a
#			temp['1d']=data_1d
#			temp['2d']=data_2d.reshape((a,a,1))
#			temp['contactMatrix']=data_flag
#			locals()[pdb_name]=temp
#			dict_all[pdb_name]=temp
#			k=k+1

#	with open(output_filename,'wb') as fout:
#		cPickle.dump(dict_all,fout)
		#k+=1
#	print(k)


if __name__=="__main__":
	feature_dir=sys.argv[1]
	pdb_list=sys.argv[2]
	output_filename=sys.argv[3]
	feature_ccmpred_dir=sys.argv[4]
	flags_dir=sys.argv[5]
	generate_feature(feature_dir,pdb_list,output_filename,feature_ccmpred_dir,flags_dir)
