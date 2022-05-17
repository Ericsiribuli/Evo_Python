from sys import argv
import os
import re
import time
import multiprocessing
import numpy as np

input_f,input_r,out_last=argv[1:]

inputf = open(input_f,"r")
inputr = open(input_r,"r")
outfile = open(out_last,"w")
umi_geno = {}
geno_pattern=re.compile("ATGAGT\w{719}ACTTCTAA")
umi_pattern=re.compile("ACCACACC\w{20}GCTTCG")
mud_dict={"A":"T","T":"A","C":"G","G":"C"}
Reverse_complemrnt= lambda x:"".join([mud_dict[i] for i in x][::-1])
ccs_dict1 = {}
ccs_dict3 = {}
for r in inputr:
    if r[0]=="m":
        r = r.strip()
        r_line_list=r.split()
        r_seq=r_line_list[9]
        r_reverse=Reverse_complemrnt(r_seq)
        geno2=re.search(geno_pattern,r_reverse,flags=0)
        umi2=re.search(umi_pattern,r_reverse,flags=0)
        if geno2 is not None and umi2 is not None:
            geno3 = geno2.group()
            umi3 = umi2.group()[8:28]
            zwm_number2 = r.split("/")[1]
            if umi3 in ccs_dict1.keys():
                ccs_dict1[umi3].append(zwm_number2 + "_" + "r" + "_" + geno3)
            else:
                ccs_dict1[umi3]=[zwm_number2 + "_" + "r" + "_" + geno3]

for f in inputf:
    if f[0]=="m":
        f = f.strip()
        f_line_list=f.split()
        f_seq=f_line_list[9]
        geno=re.search(geno_pattern,f_seq,flags=0)
        umi=re.search(umi_pattern,f_seq,flags=0)
        if geno is not None and umi is not None:
            geno1 = geno.group()
            umi1 = umi.group()[8:28]
            zwm_number = f.split("/")[1]
            if umi1 in ccs_dict1.keys():
                ccs_dict1[umi1].append(zwm_number + "_" + "f" + "_" + geno1)
            else:
                ccs_dict1[umi1]=[zwm_number + "_" + "f" + "_" + geno1]

ccs_cluster = ""
for every in ccs_dict1:
        if len(ccs_dict1[every]) == 1:
                geno2 = "".join(ccs_dict1[every])
                ccs_cluster = ccs_cluster + geno2 + " " + every + " " + every + "\n"
        else:
                geno_list = ccs_dict1[every]
                first = geno_list[0].split("_")[2]
                cluster = ""
                for zwm_geno in geno_list[1:]:
                        if first != zwm_geno.split("_")[2]:
                                first = "wrong"
                                break
                        else: continue
                if first != "wrong":
                        for last_zwm_geno in geno_list:
                            ccs_cluster = ccs_cluster + last_zwm_geno + " " + every + " " + every + "\n"

ccs_cluster = ccs_cluster.strip().strip("\n").split("\n")
for x in ccs_cluster:
    zwmname = x.split("_")[0]
    left = "_".join(x.split("_")[1:])
    if zwmname in ccs_dict3:
        ccs_dict3[zwmname].append(left)
    else:
        ccs_dict3[zwmname] = [left] 

for zwmname2 in ccs_dict3:
    if len(ccs_dict3[zwmname2]) ==1:
        cluster2 = "".join(ccs_dict3[zwmname2])
        outfile.write(">" + zwmname2 + "\n" + cluster2 + "\n")
    else:
        cluster2 = "\n".join(ccs_dict3[zwmname2])
        outfile.write(">" + zwmname2 + "\n" + cluster2 + "\n")

outfile.close()
