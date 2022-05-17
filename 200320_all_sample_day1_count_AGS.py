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
line2 = sample_pre.read().strip().split("\n")
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

os.system("python 200320_sample_day1above100_count.py /mnt/data2/disk/smrtanalysis/pacbio_data_new/new_illumina_data_2-14/Yang_fitness-landscape_illumina_all_data_2020-2-11/workdic_XZ/day1_above100/88AGS1.txt /mnt/data2/disk/smrtanalysis/pacbio_data_new/new_illumina_data_2-14/Yang_fitness-landscape_illumina_all_data_2020-2-11/%s/%s_umi.txt %s_day1above100.txt"%(sample1,sample1,name1))
os.system("python 200320_sample_day1above100_count.py /mnt/data2/disk/smrtanalysis/pacbio_data_new/new_illumina_data_2-14/Yang_fitness-landscape_illumina_all_data_2020-2-11/workdic_XZ/day1_above100/89AGS2.txt /mnt/data2/disk/smrtanalysis/pacbio_data_new/new_illumina_data_2-14/Yang_fitness-landscape_illumina_all_data_2020-2-11/%s/%s_umi.txt %s_day1above100.txt"%(sample2,sample2,name2))
os.system("python 200320_sample_day1above100_count.py /mnt/data2/disk/smrtanalysis/pacbio_data_new/new_illumina_data_2-14/Yang_fitness-landscape_illumina_all_data_2020-2-11/workdic_XZ/day1_above100/90AGS3.txt /mnt/data2/disk/smrtanalysis/pacbio_data_new/new_illumina_data_2-14/Yang_fitness-landscape_illumina_all_data_2020-2-11/%s/%s_umi.txt %s_day1above100.txt"%(sample3,sample3,name3))
os.system("python 200320_sample_day1above100_count.py /mnt/data2/disk/smrtanalysis/pacbio_data_new/new_illumina_data_2-14/Yang_fitness-landscape_illumina_all_data_2020-2-11/workdic_XZ/day1_above100/88AGS1.txt /mnt/data2/disk/smrtanalysis/pacbio_data_new/new_illumina_data_2-14/Yang_fitness-landscape_illumina_all_data_2020-2-11/%s/%s_umi.txt %s_day1above100.txt"%(sample4,sample4,name4))
os.system("python 200320_sample_day1above100_count.py /mnt/data2/disk/smrtanalysis/pacbio_data_new/new_illumina_data_2-14/Yang_fitness-landscape_illumina_all_data_2020-2-11/workdic_XZ/day1_above100/89AGS2.txt /mnt/data2/disk/smrtanalysis/pacbio_data_new/new_illumina_data_2-14/Yang_fitness-landscape_illumina_all_data_2020-2-11/%s/%s_umi.txt %s_day1above100.txt"%(sample5,sample5,name5))
os.system("python 200320_sample_day1above100_count.py /mnt/data2/disk/smrtanalysis/pacbio_data_new/new_illumina_data_2-14/Yang_fitness-landscape_illumina_all_data_2020-2-11/workdic_XZ/day1_above100/90AGS3.txt /mnt/data2/disk/smrtanalysis/pacbio_data_new/new_illumina_data_2-14/Yang_fitness-landscape_illumina_all_data_2020-2-11/%s/%s_umi.txt %s_day1above100.txt"%(sample6,sample6,name6))
os.system("python 200320_sample_day1above100_count.py /mnt/data2/disk/smrtanalysis/pacbio_data_new/new_illumina_data_2-14/Yang_fitness-landscape_illumina_all_data_2020-2-11/workdic_XZ/day1_above100/88AGS1.txt /mnt/data2/disk/smrtanalysis/pacbio_data_new/new_illumina_data_2-14/Yang_fitness-landscape_illumina_all_data_2020-2-11/%s/%s_umi.txt %s_day1above100.txt"%(sample7,sample7,name7))
os.system("python 200320_sample_day1above100_count.py /mnt/data2/disk/smrtanalysis/pacbio_data_new/new_illumina_data_2-14/Yang_fitness-landscape_illumina_all_data_2020-2-11/workdic_XZ/day1_above100/89AGS2.txt /mnt/data2/disk/smrtanalysis/pacbio_data_new/new_illumina_data_2-14/Yang_fitness-landscape_illumina_all_data_2020-2-11/%s/%s_umi.txt %s_day1above100.txt"%(sample8,sample8,name8))
os.system("python 200320_sample_day1above100_count.py /mnt/data2/disk/smrtanalysis/pacbio_data_new/new_illumina_data_2-14/Yang_fitness-landscape_illumina_all_data_2020-2-11/workdic_XZ/day1_above100/90AGS3.txt /mnt/data2/disk/smrtanalysis/pacbio_data_new/new_illumina_data_2-14/Yang_fitness-landscape_illumina_all_data_2020-2-11/%s/%s_umi.txt %s_day1above100.txt"%(sample9,sample9,name9))
os.system("python 200320_sample_day1above100_count.py /mnt/data2/disk/smrtanalysis/pacbio_data_new/new_illumina_data_2-14/Yang_fitness-landscape_illumina_all_data_2020-2-11/workdic_XZ/day1_above100/88AGS1.txt /mnt/data2/disk/smrtanalysis/pacbio_data_new/new_illumina_data_2-14/Yang_fitness-landscape_illumina_all_data_2020-2-11/%s/%s_umi.txt %s_day1above100.txt"%(sample10,sample10,name10))
os.system("python 200320_sample_day1above100_count.py /mnt/data2/disk/smrtanalysis/pacbio_data_new/new_illumina_data_2-14/Yang_fitness-landscape_illumina_all_data_2020-2-11/workdic_XZ/day1_above100/89AGS2.txt /mnt/data2/disk/smrtanalysis/pacbio_data_new/new_illumina_data_2-14/Yang_fitness-landscape_illumina_all_data_2020-2-11/%s/%s_umi.txt %s_day1above100.txt"%(sample11,sample11,name11))
os.system("python 200320_sample_day1above100_count.py /mnt/data2/disk/smrtanalysis/pacbio_data_new/new_illumina_data_2-14/Yang_fitness-landscape_illumina_all_data_2020-2-11/workdic_XZ/day1_above100/90AGS3.txt /mnt/data2/disk/smrtanalysis/pacbio_data_new/new_illumina_data_2-14/Yang_fitness-landscape_illumina_all_data_2020-2-11/%s/%s_umi.txt %s_day1above100.txt"%(sample12,sample12,name12))
    
sample_pre.close()
