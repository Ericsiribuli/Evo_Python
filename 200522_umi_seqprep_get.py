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
    sample_name = "/mnt/data2/disk/smrtanalysis/pacbio_data_new/new_illumina_data_2-14/URA3_data/1.rawdata/" + str(every) + "/" + str(every)
    os.system("gzip -d %s_1.fq.gz"%(sample_name))
    os.system("gzip -d %s_2.fq.gz"%(sample_name))
    os.system("SeqPrep -f %s_1.fq -r %s_2.fq -1 %s_1.SeqPrep.fastq.gz -2 %s_2.SeqPrep.fastq.gz -s %s.merged.fastq.gz -m 0"%(sample_name,sample_name,sample_name,sample_name,sample_name))
    os.system("gzip -d %s.merged.fastq.gz"%(sample_name))
    fqfile = open(sample_name + ".merged.fastq","r")
    out_umifile = open(sample_name + "_umi.txt","w")
    umi_re = "(?e)(?P<p1>TCGCTCTTATTGACCACACC){e<=1}(?P<umi1>[ATCG]{25})(?P<p2>GCTTCGGCAGCACATATACT){e<=1}"
    for line in fqfile:
        umi_reg = regex.search(umi_re,line,flags=0)
        if umi_reg is not None:
            umi = umi_reg.groupdict()["umi1"]
            out_umifile.write(umi + "\n")
    out_umifile.close()

sample_list.close()