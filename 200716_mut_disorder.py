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

file1 = input1.read().strip(">").split(">")
for every in file1:
    mut = every.split("\n")[0].split("|")[0]
    disorder_list = every.split("\n")[0].split("|")[2].split(":")[1].split(",")
    sum1 = 0
    if disorder_list == ['']:
        out.write(mut + "," + str(sum1) + "\n")
    else:
        for line in disorder_list:
            line1 = line.strip(" ").split("-")
            count_dif = int(line1[1]) - int(line1[0])
            sum1 = sum1 + count_dif
        out.write(mut + "," + str(sum1) + "\n") 

out.close()



