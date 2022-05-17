from sys import argv
import os
import re
import time
import multiprocessing
import numpy as np
import regex

sample_name1=argv[1]
sample_list = open(sample_name1,"r")
for every in sample_list:
    every = every.strip()
    file_name = "/mnt/data2/disk/smrtanalysis/pacbio_data_new/new_illumina_data_2-14/Yang_fitness-landscape_illumina_all_data_2020-2-11/" + str(every) + "/" + str(every)
    fqfile = open(file_name + ".merged.fastq","r")
    out_umifile = open(file_name + "_umi.txt","w")
    umi_re = "(?e)(?P<p1>TCGCTCTTATTGACCACACC){e<=1}(?P<umi1>[ATCG]{25})(?P<p2>GCTTCGGCAGCACATATACT){e<=1}"
    for line in fqfile:
        umi_reg = regex.search(umi_re,line,flags=0)
        if umi_reg is not None:
            umi = umi_reg.groupdict()["umi1"]
            out_umifile.write(umi + "\n")
    out_umifile.close()


sample_list.close()