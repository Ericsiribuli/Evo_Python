from sys import argv
import os
import re
import time
import multiprocessing
import numpy as np
import pandas as pd
import math
import matplotlib.pyplot as plt

sample1,sample2,sample1_name,sample2_name=argv[1:]

file1 = open(sample1,"r")
file2 = open(sample2,"r")
#out = open(outfile,"w")
sample1_dict = {}
sample2_dict = {}
combine_dict1 = {'sample1':{},'sample2':{}}
combine_dict2 = {'sample1':{},'sample2':{}}
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

if sum1 > sum2:
    sum1_2 = sum1/sum2
    for line in sample2_dict:
        sample2_dict[line] = sample2_dict[line] * sum1_2
if sum2 > sum1:
    sum2_1 = sum2/sum1
    for line in sample1_dict:
        sample1_dict[line] = sample1_dict[line] *sum2_1

for every in sample1_dict:
    if every in sample2_dict:
        combine_dict1['sample1'][every] = sample1_dict[every]
        combine_dict1['sample2'][every] = sample2_dict[every]
        #out.write(every + "," + str(sample1_dict[every]) + "," + str(sample2_dict[every]) + "\n")
    else:
        combine_dict1['sample1'][every] = sample1_dict[every]
        combine_dict1['sample2'][every] = 0
        #out.write(every + "," + str(sample1_dict[every]) + "," + "0" + "\n")
    
for every2 in sample2_dict:
    if every2 in sample1_dict:
        pass
    else:
        combine_dict1['sample1'][every2] = 0
        combine_dict1['sample2'][every2] = sample2_dict[every2]

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


