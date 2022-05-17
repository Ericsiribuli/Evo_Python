from sys import argv
import os
import re
import multiprocessing
import numpy as np
import math
import random
from scipy.stats import pearsonr
#用的wzx的三代数据格式 不需要和wt再进行比较
input_umi,input_cellsfile,output = argv[1:]

out = open(output,"w")

umi_geno_dict = {}
with open(input_cellsfile,"r") as cellfile:
    for line in cellfile:
        umi_list = line.strip().split(" * ")[1].split(" ")
        geno = line.strip().split(" * ")[0].split("> ")[1]
        for every_umi in umi_list:
            umi_geno_dict[every_umi] = geno

with open(input_umi,"r") as umifile:
    for umi_every in umifile:
        umi_1st = umi_every[:20]
        if umi_1st in umi_geno_dict.keys():
            geno_corresp = umi_geno_dict[umi_1st]
            out.write(umi_1st + ":" + geno_corresp + "\n")
        else:
            out.write(umi_1st + ":" + "none" + "\n")

out.close()