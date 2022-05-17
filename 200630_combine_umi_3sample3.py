from sys import argv
import os
import re
import time
import multiprocessing
import numpy as np
import pandas as pd
import math
from Bio import Seq
from Bio.Alphabet import IUPAC
from Bio.SeqRecord import SeqRecord
from collections import Counter

sample1,sample2,sample3,outfile=argv[1:]

file1 = open(sample1,"r")
file2 = open(sample2,"r")
file3 = open(sample3,"r")
out_single = open(outfile,"w")

sample1_dict = {}
sample2_dict = {}
sample3_dict = {}

for i1 in file1:
    umi1 = i1.strip()[:20]
    sample1_dict[umi1] = sample1_dict.get(umi1,0) + 1

for i2 in file2:
    umi2 = i2.strip()[:20]
    sample2_dict[umi2] = sample2_dict.get(umi2,0) + 1
    
for i3 in file3:
    umi3 = i3.strip()[:20]
    sample3_dict[umi3] = sample3_dict.get(umi3,0) + 1


X,Y,Z = Counter(sample1_dict),Counter(sample2_dict),Counter(sample3_dict)
allsample_dict = dict(X+Y+Z)

for every in allsample_dict:
    out_single.write(">" + every + "\n" + str(allsample_dict[every]) + " " + every + "\n")

out_single.close()