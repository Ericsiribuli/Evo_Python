from sys import argv
import os
import re
import time
import multiprocessing
import numpy as np

input_file,out_file=argv[1:]

umi_pattern=re.compile("TCGCTCTTATTGACCACACC\w{20}GCTTCGGCAGCACATATACTAA")
mud_dict={"A":"T","T":"A","C":"G","G":"C","N":""}
Reverse_complement= lambda x:"".join([mud_dict[i] for i in x][::-1])
umi_cluster = ""
out_umi = open(out_file,"w")
with open(input_file,"r") as file_2rd:
    for index,line in enumerate(file_2rd):
        if index % 4 == 1:
            line2 = line.strip()[1:]
            line_reverse = Reverse_complement(line2)
            umi = re.search(umi_pattern,line_reverse,flags=0)
            if umi is not None:
                umi2 = umi.group()[20:40]
                out_umi.write(umi2 + "\n")

out_umi.close()
