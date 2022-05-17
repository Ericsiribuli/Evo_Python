from sys import argv
import os
import re
import time
import multiprocessing
import numpy as np
import pandas as pd
import math
import matplotlib.pyplot as plt

sample_list,threefile,sample_locate=argv[1:]

sample_pre = open(sample_list,"r")

line2 = sample_pre.read().split('\n')
sample1 = line2[0]
name1 = sample1[:3] + sample1.split('_')[1]

sample2 = line2[1]
name2 = sample2[:3] + sample2.split('_')[1]

sample3 = line2[2]
name3 = sample3[:3] + sample3.split('_')[1]

sample4 = line2[3]
name4 = sample4[:3] + sample4.split('_')[1]

sample5 = line2[4]
name5 = sample5[:3] + sample5.split('_')[1]

sample6 = line2[5]
name6 = sample6[:3] + sample6.split('_')[1]

sample7 = line2[6]
name7 = sample7[:3] + sample7.split('_')[1]

sample8 = line2[7]
name8 = sample8[:3] + sample8.split('_')[1]

sample9 = line2[8]
name9 = sample9[:3] + sample9.split('_')[1]

sample10 = line2[9]
name10 = sample10[:3] + sample10.split('_')[1]

sample11 = line2[10]
name11 = sample11[:3] + sample11.split('_')[1]

sample12 = line2[11]
name12 = sample12[:3] + sample12.split('_')[1]

os.system("python 200807_cor_geno_nowt+pearson.py %s %s/%s %s/%s %s %s"%(threefile,sample_locate,sample1,sample_locate,sample1,name1,name1))
os.system("python 200807_cor_geno_nowt+pearson.py %s %s/%s %s/%s %s %s"%(threefile,sample_locate,sample1,sample_locate,sample2,name1,name2))
os.system("python 200807_cor_geno_nowt+pearson.py %s %s/%s %s/%s %s %s"%(threefile,sample_locate,sample1,sample_locate,sample3,name1,name3))
os.system("python 200807_cor_geno_nowt+pearson.py %s %s/%s %s/%s %s %s"%(threefile,sample_locate,sample1,sample_locate,sample4,name1,name4))
os.system("python 200807_cor_geno_nowt+pearson.py %s %s/%s %s/%s %s %s"%(threefile,sample_locate,sample1,sample_locate,sample5,name1,name5))
os.system("python 200807_cor_geno_nowt+pearson.py %s %s/%s %s/%s %s %s"%(threefile,sample_locate,sample1,sample_locate,sample6,name1,name6))
os.system("python 200807_cor_geno_nowt+pearson.py %s %s/%s %s/%s %s %s"%(threefile,sample_locate,sample1,sample_locate,sample7,name1,name7))
os.system("python 200807_cor_geno_nowt+pearson.py %s %s/%s %s/%s %s %s"%(threefile,sample_locate,sample1,sample_locate,sample8,name1,name8))
os.system("python 200807_cor_geno_nowt+pearson.py %s %s/%s %s/%s %s %s"%(threefile,sample_locate,sample1,sample_locate,sample9,name1,name9))
os.system("python 200807_cor_geno_nowt+pearson.py %s %s/%s %s/%s %s %s"%(threefile,sample_locate,sample1,sample_locate,sample10,name1,name10))
os.system("python 200807_cor_geno_nowt+pearson.py %s %s/%s %s/%s %s %s"%(threefile,sample_locate,sample1,sample_locate,sample11,name1,name11))
os.system("python 200807_cor_geno_nowt+pearson.py %s %s/%s %s/%s %s %s"%(threefile,sample_locate,sample1,sample_locate,sample12,name1,name12))

