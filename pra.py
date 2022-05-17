from sys import argv
import os
import re
import time
import multiprocessing
import numpy as np
import pandas as pd
import math
import matplotlib.pyplot as plt
from scipy.stats import pearsonr

file1 = open("in1.txt","r")
file2 = open("in2.txt","r")
sample1_dict = {}
sample2_dict = {}
combine_dict = {'sample1':{},'sample2':{}}
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

list1 = []
list2 = []

for every in sample1_dict:
    if every in sample2_dict:
        combine_dict['sample1'][every] = math.log(sample1_dict[every],10)
        combine_dict['sample2'][every] = math.log(sample2_dict[every],10)
        #out.write(every + "," + str(sample1_dict[every]) + "," + str(sample2_dict[every]) + "\n")
    else:
        combine_dict['sample1'][every] = math.log(sample1_dict[every],10)
        combine_dict['sample2'][every] = 0
        #out.write(every + "," + str(sample1_dict[every]) + "," + "0" + "\n")
    
for every2 in sample2_dict:
    if every2 in sample1_dict:
        pass
    else:
        combine_dict['sample1'][every2] = 0
        combine_dict['sample2'][every2] = math.log(sample2_dict[every2],10)

sam1_dict = combine_dict['sample1']
sam2_dict = combine_dict['sample2']
for iii in sam1_dict:
  list1.append(sam1_dict[iii])
  list2.append(sam2_dict[iii])

print(pearsonr(list1,list2))

df_comb = pd.DataFrame(combine_dict)

df_pearson = df_comb.corr()
pearson_corr = round(df_pearson.iat[1,0],4)
print(pearson_corr)

df_spearman = df_comb.corr("spearman")
spearman_corr = round(df_spearman.iat[1,0],4)

plt.scatter(df_comb.sample1, df_comb.sample2, s=1)

text1 = "pearson:" + str(pearson_corr) + "\nspearman:" + str(spearman_corr)
plt.xlabel("sample%s"%(sample1_name))
plt.ylabel("sample%s"%(sample2_name))
plt.figure(figsize= (8,8))
plt.plot((-0.1,8),(-0.1,8), ls="--", c=".3")
plt.xlim(-0.1,8)
plt.ylim(-0.1,8)
plt.xlabel("%sumi"%(sample1_name))
plt.ylabel("%sumi"%(sample2_name))
plt.scatter(df_comb.sample1, df_comb.sample2, s=1)
plt.text(0.8,4.3,text1,fontdict={'size':'13','color':'b'})
plt.savefig("%s_%s.png"%(sample1_name,sample2_name))



import pandas as pd
import math
from Bio import Seq
from Bio.Alphabet import IUPAC
from Bio.SeqRecord import SeqRecord
from collections import Counter

wt = 'ATGAGTAAAGGAGAAGAACTTTTCACTGGAGTTGTCCCAATTCTTGTTGAATTAGATGGTGATGTTAATGGGCACAAATTTTCTGTCAGTGGAGAGGGTGAAGGTGATGCAACATACGGAAAACTTACCCTTAAATTTATTTGCACTACTGGAAAACTACCTGTTCCATGGCCAACACTTGTCACTACTTTCACTTATGGTGTTCAATGCTTTTCAAGATACCCAGATCATATGAAACGGCATGACTTTTTCAAGAGTGCCATGCCCGAAGGTTATGTACAGGAAAGAACTATATTTTTCAAAGATGACGGGAACTACAAGACACGTGCTGAAGTCAAGTTTGAAGGTGATACCCTTGTTAATAGAATCGAGTTAAAAGGTATTGATTTTAAAGAAGATGGAAACATTCTTGGACACAAATTGGAATACAACTATAACTCACACAATGTATACATCATGGCAGACAAACAAAAGAATGGAATCAAAGTTAACTTCAAAATTAGACACAACATTGAAGATGGAAGCGTTCAACTAGCAGACCATTATCAACAAAATACTCCAATTGGCGATGGCCCTGTCCTTTTACCAGACAACCATTACCTGTCCACACAATCTGCCCTTTCGAAAGATCCCAACGAAAAGAGAGACCACATGGTCCTTCTTGAGTTTGTAACAGCTGCTGGGATTACACATGGCATGGATGAACTATACAAATAGGGCGCGCCACTTCTAA'
i=611
change='G'
#for index,bp in enumerate(wt):
if i%3 == 1:
    aa = wt[i-1] + wt[i] + wt[i+1]
    aa_c = change + wt[i] + wt[i+1]
if i%3 == 2:
    aa = wt[i-2] + wt[i-1] + wt[i]
    aa_c = wt[i-2] + change + wt[i]
if i%3 == 0:
    aa = wt[i-3] + wt[i-2] + wt[i-1]
    aa_c = wt[i-3] + wt[i-2] + change
print(wt[i-1])
print(i%3)
print(aa)
print(aa_c)

dna = Seq.Seq(aa, IUPAC.unambiguous_dna)
mrna = dna.transcribe()
protein = mrna.translate()

changeAA_pos = math.ceil((index+1)/3)
out.write(bp + str(index+1) + rest + ',' + str(changeAA_pos) + ',' + str(protein[changeAA_pos-1]) + '\n')




