#-*-coding:utf-8 -*-
#2019-3-15
#calculate fitness0
from sys import argv
import os
import re
import multiprocessing
import numpy as np
import math
import random
from scipy.stats import pearsonr
input1,one_f,one_r,two_f,two_r,three_f,three_r,output1=argv[1:]

wt="GCGCAGACGAGTGCGGTGCAGCAAAAGCTGGCGGCGCTGGAGAAAAGCAGCGGAGGGCGGCTGGGCGTCGCGCTCATCGATACCGCAGATAATACGCAGGTGCTTTATCGCGGTGATGAACGCTTTCCAATGTGCAGTACCAGTAAAGTTATGGCGGCCGCGGCGGTGCTTAAGCAGAGTGAAACGCAAAAGCAGCTGCTTAATCAGCCTGTCGAGATCAAGCCTGCCGATCTGGTTAACTACAATCCGATTGCCGAAAAACACGTCAACGGCACAATGACGCTGGCAGAACTGAGCGCGGCCGCGTTGCAGTACAGCGACAATACCGCCATGAACAAATTGATTGCCCAGCTCGGTGGCCCGGGAGGCGTGACGGCTTTTGCCCGCGCGATCGGCGATGAGACGTTTCGTCTGGATCGCACTGAACCTACGCTGAATACCGCCATTCCCGGCGACCCGAGAGACACCACCACGCCGCGGGCGATGGCGCAGACGTTGCGTCAGCTTACGCTGGGTCATGCGCTGGGCGAAACCCAGCGGGCGCAGTTGGTGACGTGGCTCAAAGGCAATACGACCGGCGCAGCCAGCATTCGGGCCGGCTTACCGACGTCGTGGACTGTGGGTGATAAGACCGGCAGCGGCGACTACGGCACCACCAATGATATTGCGGTGATCTGGCCGCAGGGTCGTGCGCCGCTGGTTCTGGTGACCTATTTTACCCAGCCGCAACAGAACGCAGAGAGCCGCCGCGATGTGCTGGCTTCAGCGGCGAGAATCATCGCCGAAGGGCTG"

ccs_dict1f = {}
ccs_dict1r = {}
ccs_dict2f = {}
ccs_dict2r = {}
ccs_dict3f = {}
ccs_dict3r = {}

with open(one_f,"r") as one_f_file:
    for r in one_f_file:
        if r[0]=="m":
            r = r.strip()
            zwm_name = r.split("/")[1]
            n_pass = r.split()[12].split(":")[2]
            ccs_dict1f[zwm_name] = n_pass 

with open(one_r,"r") as one_r_file:
    for r in one_r_file:
        if r[0]=="m":
            r = r.strip()
            zwm_name = r.split("/")[1]
            n_pass = r.split()[12].split(":")[2]
            ccs_dict1r[zwm_name] = n_pass 

with open(two_f,"r") as two_f_file:
    for r in two_f_file:
        if r[0]=="m":
            r = r.strip()
            zwm_name = r.split("/")[1]
            n_pass = r.split()[12].split(":")[2]
            ccs_dict2f[zwm_name] = n_pass 

with open(two_r,"r") as two_r_file:
    for r in two_r_file:
        if r[0]=="m":
            r = r.strip()
            zwm_name = r.split("/")[1]
            n_pass = r.split()[12].split(":")[2]
            ccs_dict2r[zwm_name] = n_pass 

with open(three_f,"r") as three_f_file:
    for r in three_f_file:
        if r[0]=="m":
            r = r.strip()
            zwm_name = r.split("/")[1]
            n_pass = r.split()[12].split(":")[2]
            ccs_dict3f[zwm_name] = n_pass 

with open(three_r,"r") as three_r_file:
    for r in three_r_file:
        if r[0]=="m":
            r = r.strip()
            zwm_name = r.split("/")[1]
            n_pass = r.split()[12].split(":")[2]
            ccs_dict3r[zwm_name] = n_pass 

out_file = open(output1,"w")

with open(input1,"r") as input_rere:#得到umi以及对应的genotype
    umi_geno_dict = {}
    pra_input = input_rere.read().strip(">").split(">")
    for line in pra_input:
        zwm_name = line.strip().split("\n")[0]
        line2 = line.strip().split("\n")
        geno = line2[1].split(" ")[0].split("_")[1]
        umi = line2[1].split(" ")[1]
        which_file = zwm_name.split("_")[2]
        which_strand = zwm_name.split("_")[1]
        which_zwm = zwm_name.split("_")[0]
        if which_file == "1" and which_strand == "f":
            np_pass = ccs_dict1f[which_zwm]
        if which_file == "1" and which_strand == "r":
            np_pass = ccs_dict1r[which_zwm]
        if which_file == "2" and which_strand == "f":
            np_pass = ccs_dict2f[which_zwm]
        if which_file == "2" and which_strand == "r":
            np_pass = ccs_dict2r[which_zwm]
        if which_file == "3" and which_strand == "f":
            np_pass = ccs_dict3f[which_zwm]
        if which_file == "3" and which_strand == "r":
            np_pass = ccs_dict3r[which_zwm]            
        out_file.write(umi + "," + geno + "," + np_pass + "\n")


out_file.close()


