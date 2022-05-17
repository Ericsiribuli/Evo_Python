from sys import argv
import re
from collections import Counter
import numpy as np

inputfile,out=argv[1:]

input_file = open(inputfile, "r")
out_file = open(out,"w")

pra_input = input_file.read().strip(">").split(">")

for line in pra_input:
    zwm_name = line.strip().split("\n")[0]
    other = line.strip().split("\n")[1:]
    for every in other:
        type1 = every.strip().split("_")[0]
        new_zwm_name = ">" + zwm_name + "_" + type1 + "_" + "1"
        out_file.write(new_zwm_name + "\n" + every + "\n")
    

input_file.close()
out_file.close()