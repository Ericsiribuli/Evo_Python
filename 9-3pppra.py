from sys import argv
import os
import re
import multiprocessing
import numpy as np
import math
import random
from scipy.stats import pearsonr
input1,output1=argv[1:]

wt="GCGCAGACGAGTGCGGTGCAGCAAAAGCTGGCGGCGCTGGAGAAAAGCAGCGGAGGGCGGCTGGGCGTCGCGCTCATCGATACCGCAGATAATACGCAGGTGCTTTATCGCGGTGATGAACGCTTTCCAATGTGCAGTACCAGTAAAGTTATGGCGGCCGCGGCGGTGCTTAAGCAGAGTGAAACGCAAAAGCAGCTGCTTAATCAGCCTGTCGAGATCAAGCCTGCCGATCTGGTTAACTACAATCCGATTGCCGAAAAACACGTCAACGGCACAATGACGCTGGCAGAACTGAGCGCGGCCGCGTTGCAGTACAGCGACAATACCGCCATGAACAAATTGATTGCCCAGCTCGGTGGCCCGGGAGGCGTGACGGCTTTTGCCCGCGCGATCGGCGATGAGACGTTTCGTCTGGATCGCACTGAACCTACGCTGAATACCGCCATTCCCGGCGACCCGAGAGACACCACCACGCCGCGGGCGATGGCGCAGACGTTGCGTCAGCTTACGCTGGGTCATGCGCTGGGCGAAACCCAGCGGGCGCAGTTGGTGACGTGGCTCAAAGGCAATACGACCGGCGCAGCCAGCATTCGGGCCGGCTTACCGACGTCGTGGACTGTGGGTGATAAGACCGGCAGCGGCGACTACGGCACCACCAATGATATTGCGGTGATCTGGCCGCAGGGTCGTGCGCCGCTGGTTCTGGTGACCTATTTTACCCAGCCGCAACAGAACGCAGAGAGCCGCCGCGATGTGCTGGCTTCAGCGGCGAGAATCATCGCCGAAGGGCTG"

with open(input1,"r") as input_rere:#得到umi以及对应的genotype
    umi_geno_dict = {}
    pra_input = input_rere.read().strip(">").split(">")
    for line in pra_input:
        zwm_name = line.strip().split("\n")[0]
        line2 = line.strip().split("\n")
        geno = line2[1].split(" ")[0].split("_")[1][:792]
        umi1 = line2[1].split(" ")[1][:20]
        umi2 = line2[1].split(" ")[2][:20]
        if umi1 == umi2:
            if umi1 in umi_geno_dict:
                umi_geno_dict[umi1].append(geno)
            else:
                umi_geno_dict[umi1] = [geno]

last_dict = {}
for line in umi_geno_dict:
    mut_dict = {}
    number_mut = 0
    if len(np.unique(umi_geno_dict[line]))==1:
        mut = ""
        geno_myy = "".join(np.unique(umi_geno_dict[line]))
        if geno_myy == wt:
            last_dict[line] = ">0>" + " " + "WT" 
        else:
            mut_dict[geno_myy] = []
            for i in range(792):
                if geno_myy[i] != wt[i]:
                    mut_cluster = wt[i] + str(i+1) + geno_myy[i]
                    mut_dict[geno_myy].append(mut_cluster)
            mut_list = ",".join(mut_dict[geno_myy])
            number_mut = len(mut_dict[geno_myy])
            last_dict[line] = ">" + str(number_mut) + ">" + str(mut_list) 

    else: #一对多
        geno_dict={}
        uni_gen=np.unique(umi_geno_dict[line])
        for ii in uni_gen:
            geno_dict[ii]=umi_geno_dict[line].count(ii)
        sort_geno_dict=sorted(geno_dict.items(),key=lambda geno_dict:geno_dict[1],reverse=True)
        a=sort_geno_dict[0][1]
        c=0
        for iiii in sort_geno_dict[1:]:
            if iiii[1]>=a:
                c=1
        if c!=1:
            mutant1 = 0
            genotype1 = ""
            geno_myy = sort_geno_dict[0][0]
            if geno_myy == wt:
                last_dict[line] = ">0>" + " " + "WT" 
            else:
                mut_dict[geno_myy] = []
                for xx in range(792):
                    if geno_myy[xx] != wt[xx]:
                        mut_cluster = wt[xx] + str(xx+1) + geno_myy[xx]
                        mut_dict[geno_myy].append(mut_cluster)
                mut_list = ",".join(mut_dict[geno_myy])
                number_mut = len(mut_dict[geno_myy])
                last_dict[line] = ">" + str(number_mut) + ">" + str(mut_list) 

g_umi_dict={}
for um in last_dict.keys():
    if last_dict[um] in g_umi_dict.keys():
        g_umi_dict[last_dict[um]].append(um)
    else:
        g_umi_dict[last_dict[um]]=[um]

with open(output1,"w") as out2:
    for ggg in g_umi_dict.keys():
        out2.write(ggg+"*")
        for uuu in g_umi_dict[ggg]:
            out2.write(" "+uuu)
        out2.write("\n")



