# -*- coding: utf-8 -*-


from sys import argv
import os
inputfile,file010,file011,file012,file013,file014,file015,out=argv[1:]

file=open(inputfile,"r")            #打开拆分好的文件
files010=open(file010,"r")      #打开六个库，做成六个字典
files011=open(file011,"r")
files012=open(file012,"r")
files013=open(file013,"r")
files014=open(file014,"r")
files015=open(file015,"r")
output=open(out,"w")
dict1={}
dict2={}
dict3={}
dict4={}
dict5={}
dict6={}

for each_umi1 in files010:                #还原六个库的字典
    t1 = each_umi1.rstrip(",").split(":")
    umi = t1[0]
    one_seq_qual = t1[1].strip().rstrip(",")
    if umi in dict1:
        dict1[umi].append(one_seq_qual)
    else:
        dict1[umi]=[one_seq_qual]
for each_umi2 in files011:                
    t2 = each_umi2.rstrip(",").split(":")
    umi = t2[0]
    one_seq_qual = t2[1].strip().rstrip(",")
    if umi in dict2:
        dict2[umi].append(one_seq_qual)
    else:
        dict2[umi]=[one_seq_qual]
for each_umi3 in files012:                
    t3 = each_umi3.rstrip(",").split(":")
    umi = t3[0]
    one_seq_qual = t3[1].strip().rstrip(",")
    if umi in dict3:
        dict3[umi].append(one_seq_qual)
    else:
        dict3[umi]=[one_seq_qual]
for each_umi4 in files013:                
    t4 = each_umi4.rstrip(",").split(":")
    umi = t4[0]
    one_seq_qual = t4[1].strip().rstrip(",")
    if umi in dict4:
        dict4[umi].append(one_seq_qual)
    else:
        dict4[umi]=[one_seq_qual]
for each_umi5 in files014:                
    t5 = each_umi5.rstrip(",").split(":")
    umi = t5[0]
    one_seq_qual = t5[1].strip().rstrip(",")
    if umi in dict5:
        dict5[umi].append(one_seq_qual)
    else:
        dict5[umi]=[one_seq_qual]
for each_umi6 in files015:                
    t6 = each_umi6.rstrip(",").split(":")
    umi = t6[0]
    one_seq_qual = t6[1].strip().rstrip(",")
    if umi in dict6:
        dict6[umi].append(one_seq_qual)
    else:
        dict6[umi]=[one_seq_qual]

for line in file:
    seq_qual1 = "one>"
    seq_qual2 = "two>"
    seq_qual3 = "three>"
    seq_qual4 = "four>"
    seq_qual5 = "five>"
    seq_qual6 = "six>"
    seq_qual11 = dict1[line[1:21]]
    seq_qual22 = dict2[line[1:21]]
    seq_qual33 = dict3[line[1:21]]
    seq_qual44 = dict4[line[1:21]]
    seq_qual55 = dict5[line[1:21]]
    seq_qual66 = dict6[line[1:21]]

    for every in seq_qual11:
        seq_qual1 = seq_qual1 + every + ","
        seq_qual1 = seq_qual1.strip()
    for every in seq_qual22:
        seq_qual2 = seq_qual2 + every + ","
        seq_qual2 = seq_qual2.strip()
    for every in seq_qual33:
        seq_qual3 = seq_qual3 + every + ","
        seq_qual3 = seq_qual3.strip()
    for every in seq_qual44:
        seq_qual4 = seq_qual4 + every + ","
        seq_qual4 = seq_qual4.strip()
    for every in seq_qual55:
        seq_qual5 = seq_qual5 + every + ","
        seq_qual5 = seq_qual5.strip()
    for every in seq_qual66:
        seq_qual6 = seq_qual6 + every + ","
        seq_qual6 = seq_qual6.strip().rstrip(",")
    
    output.write("geno" + "-" + seq_qual1 + seq_qual2 + seq_qual3 + seq_qual4 + seq_qual5 + seq_qual6 + "\n")

output.close()

