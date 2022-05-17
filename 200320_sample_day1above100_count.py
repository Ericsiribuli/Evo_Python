from sys import argv
import os
import re
import time
import multiprocessing
import numpy as np
import pandas as pd
import math
import matplotlib.pyplot as plt
#改用R算相关性，得到每个样本umi和其数量的文件，现在限制了day1要大于100

day1_file1,sample1,outfile=argv[1:]

day1_above1 = open(day1_file1,"r")
file1 = open(sample1,"r")
out = open(outfile,"w")
day1_above100_list1 = []
sample1_dict = {}
sum = 0
#sample1_dict_fil = {}

for day1_umi1 in day1_above1:
    day1_umi1 = day1_umi1.strip()
    day1_above100_list1.append(day1_umi1)

for i1 in file1:
    umi1 = i1.strip()[:20]
    sample1_dict[umi1] = sample1_dict.get(umi1,0) + 1

for umi3 in sample1_dict:
    if umi3 in day1_above100_list1:
        sum+=1
        out.write(umi3 + "," + str(sample1_dict[umi3]) + "\n")

out.close()