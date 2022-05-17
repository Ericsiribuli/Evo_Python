from sys import argv
import os
import re
import time
import multiprocessing
import numpy as np

sample_name1=argv[1]
sample_list = open(sample_name1,"r")
for every in sample_list:
    every = every.strip()
    sample_name = "/mnt/data2/disk/smrtanalysis/pacbio_data_new/new_illumina_data_2-14/Yang_fitness-landscape_illumina_all_data_2020-2-11/" + str(every) + "/" + str(every)
    os.system("gzip -d %s_1.fq.gz"%(sample_name))
    os.system("gzip -d %s_2.fq.gz"%(sample_name))
    os.system("SeqPrep -f %s_1.fq -r %s_2.fq -1 %s_1.SeqPrep.fastq.gz -2 %s_2.SeqPrep.fastq.gz -s %s.merged.fastq.gz -m 0"%(sample_name,sample_name,sample_name,sample_name,sample_name))
    os.system("gzip -d %s.merged.fastq.gz"%(sample_name))

sample_list.close()