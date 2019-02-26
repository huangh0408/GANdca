import numpy as np
from scipy.misc import imsave
import os,sys

def plot(args):
	dir_args=os.path.join('./benchmark_DeepCov_matrix/',args)
	data=np.loadtxt(open(dir_args))
	temp=args.split('.')
        tmp=temp[0]
	image_name=os.path.join('./image_benchmark_DeepCov/',tmp+".jpg")
	imsave(image_name,data)



if __name__=="__main__":
#        args=sys.argv[1]
#        insert=sys.argv[2]
 #       m=sys.argv[3]
#       n=sys.argv[4]
#       p=sys.argv[5]
        for filename in os.listdir('./benchmark_DeepCov_matrix'):
                args=filename
                plot(args)

