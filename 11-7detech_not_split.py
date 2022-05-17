from sys import argv
import os
import re
import multiprocessing
import numpy as np
import math
import random
from scipy.stats import pearsonr

input1,input2,input3,outfile=argv[1:]

inputfile1 = open(input1,"r")
inputfile2 = open(input2,"r")
inputfile3 = open(input3,"r")
out = open(outfile,"w")

zwm_count_dict = {}

for a in inputfile1:
    if a[0] == "m":
        a = a.strip()
        a_line_list = a.split("/")
        a_zwm = a_line_list[1]
        zwm_name = a_zwm + "_" + "1"
        if zwm_name in zwm_count_dict:
            zwm_count_dict[zwm_name] +=1
        else:
            zwm_count_dict[zwm_name] = 1

for a in inputfile2:
    if a[0] == "m":
        a = a.strip()
        a_line_list = a.split("/")
        a_zwm = a_line_list[1]
        zwm_name = a_zwm + "_" + "2"
        if zwm_name in zwm_count_dict:
            zwm_count_dict[zwm_name] +=1
        else:
            zwm_count_dict[zwm_name] = 1

for a in inputfile3:
    if a[0] == "m":
        a = a.strip()
        a_line_list = a.split("/")
        a_zwm = a_line_list[1]
        zwm_name = a_zwm + "_" + "3"
        if zwm_name in zwm_count_dict:
            zwm_count_dict[zwm_name] +=1
        else:
            zwm_count_dict[zwm_name] = 1

# count_reads1 = 0
# count_reads2 = 0
# count_reads3 = 0
# count_reads4 = 0
# count_reads5 = 0
# count_reads6 = 0
# count_reads7 = 0
# count_reads8 = 0
# count_reads9 = 0
# count_reads10 = 0

# for line in zwm_count_dict:
#     count = zwm_count_dict[line]
#     if count >=1:
#         count_reads1 = count_reads1 + count
#     if count >=2:
#         count_reads2 = count_reads2 + count
#     if count >=3:
#         count_reads3 = count_reads3 + count
#     if count >=4:
#         count_reads4 = count_reads4 + count
#     if count >=5:
#         count_reads5 = count_reads5 + count
#     if count >=6:
#         count_reads6 = count_reads6 + count
#     if count >=7:
#         count_reads7 = count_reads7 + count
#     if count >=8:
#         count_reads8 = count_reads8 + count
#     if count >=9:
#         count_reads9 = count_reads9 + count
#     if count >=10:
#         count_reads10 = count_reads10 + count

count_cell_dict = {}
for k,v in zwm_count_dict.items():
    if v in count_cell_dict.keys():
        count_cell_dict[v].append(k)
    else:
        count_cell_dict[v] = [k]

for npass in count_cell_dict:
    num = len(count_cell_dict[npass])
    out.write(str(npass) + "," + str(num) + "\n")

# print("npass 1 reads is" + str(count_reads1))
# print("npass 2 reads is" + str(count_reads2))
# print("npass 3 reads is" + str(count_reads3))
# print("npass 4 reads is" + str(count_reads4))
# print("npass 5 reads is" + str(count_reads5))
# print("npass 6 reads is" + str(count_reads6))
# print("npass 7 reads is" + str(count_reads7))
# print("npass 8 reads is" + str(count_reads8))
# print("npass 9 reads is" + str(count_reads9))
# print("npass 10 reads is" + str(count_reads10))

out.close()