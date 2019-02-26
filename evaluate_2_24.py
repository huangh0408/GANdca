#!/usr/bin/env python
import numpy as np
import os
from utils.acc_cal_v2 import topKaccuracy, evaluate, output_result
from PIL import Image
#import numpy as np
import matplotlib.pyplot as plt
import scipy.misc as misc

#def evaluate_tmp(predict_matrix,ccmpred_matrix,contact_matrix):
#input_acc=[]
output_acc=[]
DeepCov_acc=[]
psicov_acc=[]
ccmpred_acc=[]
j=0
output_dir='./hh_2_24/images/'
for filename in os.listdir('./workspace_2_21/cm_DeepCov_flag/train'):
	temp=filename.split('.')
	name=temp[0]
	fasta_file=os.path.join('/home/huanghe/workspace_1_2/feature_2_21/feature_contact_matrix/ccmpred',name+'.ccmpred')
	temp_matrix=np.loadtxt(fasta_file)
	ccmpred_matrix=temp_matrix
	L=temp_matrix.shape[1]
	ccmpred_matrix_name=fasta_file
	DeepCov_matrix_name=os.path.join('/home/huanghe/workspace_1_2/feature_2_21/feature_contact_matrix/DeepCov',name+'.matrix')
	psicov_matrix_name=os.path.join('/home/huanghe/workspace_1_2/feature_2_21/feature_contact_matrix/psicov',name+'.matrix')
	contact_matrix_name=os.path.join('/home/huanghe/workspace_1_2/flag_2_21/flag_contact_matrix',name+'.matrix')
	predict_matrix_file=os.path.join(output_dir,name+'-outputs.png')
#	ccmpred_matrix=os.path.join('./TEST.1.7/images/',name+'-inputs.png')
#	contact_matrix_file=os.path.join('./hh_2_21_1/images/',name+'-targets.png')
	predict_matrix_file_gray=Image.open(predict_matrix_file).convert('L')
	predict_matrix_file_temp=misc.imresize(predict_matrix_file_gray,[L,L],interp='nearest')
#	contact_matrix_file_temp=misc.imresize(contact_matrix_file,[L,L],interp='nearest')
#	contact_matrix_file_temp
#	im1=Image.open(predict_matrix_file_temp)
#	im1=predict_matrix_file_temp
#	im2=Image.open(contact_matrix_file_temp)
	predict_matrix=np.array(predict_matrix_file_temp)
#	contact_matrix=np.array(im2)
	contact_matrix=np.loadtxt(contact_matrix_name)
	DeepCov_matrix=np.loadtxt(DeepCov_matrix_name)
	psicov_matrix=np.loadtxt(psicov_matrix_name)
	DeepCov_acc.append(evaluate(DeepCov_matrix, contact_matrix))
	psicov_acc.append(evaluate(psicov_matrix, contact_matrix))
	ccmpred_acc.append(evaluate(ccmpred_matrix, contact_matrix))
#	input_acc.append(evaluate(_matrix, contact_matrix))
	output_acc.append(evaluate(predict_matrix,contact_matrix))
	print "\n"
	print "*"*50
	print "\nAcc result:%s" %name
	print "*"*50
	print "\nccmpred result accuracy:" 
        output_result(ccmpred_acc[j])
	print "\npsicov result accuracy:"
        output_result(psicov_acc[j])
	print "\nDeepCov result accuracy:"
        output_result(DeepCov_acc[j])
        print "\nOutput result accuracy:" 
        output_result(output_acc[j])
#	print "\nDeepCov result:"
#        output_result(DeepCov_acc[j])
        j+=1

#print "Input result:"
#output_result(np.mean(np.array(input_acc), axis=0))
print "\n"*5
print "*"*50
print "\nccmpred total result:"
#print "*"*50
output_result(np.mean(np.array(ccmpred_acc), axis=0))
print "\n"*5
print "*"*50
print "\nDeepCov total result:"
output_result(np.mean(np.array(DeepCov_acc), axis=0))
print "\n"*5
print "*"*50
print "\npsicov total result:"
output_result(np.mean(np.array(psicov_acc), axis=0))
print "\n"*5
print "*"*50
print "\noutput total result:"
output_result(np.mean(np.array(output_acc), axis=0))
