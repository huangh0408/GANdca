from numpy import *
import numpy as np
import os,sys
def convert(args):
	dir_args=os.path.join('/home/huanghe/huangh/Bioinfo_clone/DeepCov/result_PDB_benchmark_alignments/',args)
	f=open(dir_args,"r")
	lines=f.readlines()
#	s=len(lines)
#	s=s+1
	temp=args.split('.')
	tmp=temp[0]
#	temp2=args.split('_')
#	tmp2=temp2[0]
#	tmp3=temp2[1]
	ccmpred_name=os.path.join('/home/huanghe/huangh/Bioinfo_clone/DeepCov/result_ccmpred_benchmark/',tmp+'.ccmpred')
	ccmpred_data=np.loadtxt(open(ccmpred_name))
	s=len(ccmpred_data)
#	s=401
	M=zeros((s,s))
	m=0
	n=1
	p=4
	for line in lines:
		#if insert==0:
		#	list_1=line.split(',')
		#else:
		list_1=line.split()
		xx=int(list_1[m])-1
		yy=int(list_1[n])-1
		M[xx][yy]=float(list_1[p])	
		M[yy][xx]=float(list_1[p])
#	temp=args.split('.')
#	tmp=temp[0]
	name=os.path.join('./benchmark_DeepCov_matrix/',tmp+'.matrix')
	np.savetxt(name,M)

if __name__=="__main__":
#        args=sys.argv[1]
#        insert=sys.argv[2]
 #       m=sys.argv[3]
#	n=sys.argv[4]
#	p=sys.argv[5]
	for filename in os.listdir('/home/huanghe/huangh/Bioinfo_clone/DeepCov/result_ccmpred_benchmark/'):
		ss=filename
		sss=ss.split('.')
		ssss=sss[0]
		args=os.path.join(ssss+'.con')
#		args=filename
	        convert(args)
