# -*- coding: utf-8 -*-
# 将六个库依据umi进行合并 方便其后拆分、筛最佳、拼接

from sys import argv
import os

file1,file2,file3,file4,file5,file6,umi_conbi6=argv[1:]

file1=open(file1,"r")
file2=open(file2,"r")
file3=open(file3,"r")
file4=open(file4,"r")
file5=open(file5,"r")
file6=open(file6,"r")
out_umi_combi6=open(umi_conbi6,"w")
dict_combi6={}

for a in file1:
    a1=a.strip().split(":")
    umi1=a1[0]
    # print(umi1)
    if umi1 in dict_combi6.keys():
        dict_combi6[umi1]=umi1+"_"+"one"
    else:
        dict_combi6[umi1]=umi1+"_"+"one"
# print(dict_combi6)
for b in file2:
    b1=b.strip().split(":")
    umi2=b1[0]
    if umi2 in dict_combi6.keys():
        dict_combi6[umi2]=dict_combi6[umi2]+"_"+"two"
    else:
        dict_combi6[umi2]=umi2+"_"+"two"

for c in file3:
    c1=c.strip().split(":")
    umi3=c1[0]
    if umi3 in dict_combi6.keys():
        dict_combi6[umi3]=dict_combi6[umi3]+"_"+"three"
    else:
        dict_combi6[umi3]=umi3+"_"+"three"

for d in file4:
    d1=d.strip().split(":")
    umi4=d1[0]
    if umi4 in dict_combi6.keys():
        dict_combi6[umi4]=dict_combi6[umi4]+"_"+"four"
    else:
        dict_combi6[umi4]=umi4+"_"+"four"

for e in file5:
    e1=e.strip().split(":")
    umi5=e1[0]
    if umi5 in dict_combi6.keys():
        dict_combi6[umi5]= dict_combi6[umi5]+"_"+"five"
    else:
        dict_combi6[umi5]=umi5+"_"+"five"

for f in file6:
    f1=f.strip().split(":")
    umi6=f1[0]
    if umi6 in dict_combi6.keys():
        dict_combi6[umi6]= dict_combi6[umi6]+"_"+"six"
    else:
        dict_combi6[umi6]=umi6+"_"+"six"

for g in dict_combi6.keys():
    combine6=dict_combi6[g]
    out_umi_combi6.write(">"+combine6+"\n"+combine6[:20]+"\n")

out_umi_combi6.close()