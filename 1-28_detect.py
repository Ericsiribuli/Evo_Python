#-*-coding:utf-8 -*-
from sys import argv
import os
import re
import numpy as np
infile_f,infile_r,ccs_f,ccs_r=argv[1:]
inputf = open(infile_f,"r")
inputr = open(infile_r,"r")
forward_ccs = open(ccs_f,"r")
rorward_ccs = open(ccs_r,"r")
# outfile = open(out,"w")
umi_geno = {}
geno_pattern=re.compile("CGCTGC\w{918}TTAATTAA")
umi_pattern=re.compile("TTAATTAA\w{20}CTGCAG")
mud_dict={"A":"T","T":"A","C":"G","G":"C"}
Reverse_complemrnt= lambda x:"".join([mud_dict[i] for i in x][::-1])
ccs_dict1={}
ccs_dict2={}
ccs_dict3={}
ccs_dict4={}
n1=0
n2=0
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
            zwm_number2 = r[:29]
            if umi3 in ccs_dict1.keys():
                ccs_dict1[umi3].append(geno3)
            else:
                ccs_dict1[umi3]=[geno3]
# k=0
# for kk in ccs_dict.keys():
#     gg=ccs_dict[kk]
#     if len(np.unique(gg))==1:
#         k+=1
# print(k)
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
            zwm_number = f[:29]
            if umi1 in ccs_dict.keys():
                ccs_dict[umi1].append(geno1)
            else:
                ccs_dict[umi1]=[geno1]


o=0
for u in ccs_dict.keys():
    g=ccs_dict[u]
    if len(np.unique(g))==1:
        o+=1
print(o)
for r1 in rorward_ccs:
    r1 =r1.strip()
    r1_g=r1.split(",")[1]
    r1_umi=r1.split(",")[2]
    if r1_umi in ccs_dict3.keys():
        ccs_dict3[r1_umi].append(r1_g)
    else:
        ccs_dict3[r1_umi]=[r1_g]


# for t in forward_dict.keys():
#     gg=forward_dict[t]
#     if len(np.unique(gg))==1:
#         e+=1
# print(e)
for f1 in forward_ccs:
    f1 =f1.strip()
    f1_g=f1.split(",")[1]
    f1_umi=f1.split(",")[2]
    if f1_umi in ccs_dict4.keys():
        ccs_dict4[f1_umi].append(f1_g)
    else:
        ccs_dict4[f1_umi]=[f1_g]
print(cmp(ccs_dict1,ccs_dict3),cmp(ccs_dict2,ccs_dict4))