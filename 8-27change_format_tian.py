from sys import argv
import re
from collections import Counter
import numpy as np

inputfile,out=argv[1:]

sum_file = open(inputfile, "r")
out_file = open(out,"w")

ccs_dict = {}
for every in sum_file:
    if len(every)>40:
        geno = every.strip().split(",")[1]
        umi = every.strip().split(",")[0]
        out_file.write(geno + " " + umi + " " + umi + "\n")

sum_file.close()
out_file.close()

    
