from sys import argv
import os
import re
import time
import multiprocessing
import numpy as np
import pandas as pd
import math
import matplotlib.pyplot as plt

cells_file=argv[1]

geno_umi_file= open(cells_file,"r")

geno_umi_dict = {}
wt="ATGAGTAAAGGAGAAGAACTTTTCACTGGAGTTGTCCCAATTCTTGTTGAATTAGATGGTGATGTTAATGGGCACAAATTTTCTGTCAGTGGAGAGGGTGAAGGTGATGCAACATACGGAAAACTTACCCTTAAATTTATTTGCACTACTGGAAAACTACCTGTTCCATGGCCAACACTTGTCACTACTTTCACTTATGGTGTTCAATGCTTTTCAAGATACCCAGATCATATGAAACGGCATGACTTTTTCAAGAGTGCCATGCCCGAAGGTTATGTACAGGAAAGAACTATATTTTTCAAAGATGACGGGAACTACAAGACACGTGCTGAAGTCAAGTTTGAAGGTGATACCCTTGTTAATAGAATCGAGTTAAAAGGTATTGATTTTAAAGAAGATGGAAACATTCTTGGACACAAATTGGAATACAACTATAACTCACACAATGTATACATCATGGCAGACAAACAAAAGAATGGAATCAAAGTTAACTTCAAAATTAGACACAACATTGAAGATGGAAGCGTTCAACTAGCAGACCATTATCAACAAAATACTCCAATTGGCGATGGCCCTGTCCTTTTACCAGACAACCATTACCTGTCCACACAATCTGCCCTTTCGAAAGATCCCAACGAAAAGAGAGACCACATGGTCCTTCTTGAGTTTGTAACAGCTGCTGGGATTACACATGGCATGGATGAACTATACAAATAGGGCGCGCCACTTCTAA"

for line in geno_umi_file:
    umi = line.strip().split("\t")[0]
    geno = line.strip().split("\t")[1]
    if geno in geno_umi_dict:
        geno_umi_dict[geno].append(umi)
    else:
        geno_umi_dict[geno] = [umi]

print(len(geno_umi_dict))

wt_num = 0
single_num = 0
double_num = 0
triple_num = 0
four_num = 0
five_num = 0
geno_all_set = set()

for geno_myy in geno_umi_dict:
    geno_all_set.add(geno_myy)
    mut_num = 0
    for i in range(733):
        if geno_myy[i] != wt[i]:
            mut_num +=1
    if mut_num == 0:
        wt_num +=1
    if mut_num == 1:
        single_num +=1
    if mut_num == 2:
        double_num +=1
    if mut_num == 3:
        triple_num +=1
    if mut_num == 4:
        four_num +=1
    if mut_num == 5:
        five_num +=1

print("geno num:" + str(len(geno_all_set)))
print("wt num:" + str(wt_num))
print("single num:" + str(single_num))
print("double num:" + str(double_num))
print("three num:" + str(triple_num))
print("four num:" + str(four_num))
print("five num:" + str(five_num))

geno_umi_file.close()