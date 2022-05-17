from sys import argv
import os
import re
import time
import multiprocessing
import numpy as np
import pandas as pd
import math
import matplotlib.pyplot as plt
#3-24 nomis和mis1的文件的geno差距到底是怎么样的呢？
file_mis1,file_nomis=argv[1:]

mis1_file= open(file_mis1,"r")
nomis_file= open(file_nomis,"r")

geno_umi_dict_mis1 = {}
geno_umi_dict_nomis = {}
wt="ATGAGTAAAGGAGAAGAACTTTTCACTGGAGTTGTCCCAATTCTTGTTGAATTAGATGGTGATGTTAATGGGCACAAATTTTCTGTCAGTGGAGAGGGTGAAGGTGATGCAACATACGGAAAACTTACCCTTAAATTTATTTGCACTACTGGAAAACTACCTGTTCCATGGCCAACACTTGTCACTACTTTCACTTATGGTGTTCAATGCTTTTCAAGATACCCAGATCATATGAAACGGCATGACTTTTTCAAGAGTGCCATGCCCGAAGGTTATGTACAGGAAAGAACTATATTTTTCAAAGATGACGGGAACTACAAGACACGTGCTGAAGTCAAGTTTGAAGGTGATACCCTTGTTAATAGAATCGAGTTAAAAGGTATTGATTTTAAAGAAGATGGAAACATTCTTGGACACAAATTGGAATACAACTATAACTCACACAATGTATACATCATGGCAGACAAACAAAAGAATGGAATCAAAGTTAACTTCAAAATTAGACACAACATTGAAGATGGAAGCGTTCAACTAGCAGACCATTATCAACAAAATACTCCAATTGGCGATGGCCCTGTCCTTTTACCAGACAACCATTACCTGTCCACACAATCTGCCCTTTCGAAAGATCCCAACGAAAAGAGAGACCACATGGTCCTTCTTGAGTTTGTAACAGCTGCTGGGATTACACATGGCATGGATGAACTATACAAATAGGGCGCGCCACTTCTAA"

for line in mis1_file:
    umi = line.strip().split("\t")[0]
    geno = line.strip().split("\t")[1]
    if geno in geno_umi_dict_mis1:
        geno_umi_dict_mis1[geno].append(umi)
    else:
        geno_umi_dict_mis1[geno] = [umi]

for line in nomis_file:
    umi = line.strip().split("\t")[0]
    geno = line.strip().split("\t")[1]
    if geno in geno_umi_dict_nomis:
        geno_umi_dict_nomis[geno].append(umi)
    else:
        geno_umi_dict_nomis[geno] = [umi]

print("mis1 geno num:" + str(len(geno_umi_dict_mis1)))
print("nomis geno num:" + str(len(geno_umi_dict_nomis)))

in_mis1_not_nomis_list = []
in_nomis_not_mis1_list = []
mis1_in_nomis = 0
nomis_in_mis1 = 0

for mis1 in geno_umi_dict_mis1:
    if mis1 in geno_umi_dict_nomis:
        mis1_in_nomis +=1
    else:
        in_mis1_not_nomis_list.append(mis1)

for nomis in geno_umi_dict_nomis:
    if nomis in geno_umi_dict_mis1:
        nomis_in_mis1 +=1
    else:
        in_nomis_not_mis1_list.append(nomis)

print("mis1 in nomis num:" + str(mis1_in_nomis))
print("nomis in mis1 num:" + str(nomis_in_mis1))

print("in mis1 not nomis num:" + str(len(in_mis1_not_nomis_list)))
print("in nomis not mis1 num:" + str(len(in_nomis_not_mis1_list)))

