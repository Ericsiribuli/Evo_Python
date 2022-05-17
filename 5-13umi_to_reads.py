from sys import argv
import re
import numpy as np
#5-13把二代对应到三代里找到相应的geno

input_ccs_3rd,input_2nd,out_reads= argv[1:]

input_3rd = open(input_ccs_3rd,"r")
out = open(out_reads,"w")

ccs_dict = {}
for every in input_3rd:
    if len(every)>40:
        geno = every.strip().split(" ")[0].split("_")[1]
        umi = every.strip().split(" ")[1]
        if umi in ccs_dict:
            ccs_dict[umi].append(geno)
        else:
            ccs_dict[umi] = [geno]

umi_geno_my_dict = {}
for umi_myy in ccs_dict:
    if len(np.unique(ccs_dict[umi_myy]))==1:
        geno_myy = "".join(np.unique(ccs_dict[umi_myy]))
        umi_geno_my_dict[umi_myy] = geno_myy

len_dict_num = len(umi_geno_my_dict)

noexit_num = 0
with open(input_2nd,"r") as umi_2rd:
    for every_umi in umi_2rd:
        every_umi = every_umi.strip()
        if every_umi in umi_geno_my_dict.keys():
            geno_2rd = umi_geno_my_dict[every_umi]
            out.write(every_umi + "," + geno_2rd + "\n")
        else:
            noexit_num +=1

 
print("dict_num is" + str(len_dict_num))    
print("noexit_num is" + str(noexit_num))            

input_3rd.close()
out.close()
