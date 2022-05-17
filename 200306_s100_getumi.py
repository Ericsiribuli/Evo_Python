from sys import argv
import os
import re
import time
import multiprocessing
import numpy as np
import regex

inputfile,outfile=argv[1:]

fqfile = open(inputfile,"r")
out_umifile = open(outfile,"w")
umi_re = "(?e)(?P<p1>TCGCTCTTATTGACCACACC){e<=1}(?P<umi1>[ATCG]{25})(?P<p2>GCTTCGGCAGCACATATACT){e<=1}"
for line in fqfile:
    umi_reg = regex.search(umi_re,line,flags=0)
    if umi_reg is not None:
        umi = umi_reg.groupdict()["umi1"]
        out_umifile.write(umi + "\n")
out_umifile.close()