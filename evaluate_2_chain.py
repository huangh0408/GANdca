#!/usr/bin/env python
import numpy as np
import os
from utils.acc_cal_v2 import topKaccuracy, evaluate, output_result
from utils.acc_cal_for_interaction import topKaccuracy_temp, evaluate_temp, output_result_temp
from PIL import Image
#import numpy as np
import matplotlib.pyplot as plt
import scipy.misc as misc

#def evaluate_tmp(predict_matrix,ccmpred_matrix,contact_matrix):
input_acc=[]
output_acc=[]
sub_acc=[]
j=0
for filename in os.listdir('./cm_2_chain_1_17/val'):
	temp=filename.split('.')
	name=temp[0]
#	fasta_file=os.path.join('./2_chain_feature/',name+'.jpg')
#	temp_matrix=np.loadtxt(fasta_file)
#	ccmpred_matrix=temp_matrix
#	L=temp_matrix.shape[1]
	DeepCov_matrix_name=os.path.join('./2_chain_DeepCov/',name+'.matrix')
#	contact_matrix_name=os.path.join('../workspace_12_18/flags/',name+'.contact_matrix')
	sub_temp_matrix_file=os.path.join('/home/huanghe/huangh/bioinfo_hh/Complex_Tool/contact_1_14/',name+'.contact_matrix')
	temp_matrix_file=os.path.join('/home/huanghe/workspace_1_2/2_chain_flag_matrix/',name+'.txt')
	
	predict_matrix_file=os.path.join('./hh_1_17/images/',name+'-outputs.png')
#	ccmpred_matrix=os.path.join('./TEST.1.7/images/',name+'-inputs.png')
#	contact_matrix_file=os.path.join('./hh_1_14/images/',name+'-targets.png')
	predict_matrix_file_gray=Image.open(predict_matrix_file).convert('L')
#	contact_matrix_file_gray=Image.open(contact_matrix_file).convert('L')
#	temp_matrix_file_gray=Image.open(temp_matrix_file)
#	im3=temp_matrix_file_gray
	temp_matrix=np.loadtxt(temp_matrix_file)
	DeepCov_matrix_temp=np.loadtxt(DeepCov_matrix_name)
	L=temp_matrix.shape[0]
	sub_temp_matrix=np.loadtxt(sub_temp_matrix_file)
        l_A=sub_temp_matrix.shape[0]
        l_B=sub_temp_matrix.shape[1]
#	L=l_A+l_B
	predict_matrix_file_temp=misc.imresize(predict_matrix_file_gray,[L,L],interp='nearest')
#	contact_matrix_file_temp=misc.imresize(contact_matrix_file,[L,L],interp='nearest')
#	contact_matrix_file_temp
#	im1=Image.open(predict_matrix_file_temp)
	im1=predict_matrix_file_temp
#	im2=contact_matrix_file_gray
#	im2=im3
#	im3=temp_matrix_file_gray
#	im2=Image.open(contact_matrix_file_temp)
	predict_matrix=np.array(im1)
	range_1=range(0,l_A)
	range_2=range(l_A,L)
	tempp=predict_matrix[range_1]
	temppp=DeepCov_matrix_temp[range_1]
	sub_predict_A_B_matrix=tempp[:,range_2]
	DeepCov_matrix=temppp[:,range_2]
	predict_A_B_matrix=predict_matrix
	contact_matrix=temp_matrix
#	temp_matrix=np.array(im3)
#	l_A=temp_matrix.shape[0]
#	l_B=temp_matrix.shape[1]
#	contact_matrix=np.array(im2)
#	contact_matrix=np.loadtxt(contact_matrix_name)
#	DeepCov_matrix=np.loadtxt(DeepCov_matrix_name)
#	DeepCov_acc.append(evaluate(DeepCov_matrix, contact_matrix))
	input_acc.append(evaluate_temp(DeepCov_matrix, sub_temp_matrix))
	sub_acc.append(evaluate_temp(sub_predict_A_B_matrix, sub_temp_matrix))
        output_acc.append(evaluate(predict_matrix, contact_matrix))
	print "\n"
	print "*"*50
	print "\nAcc result:%s" %name
	print "*"*50
	print "\ninteraction result:" 
        output_result_temp(sub_acc[j])
        print "\ncontact result:" 
        output_result(output_acc[j])
	print "\nDeepCov result:"
        output_result_temp(input_acc[j])
        j+=1

print "\n"*5
print "*"*50
print "Input total result:"
output_result_temp(np.mean(np.array(input_acc), axis=0))
print "\n"*5
print "*"*50
print "\nimteraction total result:"
print "*"*50
output_result_temp(np.mean(np.array(sub_acc), axis=0))
print "\n"*5
print "*"*50
print "\ncontact total result:"
output_result(np.mean(np.array(output_acc), axis=0))
#print "\n"*5
#print "*"*50
#print "\nDeepCov total result:"
#output_result(np.mean(np.array(DeepCov_acc), axis=0))
