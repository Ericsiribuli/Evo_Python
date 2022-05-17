from sys import argv
import re
from collections import Counter
import numpy as np

inputfile,out=argv[1:]

sum_file = open(inputfile, "r")
out_file = open(out,"w")

ccs_dict = {}
for every in sum_file:
    if len(every)>40:
        geno = every.strip().split(" ")[0].split("_")[1]
        umi = every.strip().split(" ")[1]
        if umi in ccs_dict:
            ccs_dict[umi].append(geno)
        else:
            ccs_dict[umi] = [geno]

print(len(ccs_dict))

umi_geno_my_dict = {}
for umi_myy in ccs_dict:
    if len(np.unique(ccs_dict[umi_myy]))==1:
        geno_myy = "".join(np.unique(ccs_dict[umi_myy]))
        umi_geno_my_dict[umi_myy] = geno_myy

print(len(umi_geno_my_dict))

sum_file.close()
out_file.close()
