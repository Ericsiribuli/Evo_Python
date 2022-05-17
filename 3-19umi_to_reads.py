from sys import argv
import re
import numpy as np

input_ccs_3rd,input_2nd,out_reads= argv[1:]

input_3rd = open(input_ccs_3rd,"r")
out = open(out_reads,"w")
umi_geno_pra_dict = {}
pra_3rd = input_3rd.read().strip(">").split(">")

for line in pra_3rd:
    zwm_name = line.strip().split("\n")[0]
    line2 = line.strip().split("\n")
    for every in line2[1:]:
        geno = every.split(",")[1]
        umi = every.split(",")[2]
        if umi in umi_geno_pra_dict:
            if geno != umi_geno_pra_dict[umi]:
                umi_geno_pra_dict[umi].append(geno)
        else:
            umi_geno_pra_dict[umi] = [geno]

umi_geno_dict = {}
for i in umi_geno_pra_dict:
    if len(umi_geno_pra_dict[i]) == 1:
        geno_i = "".join(umi_geno_pra_dict[i])
        umi_geno_dict[i] = geno_i

len_dict_num = len(umi_geno_dict)

noexit_num = 0
with open(input_2nd,"r") as umi_2rd:
    for every_umi in umi_2rd:
        every_umi = every_umi.strip()
        if every_umi in umi_geno_dict.keys():
            geno_2rd = umi_geno_dict[every_umi]
            out.write(every_umi + "," + geno_2rd + "\n")
        else:
            noexit_num +=1
 
print("dict_num is" + str(len_dict_num))    
print("noexit_num is" + str(noexit_num))            

input_3rd.close()
out.close()
