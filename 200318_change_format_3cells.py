from sys import argv
import os
import re
import time
import multiprocessing
import numpy as np
import pandas as pd
import math
import matplotlib.pyplot as plt

threecells,outfile=argv[1:]

cells_file = open(threecells,"r")
out = open(outfile,"w")

geno_dict = {}

for every in cells_file:
    every1 = every.strip().split("\t")
    umi = every1[0]
    geno = every1[1]
    mut = " ".join(every1[2].split(","))
    mut_num = every1[3]
    if ">" + mut_num + "> " + mut + " * " in geno_dict:
        geno_dict[">" + mut_num + "> " + mut + " * "].append(umi)
    else:
        geno_dict[">" + mut_num + "> " + mut + " * "] = [umi]

for xx in geno_dict:
    umi_list = " ".join(geno_dict[xx])
    out.write(xx + umi_list + "\n")

out.close()