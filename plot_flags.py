with open(pdb_list,'r') as f:
	dic=[]
	for line in f.readlines():
		line=line.strip('\n')
		hh=line.split(' ')
		dic.append(hh)
pdb_dict=dict(dic)
for j in range(0,600):
	pdb_name=pdb_dict[str(j)]
	file_1d_name=os.path.join(feature_1d_dir,pdb_name+".txt")
        file_2d_name=os.path.join(feature_2d_dir,pdb_name+".ccmpred")
        file_flag_name=os.path.join(flag_dir,pdb_name+".contact_matrix")
#               with open(file_1d_name) as fin_1d:
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

