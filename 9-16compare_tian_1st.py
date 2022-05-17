from sys import argv
import re
from collections import Counter
import numpy as np

inputfile,umi_1,out=argv[1:]

input_file = open(inputfile, "r")
first_umi = open(umi_1, "r")
outfile = open(out,"w")

wt = "GCGCAGACGAGTGCGGTGCAGCAAAAGCTGGCGGCGCTGGAGAAAAGCAGCGGAGGGCGGCTGGGCGTCGCGCTCATCGATACCGCAGATAATACGCAGGTGCTTTATCGCGGTGATGAACGCTTTCCAATGTGCAGTACCAGTAAAGTTATGGCGGCCGCGGCGGTGCTTAAGCAGAGTGAAACGCAAAAGCAGCTGCTTAATCAGCCTGTCGAGATCAAGCCTGCCGATCTGGTTAACTACAATCCGATTGCCGAAAAACACGTCAACGGCACAATGACGCTGGCAGAACTGAGCGCGGCCGCGTTGCAGTACAGCGACAATACCGCCATGAACAAATTGATTGCCCAGCTCGGTGGCCCGGGAGGCGTGACGGCTTTTGCCCGCGCGATCGGCGATGAGACGTTTCGTCTGGATCGCACTGAACCTACGCTGAATACCGCCATTCCCGGCGACCCGAGAGACACCACCACGCCGCGGGCGATGGCGCAGACGTTGCGTCAGCTTACGCTGGGTCATGCGCTGGGCGAAACCCAGCGGGCGCAGTTGGTGACGTGGCTCAAAGGCAATACGACCGGCGCAGCCAGCATTCGGGCCGGCTTACCGACGTCGTGGACTGTGGGTGATAAGACCGGCAGCGGCGACTACGGCACCACCAATGATATTGCGGTGATCTGGCCGCAGGGTCGTGCGCCGCTGGTTCTGGTGACCTATTTTACCCAGCCGCAACAGAACGCAGAGAGCCGCCGCGATGTGCTGGCTTCAGCGGCGAGAATCATCGCCGAAGGGCTG"
ccs_dict = {}

for line1 in input_file:
    umi = line1.strip().split(",")[0]
    geno = line1.strip().split(",")[1]
    ccs_dict[umi] = geno

for line in first_umi:
    mut_cluster = ""
    umi_first = line.strip().split(">")[1]
    num = line.strip().split(">")[0]
    if umi_first in ccs_dict:
        geno_first = ccs_dict[umi_first]
        for i in range(792):
            if geno_first[i] != wt[i]:
                mut_cluster = mut_cluster + wt[i] + str(i+1) + geno_first[i] + ","
        if mut_cluster == "":
            mut_cluster = "WT"
    else:
        mut_cluster = "NO"
    outfile.write(num + ":" + mut_cluster + "\n")

outfile.close()

