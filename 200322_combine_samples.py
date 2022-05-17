from sys import argv
import os
import re
import time
import multiprocessing
import numpy as np
import pandas as pd
import math
import matplotlib.pyplot as plt
#改用R算相关性，现在把每12个样本的umi合并

sample1,sample2,sample3,sample4,sample5,sample6,sample7,sample8,sample9,sample10,sample11,sample12,outfile=argv[1:]

file1 = open(sample1,"r")
file2 = open(sample2,"r")
file3 = open(sample3,"r")
file4 = open(sample4,"r")
file5 = open(sample5,"r")
file6 = open(sample6,"r")
file7 = open(sample7,"r")
file8 = open(sample8,"r")
file9 = open(sample9,"r")
file10 = open(sample10,"r")
file11 = open(sample11,"r")
file12 = open(sample12,"r")
out = open(outfile,"w")
sample1_dict = {}
sample2_dict = {}
sample3_dict = {}
sample4_dict = {}
sample5_dict = {}
sample6_dict = {}
sample7_dict = {}
sample8_dict = {}
sample9_dict = {}
sample10_dict = {}
sample11_dict = {}
sample12_dict = {}
out_dict = {}
day1_dict = {}

for i1 in file1:
    umi1 = i1.strip().split(",")[0]
    count = i1.strip().split(",")[1]
    sample1_dict[umi1] = count

for i1 in file2:
    umi1 = i1.strip().split(",")[0]
    count = i1.strip().split(",")[1]
    sample2_dict[umi1] = count

for i1 in file3:
    umi1 = i1.strip().split(",")[0]
    count = i1.strip().split(",")[1]
    sample3_dict[umi1] = count

for i1 in file4:
    umi1 = i1.strip().split(",")[0]
    count = i1.strip().split(",")[1]
    sample4_dict[umi1] = count

for i1 in file5:
    umi1 = i1.strip().split(",")[0]
    count = i1.strip().split(",")[1]
    sample5_dict[umi1] = count

for i1 in file6:
    umi1 = i1.strip().split(",")[0]
    count = i1.strip().split(",")[1]
    sample6_dict[umi1] = count

for i1 in file7:
    umi1 = i1.strip().split(",")[0]
    count = i1.strip().split(",")[1]
    sample7_dict[umi1] = count

for i1 in file8:
    umi1 = i1.strip().split(",")[0]
    count = i1.strip().split(",")[1]
    sample8_dict[umi1] = count

for i1 in file9:
    umi1 = i1.strip().split(",")[0]
    count = i1.strip().split(",")[1]
    sample9_dict[umi1] = count

for i1 in file10:
    umi1 = i1.strip().split(",")[0]
    count = i1.strip().split(",")[1]
    sample10_dict[umi1] = count

for i1 in file11:
    umi1 = i1.strip().split(",")[0]
    count = i1.strip().split(",")[1]
    sample11_dict[umi1] = count

for i1 in file12:
    umi1 = i1.strip().split(",")[0]
    count = i1.strip().split(",")[1]
    sample12_dict[umi1] = count

day1_dict.update(sample1_dict)
day1_dict.update(sample2_dict)
day1_dict.update(sample3_dict)

for xxx in day1_dict:
    if xxx in sample1_dict:
        out_dict[xxx] = [str(sample1_dict[xxx])]
    else:
        out_dict[xxx] = ['0']
    if xxx in sample2_dict:
        out_dict[xxx].append(str(sample2_dict[xxx]))
    else:
        out_dict[xxx].append('0')
    if xxx in sample3_dict:
        out_dict[xxx].append(str(sample3_dict[xxx]))
    else:
        out_dict[xxx].append('0')

    if xxx in sample4_dict:
        out_dict[xxx].append(str(sample4_dict[xxx]))
    else:
        out_dict[xxx].append('0')
    if xxx in sample5_dict:
        out_dict[xxx].append(str(sample5_dict[xxx]))
    else:
        out_dict[xxx].append('0')
    if xxx in sample6_dict:
        out_dict[xxx].append(str(sample6_dict[xxx]))
    else:
        out_dict[xxx].append('0')

    if xxx in sample7_dict:
        out_dict[xxx].append(str(sample7_dict[xxx]))
    else:
        out_dict[xxx].append('0')
    if xxx in sample8_dict:
        out_dict[xxx].append(str(sample8_dict[xxx]))
    else:
        out_dict[xxx].append('0')
    if xxx in sample9_dict:
        out_dict[xxx].append(str(sample9_dict[xxx]))
    else:
        out_dict[xxx].append('0')

    if xxx in sample10_dict:
        out_dict[xxx].append(str(sample10_dict[xxx]))
    else:
        out_dict[xxx].append('0')
    if xxx in sample11_dict:
        out_dict[xxx].append(str(sample11_dict[xxx]))
    else:
        out_dict[xxx].append('0')
    if xxx in sample12_dict:
        out_dict[xxx].append(str(sample12_dict[xxx]))
    else:
        out_dict[xxx].append('0')

for every in out_dict:
    count_list = ",".join(out_dict[every])
    out.write(every + "," + count_list + "\n")

out.close()

