from sys import argv
import os
import re
import time
import multiprocessing
import numpy as np
import regex

sample_name1,index_name,outfile=argv[1:]
sample_list = open(sample_name1,"r")
index_list = open(index_name,"r")
out = open(outfile,"w")
outlist = ""
for every in sample_list:
    every = every.strip()
    sample_num = every[1:3]
    file_name = "/mnt/data2/disk/smrtanalysis/pacbio_data_new/new_illumina_data_2-14/Yang_fitness-landscape_illumina_all_data_2020-2-11/" + str(every) + "/" + str(every) + ".merged.fastq"
    fqfile = open(file_name,"r")
    outlist = outlist + sample_num + ","
    list_count = []
    for every_index in index_list:
        index_num = every_index.strip().split(',')[0]
        index = every_index.strip().split(',')[1]
        index_re = "(?e)" + str(index) + "{e<=1}"
        count = 0
        sample_reads_num = 0
        for line in fqfile:
            sample_reads_num +=1
            index_reg = regex.search(index_re,line,flags=0)
            if index_reg is not None:
                count +=1
        list_count.append(count)
        fqfile.seek(0,0)
        max_count = max(list_count)
    for count_one in list_count:
        if count_one == max_count:
            outlist = outlist + str(max_count) + ","
        else:
            outlist = outlist + str(count_one/max_count) + ","
    index_list.seek(0,0)
    outlist = outlist + str(sample_reads_num/4) + "\n"

out.write(str(outlist))

out.close()