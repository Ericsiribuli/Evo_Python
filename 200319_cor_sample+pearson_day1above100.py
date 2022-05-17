from sys import argv
import os
import re
import time
import multiprocessing
import numpy as np
import pandas as pd
import math
import matplotlib.pyplot as plt

day1_file1,day1_file2,sample1,sample2,sample1_name,sample2_name=argv[1:]

day1_above1 = open(day1_file1,"r")
day1_above2 = open(day1_file2,"r")
file1 = open(sample1,"r")
file2 = open(sample2,"r")
#out = open(outfile,"w")
day1_above100_list1 = []
day1_above100_list2 = []
sample1_dict = {}
sample2_dict = {}
sample1_dict_fil = {}
sample2_dict_fil = {}
combine_dict1 = {'sample1':{},'sample2':{}}
combine_dict2 = {'sample1':{},'sample2':{}}
sum1 = 0
sum2 = 0

for day1_umi1 in day1_above1:
    day1_above100_list1.append(day1_umi1)

for day1_umi2 in day1_above2:
    day1_above100_list2.append(day1_umi2)

for i1 in file1:
    umi1 = i1.strip()[:20]
    sum1 +=1
    sample1_dict[umi1] = sample1_dict.get(umi1,0) + 1

for umi3 in sample1_dict:
    if umi3 in day1_above100_list1:
        sample1_dict_fil[umi3] = sample1_dict[umi3]

for i2 in file2:
    umi2 = i2.strip()[:20]
    sum2 +=1
    sample2_dict[umi2] = sample2_dict.get(umi2,0) + 1

for umi4 in sample2_dict:
    if umi4 in day1_above100_list2:
        sample2_dict_fil[umi4] = sample2_dict[umi4]

if sum1 > sum2:
    sum1_2 = sum1/sum2
    for line in sample2_dict_fil:
        sample2_dict_fil[line] = sample2_dict_fil[line] * sum1_2
if sum2 > sum1:
    sum2_1 = sum2/sum1
    for line in sample1_dict_fil:
        sample1_dict_fil[line] = sample1_dict_fil[line] *sum2_1

for every in sample1_dict_fil:
    if every in sample2_dict_fil:
        combine_dict1['sample1'][every] = sample1_dict_fil[every]
        combine_dict1['sample2'][every] = sample2_dict_fil[every]
    else:
        combine_dict1['sample1'][every] = sample1_dict_fil[every]
        combine_dict1['sample2'][every] = 0
    
for every2 in sample2_dict_fil:
    if every2 in sample1_dict_fil:
        pass
    else:
        combine_dict1['sample1'][every2] = 0
        combine_dict1['sample2'][every2] = sample2_dict_fil[every2]

df_comb1 = pd.DataFrame(combine_dict1)

df_pearson = df_comb1.corr()
pearson_corr = round(df_pearson.iat[1,0],4)

df_spearman = df_comb1.corr("spearman")
spearman_corr = round(df_spearman.iat[1,0],4)

print(str(sample1_name) + "," + str(sample2_name) + ":" + str(pearson_corr))





# data = pd.DataFrame({'A':np.random.randint(1, 100, 10), 
#                      'B':np.random.randint(1, 100, 10),
#                      'C':np.random.randint(1, 100, 10)})

# df2 = data.corr("spearman")
# plt.scatter(data.A,data.B)
# spearman = round(df2.iat[1,0],4)
# plt.text(40,80,spearman,fontdict={'size':'13','color':'b'})
# plt.show()