os.system("python 200807_cor_geno_nowt+pearson.py %s %s/%s %s/%s %s %s"%(threefile,sample_locate,sample2,sample_locate,sample2,name2,name2))
os.system("python 200807_cor_geno_nowt+pearson.py %s %s/%s %s/%s %s %s"%(threefile,sample_locate,sample2,sample_locate,sample3,name2,name3))
os.system("python 200807_cor_geno_nowt+pearson.py %s %s/%s %s/%s %s %s"%(threefile,sample_locate,sample2,sample_locate,sample4,name2,name4))
os.system("python 200807_cor_geno_nowt+pearson.py %s %s/%s %s/%s %s %s"%(threefile,sample_locate,sample2,sample_locate,sample5,name2,name5))
os.system("python 200807_cor_geno_nowt+pearson.py %s %s/%s %s/%s %s %s"%(threefile,sample_locate,sample2,sample_locate,sample6,name2,name6))
os.system("python 200807_cor_geno_nowt+pearson.py %s %s/%s %s/%s %s %s"%(threefile,sample_locate,sample2,sample_locate,sample7,name2,name7))
os.system("python 200807_cor_geno_nowt+pearson.py %s %s/%s %s/%s %s %s"%(threefile,sample_locate,sample2,sample_locate,sample8,name2,name8))
os.system("python 200807_cor_geno_nowt+pearson.py %s %s/%s %s/%s %s %s"%(threefile,sample_locate,sample2,sample_locate,sample9,name2,name9))
os.system("python 200807_cor_geno_nowt+pearson.py %s %s/%s %s/%s %s %s"%(threefile,sample_locate,sample2,sample_locate,sample10,name2,name10))
os.system("python 200807_cor_geno_nowt+pearson.py %s %s/%s %s/%s %s %s"%(threefile,sample_locate,sample2,sample_locate,sample11,name2,name11))
os.system("python 200807_cor_geno_nowt+pearson.py %s %s/%s %s/%s %s %s"%(threefile,sample_locate,sample2,sample_locate,sample12,name2,name12))

os.system("python 200807_cor_geno_nowt+pearson.py %s %s/%s %s/%s %s %s"%(threefile,sample_locate,sample3,sample_locate,sample3,name3,name3))
os.system("python 200807_cor_geno_nowt+pearson.py %s %s/%s %s/%s %s %s"%(threefile,sample_locate,sample3,sample_locate,sample4,name3,name4))
os.system("python 200807_cor_geno_nowt+pearson.py %s %s/%s %s/%s %s %s"%(threefile,sample_locate,sample3,sample_locate,sample5,name3,name5))
os.system("python 200807_cor_geno_nowt+pearson.py %s %s/%s %s/%s %s %s"%(threefile,sample_locate,sample3,sample_locate,sample6,name3,name6))
os.system("python 200807_cor_geno_nowt+pearson.py %s %s/%s %s/%s %s %s"%(threefile,sample_locate,sample3,sample_locate,sample7,name3,name7))
os.system("python 200807_cor_geno_nowt+pearson.py %s %s/%s %s/%s %s %s"%(threefile,sample_locate,sample3,sample_locate,sample8,name3,name8))
os.system("python 200807_cor_geno_nowt+pearson.py %s %s/%s %s/%s %s %s"%(threefile,sample_locate,sample3,sample_locate,sample9,name3,name9))
os.system("python 200807_cor_geno_nowt+pearson.py %s %s/%s %s/%s %s %s"%(threefile,sample_locate,sample3,sample_locate,sample10,name3,name10))
os.system("python 200807_cor_geno_nowt+pearson.py %s %s/%s %s/%s %s %s"%(threefile,sample_locate,sample3,sample_locate,sample11,name3,name11))
os.system("python 200807_cor_geno_nowt+pearson.py %s %s/%s %s/%s %s %s"%(threefile,sample_locate,sample3,sample_locate,sample12,name3,name12))

