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
sample = sample_pre.read().strip(">").split(">")
for line in sample:
    line2 = line.strip().split("\n")
    sample1 = line2[0]
    name1 = sample1[1:3]
    sample2 = line2[1]
    name2 = sample2[1:3]
    sample3 = line2[2]
    name3 = sample3[1:3]
    os.system("python 200222_cor_sample.py /mnt/data2/disk/smrtanalysis/pacbio_data_new/new_illumina_data_2-14/Yang_fitness-landscape_illumina_all_data_2020-2-11/%s/%s_umi.txt /mnt/data2/disk/smrtanalysis/pacbio_data_new/new_illumina_data_2-14/Yang_fitness-landscape_illumina_all_data_2020-2-11/%s/%s_umi.txt %s %s"%(sample1,sample1,sample2,sample2,name1,name2))
    os.system("python 200222_cor_sample.py /mnt/data2/disk/smrtanalysis/pacbio_data_new/new_illumina_data_2-14/Yang_fitness-landscape_illumina_all_data_2020-2-11/%s/%s_umi.txt /mnt/data2/disk/smrtanalysis/pacbio_data_new/new_illumina_data_2-14/Yang_fitness-landscape_illumina_all_data_2020-2-11/%s/%s_umi.txt %s %s"%(sample1,sample1,sample3,sample3,name1,name3))
    os.system("python 200222_cor_sample.py /mnt/data2/disk/smrtanalysis/pacbio_data_new/new_illumina_data_2-14/Yang_fitness-landscape_illumina_all_data_2020-2-11/%s/%s_umi.txt /mnt/data2/disk/smrtanalysis/pacbio_data_new/new_illumina_data_2-14/Yang_fitness-landscape_illumina_all_data_2020-2-11/%s/%s_umi.txt %s %s"%(sample2,sample2,sample3,sample3,name2,name3))

sample_pre.close()
