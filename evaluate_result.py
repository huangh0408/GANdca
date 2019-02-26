#!/usr/bin/env python
import numpy as np
import os
from utils.acc_cal_v2 import topKaccuracy, evaluate, output_result
from PIL import Image
#import numpy as np
import matplotlib.pyplot as plt
import scipy.misc as misc

#def evaluate_tmp(predict_matrix,ccmpred_matrix,contact_matrix):
input_acc=[]
output_acc=[]
DeepCov_acc=[]
j=0
for filename in os.listdir('./reCMB/val'):
	temp=filename.split('.')
	name=temp[0]
	fasta_file=os.path.join('./matrix_ccmpred/',name+'.ccmpred')
	temp_matrix=np.loadtxt(fasta_file)
	ccmpred_matrix=temp_matrix
	L=temp_matrix.shape[1]
	DeepCov_matrix_name=os.path.join('./matrix_DeepCov/',name+'.matrix')
	contact_matrix_name=os.path.join('../workspace_12_18/flags/',name+'.contact_matrix')
	predict_matrix_file=os.path.join('./TEST.1.7/images/',name+'-outputs.png')
#	ccmpred_matrix=os.path.join('./TEST.1.7/images/',name+'-inputs.png')
	contact_matrix_file=os.path.join('./TEST.1.7/images/',name+'-targets.png')
	predict_matrix_file_gray=Image.open(predict_matrix_file).convert('L')
	predict_matrix_file_temp=misc.imresize(predict_matrix_file_gray,[L,L],interp='nearest')
#	contact_matrix_file_temp=misc.imresize(contact_matrix_file,[L,L],interp='nearest')
#	contact_matrix_file_temp
#	im1=Image.open(predict_matrix_file_temp)
	im1=predict_matrix_file_temp
#	im2=Image.open(contact_matrix_file_temp)
	predict_matrix=np.array(im1)
#	contact_matrix=np.array(im2)
	contact_matrix=np.loadtxt(contact_matrix_name)
	DeepCov_matrix=np.loadtxt(DeepCov_matrix_name)
	DeepCov_acc.append(evaluate(DeepCov_matrix, contact_matrix))
	input_acc.append(evaluate(ccmpred_matrix, contact_matrix))
        output_acc.append(evaluate(predict_matrix, contact_matrix))
	print "\n"
	print "*"*50
	print "\nAcc result:%s" %name
	print "*"*50
	print "\nInput result:" 
        output_result(input_acc[j])
        print "\nOutput result:" 
        output_result(output_acc[j])
	print "\nDeepCov result:"
        output_result(DeepCov_acc[j])
        j+=1

#print "Input result:"
#output_result(np.mean(np.array(input_acc), axis=0))
print "\n"*5
print "*"*50
print "\ninput total result:"
#print "*"*50
output_result(np.mean(np.array(input_acc), axis=0))
print "\n"*5
print "*"*50
print "\nOutput total result:"
output_result(np.mean(np.array(output_acc), axis=0))
print "\n"*5
print "*"*50
print "\nOutput total result:"
output_result(np.mean(np.array(DeepCov_acc), axis=0))
