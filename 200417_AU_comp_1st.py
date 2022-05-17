from sys import argv
import os
import re
import multiprocessing
import numpy as np
import math
import random
from scipy.stats import pearsonr

input_umi,input_cellsfile,output = argv[1:]
wt="ATGTCCACAAAATCATATACCAGTAGAGCTGAGACTCATGCAAGTCCGGTTGCATCGAAACTTTTACGTTTAATGGATGAAAAGAAGACCAATTTGTGTGCTTCTCTTGACGTTCGTTCGACTGATGAGCTATTGAAACTTGTTGAAACGTTGGGTCCATACATTTGCCTTTTGAAAACACACGTTGATATCTTGGATGATTTCAGTTATGAGGGTACTGTCGTTCCATTGAAAGCATTGGCAGAGAAATACAAGTTCTTGATATTTGAGGACAGAAAATTCGCCGATATCGGTAACACAGTCAAATTACAATATACATCGGGCGTTTACCGTATCGCAGAATGGTCTGATATCACCAACGCCCACGGGGTTACTGGTGCTGGTATTGTTGCTGGCTTGAAACAAGGTGCGCAAGAGGTCACCAAAGAACCAAGGGGATTATTGATGCTTGCTGAATTGTCTTCCAAGGGTTCTCTAGCACACGGTGAATATACTAAGGGTACCGTTGATATTGCAAAGAGTGATAAAGATTTCGTTATTGGGTTCATTGCTCAGAACGATATGGGAGGAAGAGAAGAAGGGTTTGATTGGCTAATCATGACCCCAGGTGTAGGTTTAGACGACAAAGGCGATGCATTGGGTCAGCAGTACAGAACCGTCGACGAAGTTGTAAGTGGTGGATCAGATATCATCATTGTTGGCAGAGGACTTTTCGCCAAGGGTAGAGATCCTAAGGTTGAAGGTGAAAGATACAGAAATGCTGGATGGGAAGCGTACCAAAAGAGAATCAGCGCTCCCCATTAA"

out = open(output,"w")

umi_geno_dict = {}
with open(input_cellsfile,"r") as cellfile:
    for line in cellfile:
        line1 = line.strip().split("\t")
        umi = line1[0]
        geno = line1[1]
        umi_geno_dict[umi] = geno

with open(input_umi,"r") as umifile:
    for umi_every in umifile:
        mut_cluster = ""
        umi_1st = umi_every[:20]
        if umi_1st in umi_geno_dict.keys():
            geno_corresp = umi_geno_dict[umi_1st]
            for ii in range(804):
                if geno_corresp[ii] != wt[ii]:
                    mut_cluster = mut_cluster + wt[ii] + str(ii) + geno_corresp[ii] + "," 
            if mut_cluster == "":
                out.write(umi_every + ":" + "WT" + "\n")
            else:
                out.write(umi_every + ":" + mut_cluster + "\n")
        else:
            out.write(umi_every + ":" + "none" + "\n")

out.close()