from sys import argv
import os
import re
import multiprocessing
import numpy as np
import math
import random
from scipy.stats import pearsonr

input1,outfile=argv[1:]

inputfile1 = open(input1,"r")
out = open(outfile,"w")

def averagenum(num):
    nsum = 0
    for i in range(len(num)):
        nsum += num[i]
    return nsum / len(num)

npass_average_dict = {}

for a in inputfile1:
    if a[0] == "m":
        a = a.strip()
        a_line_list = a.split()
        a_qual = a_line_list[10]
        n_pass = a_line_list[12].split(":")[2]
        quality_list = []
        for i in a_qual:
            every_quality = ord(i)
            quality_list.append(every_quality)
        qua_ave = averagenum(quality_list)
        if n_pass in npass_average_dict:
            npass_average_dict[n_pass].append(qua_ave)
        else:
            npass_average_dict[n_pass] = [qua_ave]

for every in npass_average_dict:
    last_aver = averagenum(npass_average_dict[every])
    out.write(every + "," + str(last_aver) + "\n")

out.close()

