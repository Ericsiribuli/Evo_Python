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

for line in geno_umi_file:
    umi = line.strip().split("\t")[0]
    geno = line.strip().split("\t")[1]
    if geno in geno_umi_dict:
        geno_umi_dict[geno].append(umi)
    else:
        geno_umi_dict[geno] = [umi]
print(len(geno_umi_dict))

for i1 in file1:
    umi1 = i1.strip()[:20]
    sample1_dict[umi1] = sample1_dict.get(umi1,0) + 1

for i2 in file2:
    umi2 = i2.strip()[:20]
    sample2_dict[umi2] = sample2_dict.get(umi2,0) + 1

print(len(sample1_dict))
print(len(sample2_dict))

num1 = 0
num2 = 0
for geno in geno_umi_dict:
    if len(geno_umi_dict[geno])==1:
        umi_single = "".join(geno_umi_dict[geno])
        if umi_single in sample1_dict:
            num1+=1
            sample1_geno_dict[geno] = sample1_dict[umi_single]
        if umi_single in sample2_dict:
            num2+=1
            sample2_geno_dict[geno] = sample2_dict[umi_single]
    else:
        umi_list = geno_umi_dict[geno]
        sum1 = 0
        sum2 = 0
        for umi_every in umi_list:
            if umi_every in sample1_dict:
                sum1 = sum1 + sample1_dict[umi_every]
            if umi_every in sample2_dict:
                sum2 = sum2 + sample2_dict[umi_every]
        if sum1 != 0:
            sample1_geno_dict[geno] = sum1
        if sum2 != 0:
            sample2_geno_dict[geno] = sum2
print(str(num1))
print(str(num2))

print(len(sample1_geno_dict))
print(len(sample2_geno_dict))

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

df_spearman = df_comb1.corr("spearman")
spearman_corr = round(df_spearman.iat[1,0],4)


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

text1 = "pearson:" + str(pearson_corr) + "\nspearman:" + str(spearman_corr)
plt.xlabel("sample%s"%(sample1_name))
plt.ylabel("sample%s"%(sample2_name))
plt.figure(figsize= (8,8))
plt.plot((-0.1,8),(-0.1,8), ls="--", c=".3")
plt.xlim(-0.1,8)
plt.ylim(-0.1,8)
plt.xlabel("%sgeno"%(sample1_name))
plt.ylabel("%sgeno"%(sample2_name))
plt.scatter(df_comb2.sample1, df_comb2.sample2, s=1)
plt.text(0.8,4.3,text1,fontdict={'size':'13','color':'b'})
plt.savefig("%s_%s_geno.png"%(sample1_name,sample2_name))




# data = pd.DataFrame({'A':np.random.randint(1, 100, 10), 
#                      'B':np.random.randint(1, 100, 10),
#                      'C':np.random.randint(1, 100, 10)})

# df2 = data.corr("spearman")
# plt.scatter(data.A,data.B)
# spearman = round(df2.iat[1,0],4)
# plt.text(40,80,spearman,fontdict={'size':'13','color':'b'})
# plt.show()


