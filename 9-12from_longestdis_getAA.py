from sys import argv
import re
from collections import Counter
import numpy as np

input_file,out=argv[1:]
inputfile = open(input_file,"r")
out_file = open(out,"w")

# sum_distance_dict = {}
for line2 in inputfile:
    each = line2.strip().split()
    cluster = ""
    for other in each:
        distance = float(other.split(":")[1])
        if distance > 9.01:
            pass
        else:
            cluster = cluster + other + "   "
    out_file.write(cluster + "\n")

out_file.close()