os.system("python 200807_cor_geno_nowt+pearson.py %s %s/%s %s/%s %s %s"%(threefile,sample_locate,sample4,sample_locate,sample4,name4,name4))
os.system("python 200807_cor_geno_nowt+pearson.py %s %s/%s %s/%s %s %s"%(threefile,sample_locate,sample4,sample_locate,sample5,name4,name5))
os.system("python 200807_cor_geno_nowt+pearson.py %s %s/%s %s/%s %s %s"%(threefile,sample_locate,sample4,sample_locate,sample6,name4,name6))
os.system("python 200807_cor_geno_nowt+pearson.py %s %s/%s %s/%s %s %s"%(threefile,sample_locate,sample4,sample_locate,sample7,name4,name7))
os.system("python 200807_cor_geno_nowt+pearson.py %s %s/%s %s/%s %s %s"%(threefile,sample_locate,sample4,sample_locate,sample8,name4,name8))
os.system("python 200807_cor_geno_nowt+pearson.py %s %s/%s %s/%s %s %s"%(threefile,sample_locate,sample4,sample_locate,sample9,name4,name9))
os.system("python 200807_cor_geno_nowt+pearson.py %s %s/%s %s/%s %s %s"%(threefile,sample_locate,sample4,sample_locate,sample10,name4,name10))
os.system("python 200807_cor_geno_nowt+pearson.py %s %s/%s %s/%s %s %s"%(threefile,sample_locate,sample4,sample_locate,sample11,name4,name11))
os.system("python 200807_cor_geno_nowt+pearson.py %s %s/%s %s/%s %s %s"%(threefile,sample_locate,sample4,sample_locate,sample12,name4,name12))

os.system("python 200807_cor_geno_nowt+pearson.py %s %s/%s %s/%s %s %s"%(threefile,sample_locate,sample5,sample_locate,sample5,name5,name5))
os.system("python 200807_cor_geno_nowt+pearson.py %s %s/%s %s/%s %s %s"%(threefile,sample_locate,sample5,sample_locate,sample6,name5,name6))
os.system("python 200807_cor_geno_nowt+pearson.py %s %s/%s %s/%s %s %s"%(threefile,sample_locate,sample5,sample_locate,sample7,name5,name7))
os.system("python 200807_cor_geno_nowt+pearson.py %s %s/%s %s/%s %s %s"%(threefile,sample_locate,sample5,sample_locate,sample8,name5,name8))
os.system("python 200807_cor_geno_nowt+pearson.py %s %s/%s %s/%s %s %s"%(threefile,sample_locate,sample5,sample_locate,sample9,name5,name9))
os.system("python 200807_cor_geno_nowt+pearson.py %s %s/%s %s/%s %s %s"%(threefile,sample_locate,sample5,sample_locate,sample10,name5,name10))
os.system("python 200807_cor_geno_nowt+pearson.py %s %s/%s %s/%s %s %s"%(threefile,sample_locate,sample5,sample_locate,sample11,name5,name11))
os.system("python 200807_cor_geno_nowt+pearson.py %s %s/%s %s/%s %s %s"%(threefile,sample_locate,sample5,sample_locate,sample12,name5,name12))

os.system("python 200807_cor_geno_nowt+pearson.py %s %s/%s %s/%s %s %s"%(threefile,sample_locate,sample6,sample_locate,sample6,name6,name6))
os.system("python 200807_cor_geno_nowt+pearson.py %s %s/%s %s/%s %s %s"%(threefile,sample_locate,sample6,sample_locate,sample7,name6,name7))
os.system("python 200807_cor_geno_nowt+pearson.py %s %s/%s %s/%s %s %s"%(threefile,sample_locate,sample6,sample_locate,sample8,name6,name8))
os.system("python 200807_cor_geno_nowt+pearson.py %s %s/%s %s/%s %s %s"%(threefile,sample_locate,sample6,sample_locate,sample9,name6,name9))
os.system("python 200807_cor_geno_nowt+pearson.py %s %s/%s %s/%s %s %s"%(threefile,sample_locate,sample6,sample_locate,sample10,name6,name10))
os.system("python 200807_cor_geno_nowt+pearson.py %s %s/%s %s/%s %s %s"%(threefile,sample_locate,sample6,sample_locate,sample11,name6,name11))
os.system("python 200807_cor_geno_nowt+pearson.py %s %s/%s %s/%s %s %s"%(threefile,sample_locate,sample6,sample_locate,sample12,name6,name12))

