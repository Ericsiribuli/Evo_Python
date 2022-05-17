from sys import argv
import re
from collections import Counter
import numpy as np

inputfile1,inputfile2=argv[1:]

input_file = open(inputfile1, "r")
input_woson = open(inputfile2, "r")
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
for line2 in input_woson:
    mut_num = line2.strip().split(">")[1]
    mut = ",".join(line2.strip().split(">")[2].split("*")[0].split())
    key = mut_num + "_" + mut
    umi = line2.strip().split("*")[1].split()
    if key in geno_umi_dict2:
        for every in umi:
            geno_umi_dict2[key].append(every)
    else:
        geno_umi_dict2[key] = []
        for every in umi:
            geno_umi_dict2[key].append(every)

# print(geno_umi_dict2)


me_len = len(geno_umi_dict1)
woson_len = len(geno_umi_dict2)

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
        if iiii[0:2] == "1_":
            print(iiii)
            
    
print("me:" + str(me_len))
print("woson:" + str(woson_len))

print(len_not_right)
print(not_right)
print(not_in)

input_file.close()
input_woson.close()


