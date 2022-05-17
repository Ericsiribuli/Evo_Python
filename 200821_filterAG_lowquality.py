from sys import argv
import os
import re
import multiprocessing
import numpy as np
import math
import random
import matplotlib.pyplot as plt

low_quality_list = []
with open('/mnt/data2/disk/smrtanalysis/pacbio_data_new/AG_200623_101855_subreads_f_ccs.sam','r') as f:
    for line in f:
        mim_qua = 0
        if line[0] == 'm':
            quality_all = line.strip().split("\t")[10]
            for every in quality_all:
                if mim_qua == 0:
                    mim_qua == ord(every)
                else:
                    if mim_qua > ord(every):
                        mim_qua == ord(every)
            low_quality_list.append(mim_qua)
            

plt.hist(low_quality_list, normed=0, facecolor="blue", edgecolor="black", alpha=0.7)
plt.savefig("AGhist.png")