os.system("python 200807_cor_geno_nowt+pearson.py %s %s/%s %s/%s %s %s"%(threefile,sample_locate,sample7,sample_locate,sample7,name7,name7))
os.system("python 200807_cor_geno_nowt+pearson.py %s %s/%s %s/%s %s %s"%(threefile,sample_locate,sample7,sample_locate,sample8,name7,name8))
os.system("python 200807_cor_geno_nowt+pearson.py %s %s/%s %s/%s %s %s"%(threefile,sample_locate,sample7,sample_locate,sample9,name7,name9))
os.system("python 200807_cor_geno_nowt+pearson.py %s %s/%s %s/%s %s %s"%(threefile,sample_locate,sample7,sample_locate,sample10,name7,name10))
os.system("python 200807_cor_geno_nowt+pearson.py %s %s/%s %s/%s %s %s"%(threefile,sample_locate,sample7,sample_locate,sample11,name7,name11))
os.system("python 200807_cor_geno_nowt+pearson.py %s %s/%s %s/%s %s %s"%(threefile,sample_locate,sample7,sample_locate,sample12,name7,name12))

os.system("python 200807_cor_geno_nowt+pearson.py %s %s/%s %s/%s %s %s"%(threefile,sample_locate,sample8,sample_locate,sample8,name8,name8))
os.system("python 200807_cor_geno_nowt+pearson.py %s %s/%s %s/%s %s %s"%(threefile,sample_locate,sample8,sample_locate,sample9,name8,name9))
os.system("python 200807_cor_geno_nowt+pearson.py %s %s/%s %s/%s %s %s"%(threefile,sample_locate,sample8,sample_locate,sample10,name8,name10))
os.system("python 200807_cor_geno_nowt+pearson.py %s %s/%s %s/%s %s %s"%(threefile,sample_locate,sample8,sample_locate,sample11,name8,name11))
os.system("python 200807_cor_geno_nowt+pearson.py %s %s/%s %s/%s %s %s"%(threefile,sample_locate,sample8,sample_locate,sample12,name8,name12))

os.system("python 200807_cor_geno_nowt+pearson.py %s %s/%s %s/%s %s %s"%(threefile,sample_locate,sample9,sample_locate,sample9,name9,name9))
os.system("python 200807_cor_geno_nowt+pearson.py %s %s/%s %s/%s %s %s"%(threefile,sample_locate,sample9,sample_locate,sample10,name9,name10))
os.system("python 200807_cor_geno_nowt+pearson.py %s %s/%s %s/%s %s %s"%(threefile,sample_locate,sample9,sample_locate,sample11,name9,name11))
os.system("python 200807_cor_geno_nowt+pearson.py %s %s/%s %s/%s %s %s"%(threefile,sample_locate,sample9,sample_locate,sample12,name9,name12))

os.system("python 200807_cor_geno_nowt+pearson.py %s %s/%s %s/%s %s %s"%(threefile,sample_locate,sample10,sample_locate,sample10,name10,name10))
os.system("python 200807_cor_geno_nowt+pearson.py %s %s/%s %s/%s %s %s"%(threefile,sample_locate,sample10,sample_locate,sample11,name10,name11))
os.system("python 200807_cor_geno_nowt+pearson.py %s %s/%s %s/%s %s %s"%(threefile,sample_locate,sample10,sample_locate,sample12,name10,name12))

os.system("python 200807_cor_geno_nowt+pearson.py %s %s/%s %s/%s %s %s"%(threefile,sample_locate,sample11,sample_locate,sample11,name11,name11))
os.system("python 200807_cor_geno_nowt+pearson.py %s %s/%s %s/%s %s %s"%(threefile,sample_locate,sample11,sample_locate,sample12,name11,name12))

os.system("python 200807_cor_geno_nowt+pearson.py %s %s/%s %s/%s %s %s"%(threefile,sample_locate,sample12,sample_locate,sample12,name12,name12))

sample_pre.close()
