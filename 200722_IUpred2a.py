from sys import argv
import os
import re
import time
import numpy as np
import pandas as pd
import math

infile,out1file,out2file,param=argv[1:]
input1 = open(infile,"r")
out2 = open(out2file,"w")

file1 = input1.read().strip(">").split(">")
for every in file1:
    mut = every.split('\n')[0]
    out1 = open(out1file,"w")
    out1.write('>' + every)
    out1.close()
    disor_sum = 0
    for line in os.popen("python iupred2a.py every_fasta.fasta %s"%(param)):
        if line[0] != '#':
            IUP_score = line.strip().split()[2]
            if float(IUP_score) >0.5:
                disor_sum +=1
    out2.write(mut + "," + str(disor_sum) + "\n")


out2.close()


