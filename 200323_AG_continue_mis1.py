from sys import argv
import os
import re
import time
import multiprocessing
import numpy as np
import regex
#3-23 和200304相比，容许正则表达式错配一个

input_f,input_r,out_last=argv[1:]

inputf = open(input_f,"r")
inputr = open(input_r,"r")
outfile = open(out_last,"w")
umi_geno = {}
geno_re = "(?e)(?P<p1>GACAAAGATAGCTTCGCACA){e<=1}(?P<geno1>[ATCG]{733})(?P<p2>ATAAGCGAATTTCTTATGAT){e<=1}"
umi_re = "(?e)(?P<p1>TCGCTCTTATTGACCACACC){e<=1}(?P<umi1>[ATCG]{20})(?P<p2>GCTTCGGCAGCACATATACT){e<=1}"
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
        umi2 = regex.search(umi_re,r_reverse,flags=0)
        geno2 = regex.search(geno_re,r_reverse,flags=0)
        if geno2 is not None and umi2 is not None:
            geno3 = geno2.groupdict()["geno1"]
            umi3 = umi2.groupdict()["umi1"]
            zwm_number2 = r.split("/")[1]
            ccs_dict1[zwm_number2]=["r" + "_" + geno3 + " " + umi3 + " " + umi3]

for f in inputf:
    if f[0]=="m":
        f = f.strip()
        f_line_list=f.split()
        f_seq=f_line_list[9]
        umi = regex.search(umi_re,f_seq,flags=0)
        geno = regex.search(geno_re,f_seq,flags=0)
        if geno is not None and umi is not None:
            geno1 = geno.groupdict()["geno1"]
            umi1 = umi.groupdict()["umi1"]
            zwm_number = f.split("/")[1]
            if zwm_number in ccs_dict1.keys():
                ccs_dict1[zwm_number].append("f" + "_" + geno1 + " " + umi1 + " " + umi1)
            else:
                ccs_dict1[zwm_number]=["f" + "_" + geno1 + " " + umi1 + " " + umi1]

ccs_cluster = ""
for every in ccs_dict1:
    if len(ccs_dict1[every]) == 1:
        geno2 = "".join(ccs_dict1[every])
        ccs_cluster = ccs_cluster + ">" + every + "\n" + geno2 + "\n"
    else:
        geno2 = "\n".join(ccs_dict1[every])
        ccs_cluster = ccs_cluster + ">" + every + "\n" + geno2 + "\n"

pra_old54061 = ccs_cluster.strip(">").split(">")
for line in pra_old54061:
    zwm_name = line.strip().split("\n")[0]
    if line.find("r") == -1:
        line2 = line.strip().split("\n")
        f_geno = line.strip().split("\n")[1]
        outfile.write(">" + zwm_name + "\n" + "none" + "\n" + f_geno + "\n")
    if line.find("f") == -1:
        line2 = line.strip().split("\n")
        r_geno = line.strip().split("\n")[1]
        outfile.write(">" + zwm_name + "\n" + r_geno + "\n" + "none" + "\n")
    if line.find("r") != -1 and line.find("f") != -1:
        outfile.write(">" + line)


outfile.close()