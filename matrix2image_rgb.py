import numpy as np
from scipy.misc import imsave
import os,sys

def plot(args):
	temp=args.split('.')
        tmp=temp[0]
	dir_DeepCov=os.path.join('./matrix_DeepCov/',tmp+'.matrix')
	data_DeepCov=np.loadtxt(open(dir_DeepCov))
#	dir_pairstat=os.path.join('./matrix_pairstat/',tmp+'_pair.matrix')
#        data_pairstat=np.loadtxt(open(dir_pairstat))
	dir_ccmpred=os.path.join('./matrix_ccmpred/',tmp+'.ccmpred')
        data_ccmpred=np.loadtxt(open(dir_ccmpred))
	r=len(data_DeepCov)
#	g=len(data_pairstat)
	b=len(data_ccmpred)
#	if r==g and r==b:
	if r==b:
#		data=np.random.random((r,r,3))
#		data[0]=data_DeepCov
#		data[1]=data_pairstat
#		data[2]=data_ccmpred
		rr=np.reshape(data_DeepCov,(r,r,1))
#		gg=np.reshape(data_pairstat,(r,r,1))
		gg=np.reshape(data_ccmpred,(r,r,1))
		bb=np.reshape(data_ccmpred,(r,r,1))
		data=np.concatenate((rr,gg,bb),axis=-1)
		image_name=os.path.join('./image_ccmpred_DeepCov/',tmp+".jpg")
		imsave(image_name,data)



if __name__=="__main__":
#        args=sys.argv[1]
#        insert=sys.argv[2]
 #       m=sys.argv[3]
#       n=sys.argv[4]
#       p=sys.argv[5]
        for filename in os.listdir('./flags'):
                args=filename
                plot(args)

