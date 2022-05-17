from sys import argv
import re
from collections import Counter
import numpy as np

inputfile1,inputfile2=argv[1:]

input_file = open(inputfile1, "r")
input_file2 = open(inputfile2, "r")
# out_file = open(out,"w")

geno_umi_dict1 = {}
geno_umi_dict2 = {}

# input_file = open("input.txt","r")

for line in input_file:
    line1 = line.strip().split()
    umi = line1[0]
    geno = line1[1]
    mut = line1[2]
    mut_num = line1[3]
    key = mut_num + "_" + mut
    if key in geno_umi_dict1:
        geno_umi_dict1[key].append(umi)
    else:
        geno_umi_dict1[key] = [umi]

# print(geno_umi_dict1)

# input_woson = open("input2.txt","r")
# geno_umi_dict2 = {}
for line in input_file2:
    line1 = line.strip().split()
    umi = line1[0]
    geno = line1[1]
    mut = line1[2]
    mut_num = line1[3]
    key = mut_num + "_" + mut
    if key in geno_umi_dict2:
        geno_umi_dict2[key].append(umi)
    else:
        geno_umi_dict2[key] = [umi]

# print(geno_umi_dict2)


me_len = len(geno_umi_dict1)
me_len2 = len(geno_umi_dict2)

not_in = 0
len_not_right = 0
not_right = 0
for iiii in geno_umi_dict1:
    if iiii in geno_umi_dict2:
        if len(geno_umi_dict1[iiii]) != len(geno_umi_dict2[iiii]):
            len_not_right+=1
        else:
            for aaaa in geno_umi_dict1[iiii]:
                if aaaa in geno_umi_dict2[iiii]:
                    pass
                else:
                    not_right +=1
    else:
        not_in+=1
    
print("me:" + str(me_len))
print("later:" + str(me_len2))

print(len_not_right)
print(not_right)
print(not_in)

input_file.close()
input_file2.close()


