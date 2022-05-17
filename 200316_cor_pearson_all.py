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

    sample4 = line2[3]
    name4 = sample4[1:3]

    sample5 = line2[4]
    name5 = sample5[1:3]

    sample6 = line2[5]
    name6 = sample6[1:3]

    sample7 = line2[6]
    name7 = sample7[1:3]
    
    sample8 = line2[7]
    name8 = sample8[1:3]

    sample9 = line2[8]
    name9 = sample9[1:3]

    sample10 = line2[9]
    name10 = sample10[1:3]

    sample11 = line2[10]
    name11 = sample11[1:3]
    
    sample12 = line2[11]
    name12 = sample12[1:3]

    os.system("python 200316_cor_sample+pearson.py /mnt/data2/disk/smrtanalysis/pacbio_data_new/new_illumina_data_2-14/Yang_fitness-landscape_illumina_all_data_2020-2-11/%s/%s_umi.txt /mnt/data2/disk/smrtanalysis/pacbio_data_new/new_illumina_data_2-14/Yang_fitness-landscape_illumina_all_data_2020-2-11/%s/%s_umi.txt %s %s"%(sample1,sample1,sample1,sample1,name1,name1))
    os.system("python 200316_cor_sample+pearson.py /mnt/data2/disk/smrtanalysis/pacbio_data_new/new_illumina_data_2-14/Yang_fitness-landscape_illumina_all_data_2020-2-11/%s/%s_umi.txt /mnt/data2/disk/smrtanalysis/pacbio_data_new/new_illumina_data_2-14/Yang_fitness-landscape_illumina_all_data_2020-2-11/%s/%s_umi.txt %s %s"%(sample1,sample1,sample2,sample2,name1,name2))
    os.system("python 200316_cor_sample+pearson.py /mnt/data2/disk/smrtanalysis/pacbio_data_new/new_illumina_data_2-14/Yang_fitness-landscape_illumina_all_data_2020-2-11/%s/%s_umi.txt /mnt/data2/disk/smrtanalysis/pacbio_data_new/new_illumina_data_2-14/Yang_fitness-landscape_illumina_all_data_2020-2-11/%s/%s_umi.txt %s %s"%(sample1,sample1,sample3,sample3,name1,name3))
    os.system("python 200316_cor_sample+pearson.py /mnt/data2/disk/smrtanalysis/pacbio_data_new/new_illumina_data_2-14/Yang_fitness-landscape_illumina_all_data_2020-2-11/%s/%s_umi.txt /mnt/data2/disk/smrtanalysis/pacbio_data_new/new_illumina_data_2-14/Yang_fitness-landscape_illumina_all_data_2020-2-11/%s/%s_umi.txt %s %s"%(sample1,sample1,sample4,sample4,name1,name4))
    os.system("python 200316_cor_sample+pearson.py /mnt/data2/disk/smrtanalysis/pacbio_data_new/new_illumina_data_2-14/Yang_fitness-landscape_illumina_all_data_2020-2-11/%s/%s_umi.txt /mnt/data2/disk/smrtanalysis/pacbio_data_new/new_illumina_data_2-14/Yang_fitness-landscape_illumina_all_data_2020-2-11/%s/%s_umi.txt %s %s"%(sample1,sample1,sample5,sample5,name1,name5))
    os.system("python 200316_cor_sample+pearson.py /mnt/data2/disk/smrtanalysis/pacbio_data_new/new_illumina_data_2-14/Yang_fitness-landscape_illumina_all_data_2020-2-11/%s/%s_umi.txt /mnt/data2/disk/smrtanalysis/pacbio_data_new/new_illumina_data_2-14/Yang_fitness-landscape_illumina_all_data_2020-2-11/%s/%s_umi.txt %s %s"%(sample1,sample1,sample6,sample6,name1,name6))
    os.system("python 200316_cor_sample+pearson.py /mnt/data2/disk/smrtanalysis/pacbio_data_new/new_illumina_data_2-14/Yang_fitness-landscape_illumina_all_data_2020-2-11/%s/%s_umi.txt /mnt/data2/disk/smrtanalysis/pacbio_data_new/new_illumina_data_2-14/Yang_fitness-landscape_illumina_all_data_2020-2-11/%s/%s_umi.txt %s %s"%(sample1,sample1,sample7,sample7,name1,name7))
    os.system("python 200316_cor_sample+pearson.py /mnt/data2/disk/smrtanalysis/pacbio_data_new/new_illumina_data_2-14/Yang_fitness-landscape_illumina_all_data_2020-2-11/%s/%s_umi.txt /mnt/data2/disk/smrtanalysis/pacbio_data_new/new_illumina_data_2-14/Yang_fitness-landscape_illumina_all_data_2020-2-11/%s/%s_umi.txt %s %s"%(sample1,sample1,sample8,sample8,name1,name8))
    os.system("python 200316_cor_sample+pearson.py /mnt/data2/disk/smrtanalysis/pacbio_data_new/new_illumina_data_2-14/Yang_fitness-landscape_illumina_all_data_2020-2-11/%s/%s_umi.txt /mnt/data2/disk/smrtanalysis/pacbio_data_new/new_illumina_data_2-14/Yang_fitness-landscape_illumina_all_data_2020-2-11/%s/%s_umi.txt %s %s"%(sample1,sample1,sample9,sample9,name1,name9))
    os.system("python 200316_cor_sample+pearson.py /mnt/data2/disk/smrtanalysis/pacbio_data_new/new_illumina_data_2-14/Yang_fitness-landscape_illumina_all_data_2020-2-11/%s/%s_umi.txt /mnt/data2/disk/smrtanalysis/pacbio_data_new/new_illumina_data_2-14/Yang_fitness-landscape_illumina_all_data_2020-2-11/%s/%s_umi.txt %s %s"%(sample1,sample1,sample10,sample10,name1,name10))
    os.system("python 200316_cor_sample+pearson.py /mnt/data2/disk/smrtanalysis/pacbio_data_new/new_illumina_data_2-14/Yang_fitness-landscape_illumina_all_data_2020-2-11/%s/%s_umi.txt /mnt/data2/disk/smrtanalysis/pacbio_data_new/new_illumina_data_2-14/Yang_fitness-landscape_illumina_all_data_2020-2-11/%s/%s_umi.txt %s %s"%(sample1,sample1,sample11,sample11,name1,name11))
    os.system("python 200316_cor_sample+pearson.py /mnt/data2/disk/smrtanalysis/pacbio_data_new/new_illumina_data_2-14/Yang_fitness-landscape_illumina_all_data_2020-2-11/%s/%s_umi.txt /mnt/data2/disk/smrtanalysis/pacbio_data_new/new_illumina_data_2-14/Yang_fitness-landscape_illumina_all_data_2020-2-11/%s/%s_umi.txt %s %s"%(sample1,sample1,sample12,sample12,name1,name12))

    os.system("python 200316_cor_sample+pearson.py /mnt/data2/disk/smrtanalysis/pacbio_data_new/new_illumina_data_2-14/Yang_fitness-landscape_illumina_all_data_2020-2-11/%s/%s_umi.txt /mnt/data2/disk/smrtanalysis/pacbio_data_new/new_illumina_data_2-14/Yang_fitness-landscape_illumina_all_data_2020-2-11/%s/%s_umi.txt %s %s"%(sample2,sample2,sample2,sample2,name2,name2))
    os.system("python 200316_cor_sample+pearson.py /mnt/data2/disk/smrtanalysis/pacbio_data_new/new_illumina_data_2-14/Yang_fitness-landscape_illumina_all_data_2020-2-11/%s/%s_umi.txt /mnt/data2/disk/smrtanalysis/pacbio_data_new/new_illumina_data_2-14/Yang_fitness-landscape_illumina_all_data_2020-2-11/%s/%s_umi.txt %s %s"%(sample2,sample2,sample3,sample3,name2,name3))
    os.system("python 200316_cor_sample+pearson.py /mnt/data2/disk/smrtanalysis/pacbio_data_new/new_illumina_data_2-14/Yang_fitness-landscape_illumina_all_data_2020-2-11/%s/%s_umi.txt /mnt/data2/disk/smrtanalysis/pacbio_data_new/new_illumina_data_2-14/Yang_fitness-landscape_illumina_all_data_2020-2-11/%s/%s_umi.txt %s %s"%(sample2,sample2,sample4,sample4,name2,name4))
    os.system("python 200316_cor_sample+pearson.py /mnt/data2/disk/smrtanalysis/pacbio_data_new/new_illumina_data_2-14/Yang_fitness-landscape_illumina_all_data_2020-2-11/%s/%s_umi.txt /mnt/data2/disk/smrtanalysis/pacbio_data_new/new_illumina_data_2-14/Yang_fitness-landscape_illumina_all_data_2020-2-11/%s/%s_umi.txt %s %s"%(sample2,sample2,sample5,sample5,name2,name5))
    os.system("python 200316_cor_sample+pearson.py /mnt/data2/disk/smrtanalysis/pacbio_data_new/new_illumina_data_2-14/Yang_fitness-landscape_illumina_all_data_2020-2-11/%s/%s_umi.txt /mnt/data2/disk/smrtanalysis/pacbio_data_new/new_illumina_data_2-14/Yang_fitness-landscape_illumina_all_data_2020-2-11/%s/%s_umi.txt %s %s"%(sample2,sample2,sample6,sample6,name2,name6))
    os.system("python 200316_cor_sample+pearson.py /mnt/data2/disk/smrtanalysis/pacbio_data_new/new_illumina_data_2-14/Yang_fitness-landscape_illumina_all_data_2020-2-11/%s/%s_umi.txt /mnt/data2/disk/smrtanalysis/pacbio_data_new/new_illumina_data_2-14/Yang_fitness-landscape_illumina_all_data_2020-2-11/%s/%s_umi.txt %s %s"%(sample2,sample2,sample7,sample7,name2,name7))
    os.system("python 200316_cor_sample+pearson.py /mnt/data2/disk/smrtanalysis/pacbio_data_new/new_illumina_data_2-14/Yang_fitness-landscape_illumina_all_data_2020-2-11/%s/%s_umi.txt /mnt/data2/disk/smrtanalysis/pacbio_data_new/new_illumina_data_2-14/Yang_fitness-landscape_illumina_all_data_2020-2-11/%s/%s_umi.txt %s %s"%(sample2,sample2,sample8,sample8,name2,name8))
    os.system("python 200316_cor_sample+pearson.py /mnt/data2/disk/smrtanalysis/pacbio_data_new/new_illumina_data_2-14/Yang_fitness-landscape_illumina_all_data_2020-2-11/%s/%s_umi.txt /mnt/data2/disk/smrtanalysis/pacbio_data_new/new_illumina_data_2-14/Yang_fitness-landscape_illumina_all_data_2020-2-11/%s/%s_umi.txt %s %s"%(sample2,sample2,sample9,sample9,name2,name9))
    os.system("python 200316_cor_sample+pearson.py /mnt/data2/disk/smrtanalysis/pacbio_data_new/new_illumina_data_2-14/Yang_fitness-landscape_illumina_all_data_2020-2-11/%s/%s_umi.txt /mnt/data2/disk/smrtanalysis/pacbio_data_new/new_illumina_data_2-14/Yang_fitness-landscape_illumina_all_data_2020-2-11/%s/%s_umi.txt %s %s"%(sample2,sample2,sample10,sample10,name2,name10))
    os.system("python 200316_cor_sample+pearson.py /mnt/data2/disk/smrtanalysis/pacbio_data_new/new_illumina_data_2-14/Yang_fitness-landscape_illumina_all_data_2020-2-11/%s/%s_umi.txt /mnt/data2/disk/smrtanalysis/pacbio_data_new/new_illumina_data_2-14/Yang_fitness-landscape_illumina_all_data_2020-2-11/%s/%s_umi.txt %s %s"%(sample2,sample2,sample11,sample11,name2,name11))
    os.system("python 200316_cor_sample+pearson.py /mnt/data2/disk/smrtanalysis/pacbio_data_new/new_illumina_data_2-14/Yang_fitness-landscape_illumina_all_data_2020-2-11/%s/%s_umi.txt /mnt/data2/disk/smrtanalysis/pacbio_data_new/new_illumina_data_2-14/Yang_fitness-landscape_illumina_all_data_2020-2-11/%s/%s_umi.txt %s %s"%(sample2,sample2,sample12,sample12,name2,name12))

    os.system("python 200316_cor_sample+pearson.py /mnt/data2/disk/smrtanalysis/pacbio_data_new/new_illumina_data_2-14/Yang_fitness-landscape_illumina_all_data_2020-2-11/%s/%s_umi.txt /mnt/data2/disk/smrtanalysis/pacbio_data_new/new_illumina_data_2-14/Yang_fitness-landscape_illumina_all_data_2020-2-11/%s/%s_umi.txt %s %s"%(sample3,sample3,sample3,sample3,name3,name3))
    os.system("python 200316_cor_sample+pearson.py /mnt/data2/disk/smrtanalysis/pacbio_data_new/new_illumina_data_2-14/Yang_fitness-landscape_illumina_all_data_2020-2-11/%s/%s_umi.txt /mnt/data2/disk/smrtanalysis/pacbio_data_new/new_illumina_data_2-14/Yang_fitness-landscape_illumina_all_data_2020-2-11/%s/%s_umi.txt %s %s"%(sample3,sample3,sample4,sample4,name3,name4))
    os.system("python 200316_cor_sample+pearson.py /mnt/data2/disk/smrtanalysis/pacbio_data_new/new_illumina_data_2-14/Yang_fitness-landscape_illumina_all_data_2020-2-11/%s/%s_umi.txt /mnt/data2/disk/smrtanalysis/pacbio_data_new/new_illumina_data_2-14/Yang_fitness-landscape_illumina_all_data_2020-2-11/%s/%s_umi.txt %s %s"%(sample3,sample3,sample5,sample5,name3,name5))
    os.system("python 200316_cor_sample+pearson.py /mnt/data2/disk/smrtanalysis/pacbio_data_new/new_illumina_data_2-14/Yang_fitness-landscape_illumina_all_data_2020-2-11/%s/%s_umi.txt /mnt/data2/disk/smrtanalysis/pacbio_data_new/new_illumina_data_2-14/Yang_fitness-landscape_illumina_all_data_2020-2-11/%s/%s_umi.txt %s %s"%(sample3,sample3,sample6,sample6,name3,name6))
    os.system("python 200316_cor_sample+pearson.py /mnt/data2/disk/smrtanalysis/pacbio_data_new/new_illumina_data_2-14/Yang_fitness-landscape_illumina_all_data_2020-2-11/%s/%s_umi.txt /mnt/data2/disk/smrtanalysis/pacbio_data_new/new_illumina_data_2-14/Yang_fitness-landscape_illumina_all_data_2020-2-11/%s/%s_umi.txt %s %s"%(sample3,sample3,sample7,sample7,name3,name7))
    os.system("python 200316_cor_sample+pearson.py /mnt/data2/disk/smrtanalysis/pacbio_data_new/new_illumina_data_2-14/Yang_fitness-landscape_illumina_all_data_2020-2-11/%s/%s_umi.txt /mnt/data2/disk/smrtanalysis/pacbio_data_new/new_illumina_data_2-14/Yang_fitness-landscape_illumina_all_data_2020-2-11/%s/%s_umi.txt %s %s"%(sample3,sample3,sample8,sample8,name3,name8))
    os.system("python 200316_cor_sample+pearson.py /mnt/data2/disk/smrtanalysis/pacbio_data_new/new_illumina_data_2-14/Yang_fitness-landscape_illumina_all_data_2020-2-11/%s/%s_umi.txt /mnt/data2/disk/smrtanalysis/pacbio_data_new/new_illumina_data_2-14/Yang_fitness-landscape_illumina_all_data_2020-2-11/%s/%s_umi.txt %s %s"%(sample3,sample3,sample9,sample9,name3,name9))
    os.system("python 200316_cor_sample+pearson.py /mnt/data2/disk/smrtanalysis/pacbio_data_new/new_illumina_data_2-14/Yang_fitness-landscape_illumina_all_data_2020-2-11/%s/%s_umi.txt /mnt/data2/disk/smrtanalysis/pacbio_data_new/new_illumina_data_2-14/Yang_fitness-landscape_illumina_all_data_2020-2-11/%s/%s_umi.txt %s %s"%(sample3,sample3,sample10,sample10,name3,name10))
    os.system("python 200316_cor_sample+pearson.py /mnt/data2/disk/smrtanalysis/pacbio_data_new/new_illumina_data_2-14/Yang_fitness-landscape_illumina_all_data_2020-2-11/%s/%s_umi.txt /mnt/data2/disk/smrtanalysis/pacbio_data_new/new_illumina_data_2-14/Yang_fitness-landscape_illumina_all_data_2020-2-11/%s/%s_umi.txt %s %s"%(sample3,sample3,sample11,sample11,name3,name11))
    os.system("python 200316_cor_sample+pearson.py /mnt/data2/disk/smrtanalysis/pacbio_data_new/new_illumina_data_2-14/Yang_fitness-landscape_illumina_all_data_2020-2-11/%s/%s_umi.txt /mnt/data2/disk/smrtanalysis/pacbio_data_new/new_illumina_data_2-14/Yang_fitness-landscape_illumina_all_data_2020-2-11/%s/%s_umi.txt %s %s"%(sample3,sample3,sample12,sample12,name3,name12))

    os.system("python 200316_cor_sample+pearson.py /mnt/data2/disk/smrtanalysis/pacbio_data_new/new_illumina_data_2-14/Yang_fitness-landscape_illumina_all_data_2020-2-11/%s/%s_umi.txt /mnt/data2/disk/smrtanalysis/pacbio_data_new/new_illumina_data_2-14/Yang_fitness-landscape_illumina_all_data_2020-2-11/%s/%s_umi.txt %s %s"%(sample4,sample4,sample4,sample4,name4,name4))
    os.system("python 200316_cor_sample+pearson.py /mnt/data2/disk/smrtanalysis/pacbio_data_new/new_illumina_data_2-14/Yang_fitness-landscape_illumina_all_data_2020-2-11/%s/%s_umi.txt /mnt/data2/disk/smrtanalysis/pacbio_data_new/new_illumina_data_2-14/Yang_fitness-landscape_illumina_all_data_2020-2-11/%s/%s_umi.txt %s %s"%(sample4,sample4,sample5,sample5,name4,name5))
    os.system("python 200316_cor_sample+pearson.py /mnt/data2/disk/smrtanalysis/pacbio_data_new/new_illumina_data_2-14/Yang_fitness-landscape_illumina_all_data_2020-2-11/%s/%s_umi.txt /mnt/data2/disk/smrtanalysis/pacbio_data_new/new_illumina_data_2-14/Yang_fitness-landscape_illumina_all_data_2020-2-11/%s/%s_umi.txt %s %s"%(sample4,sample4,sample6,sample6,name4,name6))
    os.system("python 200316_cor_sample+pearson.py /mnt/data2/disk/smrtanalysis/pacbio_data_new/new_illumina_data_2-14/Yang_fitness-landscape_illumina_all_data_2020-2-11/%s/%s_umi.txt /mnt/data2/disk/smrtanalysis/pacbio_data_new/new_illumina_data_2-14/Yang_fitness-landscape_illumina_all_data_2020-2-11/%s/%s_umi.txt %s %s"%(sample4,sample4,sample7,sample7,name4,name7))
    os.system("python 200316_cor_sample+pearson.py /mnt/data2/disk/smrtanalysis/pacbio_data_new/new_illumina_data_2-14/Yang_fitness-landscape_illumina_all_data_2020-2-11/%s/%s_umi.txt /mnt/data2/disk/smrtanalysis/pacbio_data_new/new_illumina_data_2-14/Yang_fitness-landscape_illumina_all_data_2020-2-11/%s/%s_umi.txt %s %s"%(sample4,sample4,sample8,sample8,name4,name8))
    os.system("python 200316_cor_sample+pearson.py /mnt/data2/disk/smrtanalysis/pacbio_data_new/new_illumina_data_2-14/Yang_fitness-landscape_illumina_all_data_2020-2-11/%s/%s_umi.txt /mnt/data2/disk/smrtanalysis/pacbio_data_new/new_illumina_data_2-14/Yang_fitness-landscape_illumina_all_data_2020-2-11/%s/%s_umi.txt %s %s"%(sample4,sample4,sample9,sample9,name4,name9))
    os.system("python 200316_cor_sample+pearson.py /mnt/data2/disk/smrtanalysis/pacbio_data_new/new_illumina_data_2-14/Yang_fitness-landscape_illumina_all_data_2020-2-11/%s/%s_umi.txt /mnt/data2/disk/smrtanalysis/pacbio_data_new/new_illumina_data_2-14/Yang_fitness-landscape_illumina_all_data_2020-2-11/%s/%s_umi.txt %s %s"%(sample4,sample4,sample10,sample10,name4,name10))
    os.system("python 200316_cor_sample+pearson.py /mnt/data2/disk/smrtanalysis/pacbio_data_new/new_illumina_data_2-14/Yang_fitness-landscape_illumina_all_data_2020-2-11/%s/%s_umi.txt /mnt/data2/disk/smrtanalysis/pacbio_data_new/new_illumina_data_2-14/Yang_fitness-landscape_illumina_all_data_2020-2-11/%s/%s_umi.txt %s %s"%(sample4,sample4,sample11,sample11,name4,name11))
    os.system("python 200316_cor_sample+pearson.py /mnt/data2/disk/smrtanalysis/pacbio_data_new/new_illumina_data_2-14/Yang_fitness-landscape_illumina_all_data_2020-2-11/%s/%s_umi.txt /mnt/data2/disk/smrtanalysis/pacbio_data_new/new_illumina_data_2-14/Yang_fitness-landscape_illumina_all_data_2020-2-11/%s/%s_umi.txt %s %s"%(sample4,sample4,sample12,sample12,name4,name12))

    os.system("python 200316_cor_sample+pearson.py /mnt/data2/disk/smrtanalysis/pacbio_data_new/new_illumina_data_2-14/Yang_fitness-landscape_illumina_all_data_2020-2-11/%s/%s_umi.txt /mnt/data2/disk/smrtanalysis/pacbio_data_new/new_illumina_data_2-14/Yang_fitness-landscape_illumina_all_data_2020-2-11/%s/%s_umi.txt %s %s"%(sample5,sample5,sample5,sample5,name5,name5))
    os.system("python 200316_cor_sample+pearson.py /mnt/data2/disk/smrtanalysis/pacbio_data_new/new_illumina_data_2-14/Yang_fitness-landscape_illumina_all_data_2020-2-11/%s/%s_umi.txt /mnt/data2/disk/smrtanalysis/pacbio_data_new/new_illumina_data_2-14/Yang_fitness-landscape_illumina_all_data_2020-2-11/%s/%s_umi.txt %s %s"%(sample5,sample5,sample6,sample6,name5,name6))
    os.system("python 200316_cor_sample+pearson.py /mnt/data2/disk/smrtanalysis/pacbio_data_new/new_illumina_data_2-14/Yang_fitness-landscape_illumina_all_data_2020-2-11/%s/%s_umi.txt /mnt/data2/disk/smrtanalysis/pacbio_data_new/new_illumina_data_2-14/Yang_fitness-landscape_illumina_all_data_2020-2-11/%s/%s_umi.txt %s %s"%(sample5,sample5,sample7,sample7,name5,name7))
    os.system("python 200316_cor_sample+pearson.py /mnt/data2/disk/smrtanalysis/pacbio_data_new/new_illumina_data_2-14/Yang_fitness-landscape_illumina_all_data_2020-2-11/%s/%s_umi.txt /mnt/data2/disk/smrtanalysis/pacbio_data_new/new_illumina_data_2-14/Yang_fitness-landscape_illumina_all_data_2020-2-11/%s/%s_umi.txt %s %s"%(sample5,sample5,sample8,sample8,name5,name8))
    os.system("python 200316_cor_sample+pearson.py /mnt/data2/disk/smrtanalysis/pacbio_data_new/new_illumina_data_2-14/Yang_fitness-landscape_illumina_all_data_2020-2-11/%s/%s_umi.txt /mnt/data2/disk/smrtanalysis/pacbio_data_new/new_illumina_data_2-14/Yang_fitness-landscape_illumina_all_data_2020-2-11/%s/%s_umi.txt %s %s"%(sample5,sample5,sample9,sample9,name5,name9))
    os.system("python 200316_cor_sample+pearson.py /mnt/data2/disk/smrtanalysis/pacbio_data_new/new_illumina_data_2-14/Yang_fitness-landscape_illumina_all_data_2020-2-11/%s/%s_umi.txt /mnt/data2/disk/smrtanalysis/pacbio_data_new/new_illumina_data_2-14/Yang_fitness-landscape_illumina_all_data_2020-2-11/%s/%s_umi.txt %s %s"%(sample5,sample5,sample10,sample10,name5,name10))
    os.system("python 200316_cor_sample+pearson.py /mnt/data2/disk/smrtanalysis/pacbio_data_new/new_illumina_data_2-14/Yang_fitness-landscape_illumina_all_data_2020-2-11/%s/%s_umi.txt /mnt/data2/disk/smrtanalysis/pacbio_data_new/new_illumina_data_2-14/Yang_fitness-landscape_illumina_all_data_2020-2-11/%s/%s_umi.txt %s %s"%(sample5,sample5,sample11,sample11,name5,name11))
    os.system("python 200316_cor_sample+pearson.py /mnt/data2/disk/smrtanalysis/pacbio_data_new/new_illumina_data_2-14/Yang_fitness-landscape_illumina_all_data_2020-2-11/%s/%s_umi.txt /mnt/data2/disk/smrtanalysis/pacbio_data_new/new_illumina_data_2-14/Yang_fitness-landscape_illumina_all_data_2020-2-11/%s/%s_umi.txt %s %s"%(sample5,sample5,sample12,sample12,name5,name12))

    os.system("python 200316_cor_sample+pearson.py /mnt/data2/disk/smrtanalysis/pacbio_data_new/new_illumina_data_2-14/Yang_fitness-landscape_illumina_all_data_2020-2-11/%s/%s_umi.txt /mnt/data2/disk/smrtanalysis/pacbio_data_new/new_illumina_data_2-14/Yang_fitness-landscape_illumina_all_data_2020-2-11/%s/%s_umi.txt %s %s"%(sample6,sample6,sample6,sample6,name6,name6))
    os.system("python 200316_cor_sample+pearson.py /mnt/data2/disk/smrtanalysis/pacbio_data_new/new_illumina_data_2-14/Yang_fitness-landscape_illumina_all_data_2020-2-11/%s/%s_umi.txt /mnt/data2/disk/smrtanalysis/pacbio_data_new/new_illumina_data_2-14/Yang_fitness-landscape_illumina_all_data_2020-2-11/%s/%s_umi.txt %s %s"%(sample6,sample6,sample7,sample7,name6,name7))
    os.system("python 200316_cor_sample+pearson.py /mnt/data2/disk/smrtanalysis/pacbio_data_new/new_illumina_data_2-14/Yang_fitness-landscape_illumina_all_data_2020-2-11/%s/%s_umi.txt /mnt/data2/disk/smrtanalysis/pacbio_data_new/new_illumina_data_2-14/Yang_fitness-landscape_illumina_all_data_2020-2-11/%s/%s_umi.txt %s %s"%(sample6,sample6,sample8,sample8,name6,name8))
    os.system("python 200316_cor_sample+pearson.py /mnt/data2/disk/smrtanalysis/pacbio_data_new/new_illumina_data_2-14/Yang_fitness-landscape_illumina_all_data_2020-2-11/%s/%s_umi.txt /mnt/data2/disk/smrtanalysis/pacbio_data_new/new_illumina_data_2-14/Yang_fitness-landscape_illumina_all_data_2020-2-11/%s/%s_umi.txt %s %s"%(sample6,sample6,sample9,sample9,name6,name9))
    os.system("python 200316_cor_sample+pearson.py /mnt/data2/disk/smrtanalysis/pacbio_data_new/new_illumina_data_2-14/Yang_fitness-landscape_illumina_all_data_2020-2-11/%s/%s_umi.txt /mnt/data2/disk/smrtanalysis/pacbio_data_new/new_illumina_data_2-14/Yang_fitness-landscape_illumina_all_data_2020-2-11/%s/%s_umi.txt %s %s"%(sample6,sample6,sample10,sample10,name6,name10))
    os.system("python 200316_cor_sample+pearson.py /mnt/data2/disk/smrtanalysis/pacbio_data_new/new_illumina_data_2-14/Yang_fitness-landscape_illumina_all_data_2020-2-11/%s/%s_umi.txt /mnt/data2/disk/smrtanalysis/pacbio_data_new/new_illumina_data_2-14/Yang_fitness-landscape_illumina_all_data_2020-2-11/%s/%s_umi.txt %s %s"%(sample6,sample6,sample11,sample11,name6,name11))
    os.system("python 200316_cor_sample+pearson.py /mnt/data2/disk/smrtanalysis/pacbio_data_new/new_illumina_data_2-14/Yang_fitness-landscape_illumina_all_data_2020-2-11/%s/%s_umi.txt /mnt/data2/disk/smrtanalysis/pacbio_data_new/new_illumina_data_2-14/Yang_fitness-landscape_illumina_all_data_2020-2-11/%s/%s_umi.txt %s %s"%(sample6,sample6,sample12,sample12,name6,name12))

    os.system("python 200316_cor_sample+pearson.py /mnt/data2/disk/smrtanalysis/pacbio_data_new/new_illumina_data_2-14/Yang_fitness-landscape_illumina_all_data_2020-2-11/%s/%s_umi.txt /mnt/data2/disk/smrtanalysis/pacbio_data_new/new_illumina_data_2-14/Yang_fitness-landscape_illumina_all_data_2020-2-11/%s/%s_umi.txt %s %s"%(sample7,sample7,sample7,sample7,name7,name7))
    os.system("python 200316_cor_sample+pearson.py /mnt/data2/disk/smrtanalysis/pacbio_data_new/new_illumina_data_2-14/Yang_fitness-landscape_illumina_all_data_2020-2-11/%s/%s_umi.txt /mnt/data2/disk/smrtanalysis/pacbio_data_new/new_illumina_data_2-14/Yang_fitness-landscape_illumina_all_data_2020-2-11/%s/%s_umi.txt %s %s"%(sample7,sample7,sample8,sample8,name7,name8))
    os.system("python 200316_cor_sample+pearson.py /mnt/data2/disk/smrtanalysis/pacbio_data_new/new_illumina_data_2-14/Yang_fitness-landscape_illumina_all_data_2020-2-11/%s/%s_umi.txt /mnt/data2/disk/smrtanalysis/pacbio_data_new/new_illumina_data_2-14/Yang_fitness-landscape_illumina_all_data_2020-2-11/%s/%s_umi.txt %s %s"%(sample7,sample7,sample9,sample9,name7,name9))
    os.system("python 200316_cor_sample+pearson.py /mnt/data2/disk/smrtanalysis/pacbio_data_new/new_illumina_data_2-14/Yang_fitness-landscape_illumina_all_data_2020-2-11/%s/%s_umi.txt /mnt/data2/disk/smrtanalysis/pacbio_data_new/new_illumina_data_2-14/Yang_fitness-landscape_illumina_all_data_2020-2-11/%s/%s_umi.txt %s %s"%(sample7,sample7,sample10,sample10,name7,name10))
    os.system("python 200316_cor_sample+pearson.py /mnt/data2/disk/smrtanalysis/pacbio_data_new/new_illumina_data_2-14/Yang_fitness-landscape_illumina_all_data_2020-2-11/%s/%s_umi.txt /mnt/data2/disk/smrtanalysis/pacbio_data_new/new_illumina_data_2-14/Yang_fitness-landscape_illumina_all_data_2020-2-11/%s/%s_umi.txt %s %s"%(sample7,sample7,sample11,sample11,name7,name11))
    os.system("python 200316_cor_sample+pearson.py /mnt/data2/disk/smrtanalysis/pacbio_data_new/new_illumina_data_2-14/Yang_fitness-landscape_illumina_all_data_2020-2-11/%s/%s_umi.txt /mnt/data2/disk/smrtanalysis/pacbio_data_new/new_illumina_data_2-14/Yang_fitness-landscape_illumina_all_data_2020-2-11/%s/%s_umi.txt %s %s"%(sample7,sample7,sample12,sample12,name7,name12))

    os.system("python 200316_cor_sample+pearson.py /mnt/data2/disk/smrtanalysis/pacbio_data_new/new_illumina_data_2-14/Yang_fitness-landscape_illumina_all_data_2020-2-11/%s/%s_umi.txt /mnt/data2/disk/smrtanalysis/pacbio_data_new/new_illumina_data_2-14/Yang_fitness-landscape_illumina_all_data_2020-2-11/%s/%s_umi.txt %s %s"%(sample8,sample8,sample8,sample8,name8,name8))
    os.system("python 200316_cor_sample+pearson.py /mnt/data2/disk/smrtanalysis/pacbio_data_new/new_illumina_data_2-14/Yang_fitness-landscape_illumina_all_data_2020-2-11/%s/%s_umi.txt /mnt/data2/disk/smrtanalysis/pacbio_data_new/new_illumina_data_2-14/Yang_fitness-landscape_illumina_all_data_2020-2-11/%s/%s_umi.txt %s %s"%(sample8,sample8,sample9,sample9,name8,name9))
    os.system("python 200316_cor_sample+pearson.py /mnt/data2/disk/smrtanalysis/pacbio_data_new/new_illumina_data_2-14/Yang_fitness-landscape_illumina_all_data_2020-2-11/%s/%s_umi.txt /mnt/data2/disk/smrtanalysis/pacbio_data_new/new_illumina_data_2-14/Yang_fitness-landscape_illumina_all_data_2020-2-11/%s/%s_umi.txt %s %s"%(sample8,sample8,sample10,sample10,name8,name10))
    os.system("python 200316_cor_sample+pearson.py /mnt/data2/disk/smrtanalysis/pacbio_data_new/new_illumina_data_2-14/Yang_fitness-landscape_illumina_all_data_2020-2-11/%s/%s_umi.txt /mnt/data2/disk/smrtanalysis/pacbio_data_new/new_illumina_data_2-14/Yang_fitness-landscape_illumina_all_data_2020-2-11/%s/%s_umi.txt %s %s"%(sample8,sample8,sample11,sample11,name8,name11))
    os.system("python 200316_cor_sample+pearson.py /mnt/data2/disk/smrtanalysis/pacbio_data_new/new_illumina_data_2-14/Yang_fitness-landscape_illumina_all_data_2020-2-11/%s/%s_umi.txt /mnt/data2/disk/smrtanalysis/pacbio_data_new/new_illumina_data_2-14/Yang_fitness-landscape_illumina_all_data_2020-2-11/%s/%s_umi.txt %s %s"%(sample8,sample8,sample12,sample12,name8,name12))

    os.system("python 200316_cor_sample+pearson.py /mnt/data2/disk/smrtanalysis/pacbio_data_new/new_illumina_data_2-14/Yang_fitness-landscape_illumina_all_data_2020-2-11/%s/%s_umi.txt /mnt/data2/disk/smrtanalysis/pacbio_data_new/new_illumina_data_2-14/Yang_fitness-landscape_illumina_all_data_2020-2-11/%s/%s_umi.txt %s %s"%(sample9,sample9,sample9,sample9,name9,name9))
    os.system("python 200316_cor_sample+pearson.py /mnt/data2/disk/smrtanalysis/pacbio_data_new/new_illumina_data_2-14/Yang_fitness-landscape_illumina_all_data_2020-2-11/%s/%s_umi.txt /mnt/data2/disk/smrtanalysis/pacbio_data_new/new_illumina_data_2-14/Yang_fitness-landscape_illumina_all_data_2020-2-11/%s/%s_umi.txt %s %s"%(sample9,sample9,sample10,sample10,name9,name10))
    os.system("python 200316_cor_sample+pearson.py /mnt/data2/disk/smrtanalysis/pacbio_data_new/new_illumina_data_2-14/Yang_fitness-landscape_illumina_all_data_2020-2-11/%s/%s_umi.txt /mnt/data2/disk/smrtanalysis/pacbio_data_new/new_illumina_data_2-14/Yang_fitness-landscape_illumina_all_data_2020-2-11/%s/%s_umi.txt %s %s"%(sample9,sample9,sample11,sample11,name9,name11))
    os.system("python 200316_cor_sample+pearson.py /mnt/data2/disk/smrtanalysis/pacbio_data_new/new_illumina_data_2-14/Yang_fitness-landscape_illumina_all_data_2020-2-11/%s/%s_umi.txt /mnt/data2/disk/smrtanalysis/pacbio_data_new/new_illumina_data_2-14/Yang_fitness-landscape_illumina_all_data_2020-2-11/%s/%s_umi.txt %s %s"%(sample9,sample9,sample12,sample12,name9,name12))

    os.system("python 200316_cor_sample+pearson.py /mnt/data2/disk/smrtanalysis/pacbio_data_new/new_illumina_data_2-14/Yang_fitness-landscape_illumina_all_data_2020-2-11/%s/%s_umi.txt /mnt/data2/disk/smrtanalysis/pacbio_data_new/new_illumina_data_2-14/Yang_fitness-landscape_illumina_all_data_2020-2-11/%s/%s_umi.txt %s %s"%(sample10,sample10,sample10,sample10,name10,name10))
    os.system("python 200316_cor_sample+pearson.py /mnt/data2/disk/smrtanalysis/pacbio_data_new/new_illumina_data_2-14/Yang_fitness-landscape_illumina_all_data_2020-2-11/%s/%s_umi.txt /mnt/data2/disk/smrtanalysis/pacbio_data_new/new_illumina_data_2-14/Yang_fitness-landscape_illumina_all_data_2020-2-11/%s/%s_umi.txt %s %s"%(sample10,sample10,sample11,sample11,name10,name11))
    os.system("python 200316_cor_sample+pearson.py /mnt/data2/disk/smrtanalysis/pacbio_data_new/new_illumina_data_2-14/Yang_fitness-landscape_illumina_all_data_2020-2-11/%s/%s_umi.txt /mnt/data2/disk/smrtanalysis/pacbio_data_new/new_illumina_data_2-14/Yang_fitness-landscape_illumina_all_data_2020-2-11/%s/%s_umi.txt %s %s"%(sample10,sample10,sample12,sample12,name10,name12))

    os.system("python 200316_cor_sample+pearson.py /mnt/data2/disk/smrtanalysis/pacbio_data_new/new_illumina_data_2-14/Yang_fitness-landscape_illumina_all_data_2020-2-11/%s/%s_umi.txt /mnt/data2/disk/smrtanalysis/pacbio_data_new/new_illumina_data_2-14/Yang_fitness-landscape_illumina_all_data_2020-2-11/%s/%s_umi.txt %s %s"%(sample11,sample11,sample11,sample11,name11,name11))
    os.system("python 200316_cor_sample+pearson.py /mnt/data2/disk/smrtanalysis/pacbio_data_new/new_illumina_data_2-14/Yang_fitness-landscape_illumina_all_data_2020-2-11/%s/%s_umi.txt /mnt/data2/disk/smrtanalysis/pacbio_data_new/new_illumina_data_2-14/Yang_fitness-landscape_illumina_all_data_2020-2-11/%s/%s_umi.txt %s %s"%(sample11,sample11,sample12,sample12,name11,name12))

    os.system("python 200316_cor_sample+pearson.py /mnt/data2/disk/smrtanalysis/pacbio_data_new/new_illumina_data_2-14/Yang_fitness-landscape_illumina_all_data_2020-2-11/%s/%s_umi.txt /mnt/data2/disk/smrtanalysis/pacbio_data_new/new_illumina_data_2-14/Yang_fitness-landscape_illumina_all_data_2020-2-11/%s/%s_umi.txt %s %s"%(sample12,sample12,sample12,sample12,name12,name12))

sample_pre.close()
