from sys import argv
import os
import re
import time
import multiprocessing
import numpy as np
import pandas as pd
import math
import matplotlib.pyplot as plt

threecells_file,sample1,sample2,sample1_name,sample2_name=argv[1:]

geno_umi_file= open(threecells_file,"r")
file1 = open(sample1,"r")
file2 = open(sample2,"r")
#out = open(outfile,"w")
sample1_dict = {}
sample2_dict = {}
sample1_geno_dict = {}
sample2_geno_dict = {}
combine_dict1 = {'sample1':{},'sample2':{}}
combine_dict2 = {'sample1':{},'sample2':{}}
geno_umi_dict = {}
wt="ATGAGTAAAGGAGAAGAACTTTTCACTGGAGTTGTCCCAATTCTTGTTGAATTAGATGGTGATGTTAATGGGCACAAATTTTCTGTCAGTGGAGAGGGTGAAGGTGATGCAACATACGGAAAACTTACCCTTAAATTTATTTGCACTACTGGAAAACTACCTGTTCCATGGCCAACACTTGTCACTACTTTCACTTATGGTGTTCAATGCTTTTCAAGATACCCAGATCATATGAAACGGCATGACTTTTTCAAGAGTGCCATGCCCGAAGGTTATGTACAGGAAAGAACTATATTTTTCAAAGATGACGGGAACTACAAGACACGTGCTGAAGTCAAGTTTGAAGGTGATACCCTTGTTAATAGAATCGAGTTAAAAGGTATTGATTTTAAAGAAGATGGAAACATTCTTGGACACAAATTGGAATACAACTATAACTCACACAATGTATACATCATGGCAGACAAACAAAAGAATGGAATCAAAGTTAACTTCAAAATTAGACACAACATTGAAGATGGAAGCGTTCAACTAGCAGACCATTATCAACAAAATACTCCAATTGGCGATGGCCCTGTCCTTTTACCAGACAACCATTACCTGTCCACACAATCTGCCCTTTCGAAAGATCCCAACGAAAAGAGAGACCACATGGTCCTTCTTGAGTTTGTAACAGCTGCTGGGATTACACATGGCATGGATGAACTATACAAATAGGGCGCGCCACTTCTAA"

for line in geno_umi_file:
    umi = line.strip().split(" * ")[1].split(" ")
    geno = line.strip().split(" * ")[0].split("> ")[1]
    if geno == 'WT':
        pass
    else:
        geno_umi_dict[geno] = umi

sum1 = 0
sum2 = 0

for i1 in file1:
    umi1 = i1.strip()[:20]
    sum1 +=1
    sample1_dict[umi1] = sample1_dict.get(umi1,0) + 1

for i2 in file2:
    umi2 = i2.strip()[:20]
    sum2 +=1
    sample2_dict[umi2] = sample2_dict.get(umi2,0) + 1


for geno in geno_umi_dict:
    if len(geno_umi_dict[geno])==1:
        umi_single = "".join(geno_umi_dict[geno])
        if umi_single in sample1_dict:
            sample1_geno_dict[geno] = sample1_dict[umi_single]
        if umi_single in sample2_dict:
            sample2_geno_dict[geno] = sample2_dict[umi_single]
    else:
        umi_list = geno_umi_dict[geno]
        num1 = 0
        num2 = 0
        for umi_every in umi_list:
            if umi_every in sample1_dict:
                num1 = num1 + sample1_dict[umi_every]
            if umi_every in sample2_dict:
                num2 = num2 + sample2_dict[umi_every]
        if num1 != 0:
            sample1_geno_dict[geno] = num1
        if num2 != 0:
            sample2_geno_dict[geno] = num2

if sum1 > sum2:
    sum1_2 = sum1/sum2
    for line in sample2_geno_dict:
        sample2_geno_dict[line] = sample2_geno_dict[line] * sum1_2
if sum2 > sum1:
    sum2_1 = sum2/sum1
    for line in sample1_geno_dict:
        sample1_geno_dict[line] = sample1_geno_dict[line] * sum2_1

for every in sample1_geno_dict:
    if every in sample2_geno_dict:
        combine_dict1['sample1'][every] = sample1_geno_dict[every]
        combine_dict1['sample2'][every] = sample2_geno_dict[every]
        #out.write(every + "," + str(sample1_dict[every]) + "," + str(sample2_dict[every]) + "\n")
    else:
        combine_dict1['sample1'][every] = sample1_geno_dict[every]
        combine_dict1['sample2'][every] = 0
        #out.write(every + "," + str(sample1_dict[every]) + "," + "0" + "\n")
    
for every2 in sample2_geno_dict:
    if every2 in sample1_geno_dict:
        pass
    else:
        combine_dict1['sample1'][every2] = 0
        combine_dict1['sample2'][every2] = sample2_geno_dict[every2]

df_comb1 = pd.DataFrame(combine_dict1)

df_pearson = df_comb1.corr()
pearson_corr = round(df_pearson.iat[1,0],4)

#print(str(sample1_name) + "," + str(sample2_name) + ":" + str(pearson_corr))

#df_spearman = df_comb1.corr("spearman")
#spearman_corr = round(df_spearman.iat[1,0],4)


for every in sample1_geno_dict:
    if every in sample2_geno_dict:
        combine_dict2['sample1'][every] = math.log(sample1_geno_dict[every],10)
        combine_dict2['sample2'][every] = math.log(sample2_geno_dict[every],10)
        #out.write(every + "," + str(sample1_dict[every]) + "," + str(sample2_dict[every]) + "\n")
    else:
        combine_dict2['sample1'][every] = math.log(sample1_geno_dict[every],10)
        combine_dict2['sample2'][every] = 0
        #out.write(every + "," + str(sample1_dict[every]) + "," + "0" + "\n")
    
for every2 in sample2_geno_dict:
    if every2 in sample1_geno_dict:
        pass
    else:
        combine_dict2['sample1'][every2] = 0
        combine_dict2['sample2'][every2] = math.log(sample2_geno_dict[every2],10)

df_comb2 = pd.DataFrame(combine_dict2)

text1 = "pearson:" + str(pearson_corr)
plt.xlabel("sample%s"%(sample1_name))
plt.ylabel("sample%s"%(sample2_name))
plt.figure(figsize= (8,8))
plt.plot((-0.1,8),(-0.1,8), ls="--", c=".3")
plt.xlim(-0.1,8)
plt.ylim(-0.1,8)
plt.xlabel("%s"%(sample1_name),fontsize = 16)
plt.ylabel("%s"%(sample2_name),fontsize = 16)
plt.scatter(df_comb2.sample1, df_comb2.sample2, s=1, c = 'k')
plt.savefig("%s:%s_geno_nowt.png"%(sample1_name,sample2_name))

if sample1_name == sample2_name:
    print(str(sample1_name) + "," + str(sample2_name) + "," + str(pearson_corr))
else:
    print(str(sample1_name) + "," + str(sample2_name) + "," + str(pearson_corr))
    print(str(sample2_name) + "," + str(sample1_name) + "," + str(pearson_corr))
