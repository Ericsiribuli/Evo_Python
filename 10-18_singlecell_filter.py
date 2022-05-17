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

with open(input1,"r") as input_rere:#得到umi以及对应的genotype
    umi_geno_dict = {}
    pra_input = input_rere.read().strip(">").split(">")
    for line in pra_input:
        zwm_name = line.strip().split("\n")[0]
        line2 = line.strip().split("\n")
        geno = line2[1].split(" ")[0].split("_")[1]
        umi = line2[1].split(" ")[1]
        if umi in umi_geno_dict:
            if geno in umi_geno_dict[umi]:
                umi_geno_dict[umi][geno].append(zwm_name)
            else:
                umi_geno_dict[umi][geno] = [zwm_name]
        else:
            umi_geno_dict[umi] = {geno:[zwm_name]}

out_file = open(output1,"w")

one_to_one_umi_count = 0
one_to_mutp_count = 0
mutp_filter_count = 0
geno_one_one_set= set()
geno_before_set = set()
geno_after_set = set()
geno_wt_count = 0
geno_not_wt_count = 0


last_dict = {}
for i in umi_geno_dict.keys():
    mut_dict = {}
    total_pass = 0
    if len(umi_geno_dict[i])==1:
        one_to_one_umi_count +=1
        geno_dict = umi_geno_dict[i]
        for key in geno_dict:
            geno_myy = key
        geno_one_one_set.add(geno_myy)
        zwm_list = geno_dict[geno_myy]
        number_well = len(zwm_list)
        for every_zwm in zwm_list:
            which_file = every_zwm.split("_")[2]
            which_strand = every_zwm.split("_")[1]
            which_zwm = every_zwm.split("_")[0]
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
            out_file.write(i + "," + geno_myy + "," + np_pass + "\n")

    else: #一对多 将所有geno的zwm数量取出最大的
        one_to_mutp_count +=1
        geno_dict = umi_geno_dict[i]
        geno_zwm_dict = {}
        for key in geno_dict:
            geno_before_set.add(key)
            zwm_list = geno_dict[key]
            number_zwm = len(zwm_list)
            geno_zwm_dict[key] = number_zwm
        sort_geno_zwm_dict = sorted(geno_zwm_dict.items(),key=lambda geno_zwm_dict:geno_zwm_dict[1],reverse=True)
        number_well = sort_geno_zwm_dict[0][1]
        c = 0
        for iiii in sort_geno_zwm_dict[1:]:
            if iiii[1] >= number_well:
                c = 1
        if c!=1:
            mutp_filter_count += 1
            geno_myy = sort_geno_zwm_dict[0][0]
            geno_after_set.add(geno_myy)
            if geno_myy == wt:
                geno_wt_count +=1
            else:
                geno_not_wt_count +=1
            for every_zwm in geno_dict[geno_myy]:
                which_file = every_zwm.split("_")[2]
                which_strand = every_zwm.split("_")[1]
                which_zwm = every_zwm.split("_")[0]
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
                out_file.write(i + "," + geno_myy + "," + np_pass + "\n")

len_geno_one_one = len(geno_one_one_set)
len_geno_before_set = len(geno_before_set)
len_geno_after_set = len(geno_after_set)

print("one to one umi is " + str(one_to_one_umi_count))
print("one to one geno kind is " + str(len_geno_one_one))
print("one to muti is " + str(one_to_mutp_count))
print("muti filter one is " + str(mutp_filter_count))
print("geno kind before filter is " + str(len_geno_before_set))
print("geno kind after filter is " + str(len_geno_after_set))
print("after filter geno wt amount is " + str(geno_wt_count))
print("after filter geno not_wt amount is " + str(geno_not_wt_count))

out_file.close()
