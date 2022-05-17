from sys import argv
import os
import re
import time
import multiprocessing
import numpy as np
import pandas as pd
import math
import matplotlib.pyplot as plt

sample_list=argv[1]

sample_pre = open(sample_list,"r")
for line2 in sample_pre:
    name = line2[1:3]
    print(line2)
    os.system("python 200319_day1above100.py /mnt/data2/disk/smrtanalysis/pacbio_data_new/new_illumina_data_2-14/Yang_fitness-landscape_illumina_all_data_2020-2-11/%s/%s_umi.txt %s_day1above.txt"%(line2,line2,name))

sample_pre.close()
