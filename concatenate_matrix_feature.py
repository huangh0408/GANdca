from __future__ import division
import numpy as np
from scipy.misc import imsave
import os,sys
#from __future__ import division

def plot(a):
	pdb_name_file="pdb_3_list.txt"
	f=open(pdb_name_file,"r")
#	lines=f.readline()
	for line in f:
		temp=line.split()
		pdb_name=temp[0]
		chain_file_name=os.path.join('/home/huanghe/huangh/bioinfo_hh/Complex_Tool/chain/',pdb_name+'.rsa_chain.txt')
		ff=open(chain_file_name,"r")
#		chains=ff.readline()
		p=1
		chain_dic={}
		for chain in ff:
			temp=chain.split()
			chain_dic[p]=temp[0]
			p=p+1
		chain_A=chain_dic[1]
		chain_B=chain_dic[2]
		chain_C=chain_dic[3]
		matrix_A_name=os.path.join('/home/huanghe/workspace_12_18/flags/',pdb_name+'_'+chain_A+'.contact_matrix')
		matrix_B_name=os.path.join('/home/huanghe/workspace_12_18/flags/',pdb_name+'_'+chain_B+'.contact_matrix')
		matrix_C_name=os.path.join('/home/huanghe/workspace_12_18/flags/',pdb_name+'_'+chain_C+'.contact_matrix')
		matrix_A_B_name=os.path.join('/home/huanghe/huangh/bioinfo_hh/Complex_Tool/contact_1_14/',pdb_name+'_'+chain_A+'_'+chain_B+'.contact_matrix')
		matrix_A_C_name=os.path.join('/home/huanghe/huangh/bioinfo_hh/Complex_Tool/contact_1_14/',pdb_name+'_'+chain_A+'_'+chain_C+'.contact_matrix')
		matrix_B_C_name=os.path.join('/home/huanghe/huangh/bioinfo_hh/Complex_Tool/contact_1_14/',pdb_name+'_'+chain_B+'_'+chain_C+'.contact_matrix')
		matrix_A=np.loadtxt(matrix_A_name)
		matrix_B=np.loadtxt(matrix_B_name)
		matrix_C=np.loadtxt(matrix_C_name)
		matrix_A_B=np.loadtxt(matrix_A_B_name)
		matrix_A_C=np.loadtxt(matrix_A_C_name)
		matrix_B_C=np.loadtxt(matrix_B_C_name)
		sum_A_B=matrix_A_B.sum()
		sum_A_C=matrix_A_C.sum()
		sum_B_C=matrix_B_C.sum()
		matrix_B_A=np.transpose(matrix_A_B)
		matrix_C_A=np.transpose(matrix_A_C)
		matrix_C_B=np.transpose(matrix_B_C)
		
		l_A=len(matrix_A)
		l_B=len(matrix_B)
		l_C=len(matrix_C)
		l_A_1=matrix_A_B.shape[0]
		l_A_2=matrix_A_C.shape[0]
		l_B_1=matrix_B_C.shape[0]
		l_B_2=matrix_A_B.shape[1]
		l_C_1=matrix_A_C.shape[1]
		l_C_2=matrix_B_C.shape[1]
		ratio_A=sum_A_B/l_A+sum_A_C/l_A
		ratio_B=sum_A_B/l_B+sum_B_C/l_B
		ratio_C=sum_A_C/l_C+sum_B_C/l_C
		if l_A == l_A_1 and l_A == l_A_2 and ratio_A>0.05:
			if l_B == l_B_1 and l_B == l_B_2 and ratio_B>0.05:
				if l_C == l_C_1 and l_C == l_C_2 and ratio_C>0.05:
					random_A_B=np.random.random((l_A,l_B))
					random_B_A=np.transpose(random_A_B)
					M1=np.hstack((matrix_A,random_A_B))
					M2=np.hstack((random_B_A,matrix_B))
					L1=np.hstack((matrix_A,matrix_A_B))
					L2=np.hstack((matrix_B_A,matrix_B))
					feature_A_B=np.vstack((M1,M2))
					flag_A_B=np.vstack((L1,L2))
					feature_A_B_name=os.path.join('./2_chain_feature/',pdb_name+'_'+chain_A+'_'+chain_B+'.jpg')
					imsave(feature_A_B_name,feature_A_B)
					flag_A_B_name=os.path.join('./2_chain_flag/',pdb_name+'_'+chain_A+'_'+chain_B+'.jpg')
			                imsave(flag_A_B_name,flag_A_B)
		
					random_A_C=np.random.random((l_A,l_C))
			                random_C_A=np.transpose(random_A_C)
			                M1=np.hstack((matrix_A,random_A_C))
			                M2=np.hstack((random_C_A,matrix_C))
			                L1=np.hstack((matrix_A,matrix_A_C))
			                L2=np.hstack((matrix_C_A,matrix_C))
			                feature_A_C=np.vstack((M1,M2))
			                flag_A_C=np.vstack((L1,L2))
			                feature_A_C_name=os.path.join('./2_chain_feature/',pdb_name+'_'+chain_A+'_'+chain_C+'.jpg')
			                imsave(feature_A_C_name,feature_A_C)
			                flag_A_C_name=os.path.join('./2_chain_flag/',pdb_name+'_'+chain_A+'_'+chain_C+'.jpg')
			                imsave(flag_A_C_name,flag_A_C)		
	
					random_B_C=np.random.random((l_B,l_C))
			                random_C_B=np.transpose(random_B_C)
			                M1=np.hstack((matrix_B,random_B_C))
			                M2=np.hstack((random_C_B,matrix_C))
			                L1=np.hstack((matrix_B,matrix_B_C))
			                L2=np.hstack((matrix_C_B,matrix_C))
			                feature_B_C=np.vstack((M1,M2))
			                flag_B_C=np.vstack((L1,L2))
			                feature_B_C_name=os.path.join('./2_chain_feature/',pdb_name+'_'+chain_B+'_'+chain_C+'.jpg')
			                imsave(feature_B_C_name,feature_B_C)
			                flag_B_C_name=os.path.join('./2_chain_flag/',pdb_name+'_'+chain_B+'_'+chain_C+'.jpg')
			                imsave(flag_B_C_name,flag_B_C)
#	temp=args.split('.')
 #       tmp=temp[0]
#	dir_DeepCov=os.path.join('./matrix_DeepCov/',tmp+'.matrix')
#	data_DeepCov=np.loadtxt(open(dir_DeepCov))
#	dir_pairstat=os.path.join('./matrix_pairstat/',tmp+'_pair.matrix')
#        data_pairstat=np.loadtxt(open(dir_pairstat))
#	dir_ccmpred=os.path.join('./matrix_ccmpred/',tmp+'.ccmpred')
 #       data_ccmpred=np.loadtxt(open(dir_ccmpred))
#	r=len(data_DeepCov)
#	g=len(data_pairstat)
#	b=len(data_ccmpred)
#	if r==g and r==b:
#	if r==b:
#		data=np.random.random((r,r,3))
#		data[0]=data_DeepCov
#		data[1]=data_pairstat
#		data[2]=data_ccmpred
#		rr=np.reshape(data_DeepCov,(r,r,1))
#		


if __name__=="__main__":
	
	a=1
	plot(a)
#        args=sys.argv[1]
#        insert=sys.argv[2]
 #       m=sys.argv[3]
#       n=sys.argv[4]
#       p=sys.argv[5]
  #      for filename in os.listdir('./flags'):
 #               args=filename
#plot()

