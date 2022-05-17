from sys import argv
import os
import re
import time
import multiprocessing
import numpy as np
import pandas as pd
import math

infile,outfile=argv[1:]

RSAfile = open(infile,'r')
out = open(outfile,'w')

RSA_file = RSAfile.read().strip().split('\n')
AA = RSA_file[0]
RSA = RSA_file[1]
print(len(AA.split(',')))
print(len(RSA.split(',')))
for i in range(257):
    out.write(str(i+5) + ',' + str(AA.split(',')[i]) + ',' + str(RSA.split(',')[i]) + '\n')

out.close()