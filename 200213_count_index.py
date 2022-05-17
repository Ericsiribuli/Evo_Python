from sys import argv
import os
import re
import time
import multiprocessing
import numpy as np

sample_name1,index_name,outfile=argv[1:]
sample_list = open(sample_name1,"r")
index_list = open(index_name,"r")
out = open(outfile,"w")
outlist = ""
for every in sample_list:
    every = every.strip()
    sample_num = every[1:3]
    file_name = "/mnt/data2/RAWDATA/Yang_fitness-landscape_illumina_all_data_2020-2-11/" + str(every) + "/" + str(every) + ".merged.fastq"
    fqfile = open(file_name,"r")
    outlist = outlist + sample_num + ":"
    for every_index in index_list:
        index_num = every_index.strip().split(',')[0]
        index = every_index.strip().split(',')[1]
        count = 0
        for line in fqfile:
            if index in line:
                count +=1
        fqfile.seek(0,0)
        outlist = outlist + "," + str(count) 
    index_list.seek(0,0)
    outlist = outlist + "\n"

out.write(str(outlist))

out.close()