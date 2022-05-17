from sys import argv
import os
import re
import multiprocessing
import numpy as np
import math
import random
from scipy.stats import pearsonr

input1=argv[1]

input_file = open(input1,"r")

reads_count = 0
umi_set = set()
geno_set = set()
for line in input_file:
    umi = line.strip().split(",")[0]
    geno = line.strip().split(",")[1]
    npass = int(line.strip().split(",")[2])
    if npass >= 5:
        reads_count +=1
        umi_set.add(umi)
        geno_set.add(geno)

umi_count = len(umi_set)
geno_count = len(geno_set)

print("reads is " + str(reads_count))
print("umi is " + str(umi_count))
print("geno is " + str(geno_count))