#-*-coding:utf-8 -*-
from sys import argv
import os
import re


input_file,out_file=argv[1:]

umi_pattern=re.compile("TCGCTCTTATTGACCACACC\w{20}GCTTCGGCAGCACATATACTAA")
umi_cluster = ""
out_umi = open(out_file,"w")

with open(input_file,"r") as file_2rd:
    for index,line in enumerate(file_2rd):
        if index % 4 == 1:
            umi = re.search(umi_pattern,line,flags=0)
            if umi is not None:
                umi2 = umi.group()[20:40]
                out_umi.write(umi2 + "\n")

out_umi.close()