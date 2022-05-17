from sys import argv
import os
import re
import time
import multiprocessing
import numpy as np
import pandas as pd
import math
from collections import Counter

infile,outfile=argv[1:]
input1 = open(infile,"r")
out = open(outfile,"w")

for every in input1:
    if 'HOTLOOPS' in every:
        mut = every.split("_")[0].split(" ")[1]
        disorder_list = every.split(" ")[2:]
        sum1 = 0
        for line in disorder_list:
            line1 = line.strip(",").split("-")
            count_dif = int(line1[1]) - int(line1[0])
            sum1 = sum1 + count_dif
        out.write(mut + "," + str(sum1) + "\n") 

out.close()
