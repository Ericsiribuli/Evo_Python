from sys import argv
import os
import re
import time
import multiprocessing
import numpy as np
import pandas as pd
import math
import matplotlib.pyplot as plt

input_day1,out_day1=argv[1:]
file1 = open(input_day1,"r")
out = open(out_day1,"w")

sample1_dict = {}

for i1 in file1:
    umi1 = i1.strip()[:20]
    sample1_dict[umi1] = sample1_dict.get(umi1,0) + 1

for every in sample1_dict:
    if sample1_dict[every] >= 100:
        out.write(every + "\n")

out.close()