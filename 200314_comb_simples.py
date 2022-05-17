from sys import argv
import os
import re
import time
import multiprocessing
import numpy as np
import pandas as pd
import math
from Bio import Seq
from Bio.Alphabet import IUPAC
from Bio.SeqRecord import SeqRecord
from collections import Counter

#将sample合在一起，然后umi和geno对应起来
threecells,sample1,sample2,sample3,wtfile,outfile=argv[1:]

file1 = open(sample1,"r")
file2 = open(sample2,"r")
file3 = open(sample3,"r")
geno_umi_file = open(threecells,"r")
out_wt = open(wtfile,"w")
out_single = open(outfile,"w")

sample1_dict = {}
sample2_dict = {}
sample3_dict = {}
geno_umi_dict = {}

wt = "ATGAGTAAAGGAGAAGAACTTTTCACTGGAGTTGTCCCAATTCTTGTTGAATTAGATGGTGATGTTAATGGGCACAAATTTTCTGTCAGTGGAGAGGGTGAAGGTGATGCAACATACGGAAAACTTACCCTTAAATTTATTTGCACTACTGGAAAACTACCTGTTCCATGGCCAACACTTGTCACTACTTTCACTTATGGTGTTCAATGCTTTTCAAGATACCCAGATCATATGAAACGGCATGACTTTTTCAAGAGTGCCATGCCCGAAGGTTATGTACAGGAAAGAACTATATTTTTCAAAGATGACGGGAACTACAAGACACGTGCTGAAGTCAAGTTTGAAGGTGATACCCTTGTTAATAGAATCGAGTTAAAAGGTATTGATTTTAAAGAAGATGGAAACATTCTTGGACACAAATTGGAATACAACTATAACTCACACAATGTATACATCATGGCAGACAAACAAAAGAATGGAATCAAAGTTAACTTCAAAATTAGACACAACATTGAAGATGGAAGCGTTCAACTAGCAGACCATTATCAACAAAATACTCCAATTGGCGATGGCCCTGTCCTTTTACCAGACAACCATTACCTGTCCACACAATCTGCCCTTTCGAAAGATCCCAACGAAAAGAGAGACCACATGGTCCTTCTTGAGTTTGTAACAGCTGCTGGGATTACACATGGCATGGATGAACTATACAAATAGGGCGCGCCACTTCTAA"

for i1 in file1:
    umi1 = i1.strip()[:20]
    sample1_dict[umi1] = sample1_dict.get(umi1,0) + 1

for i2 in file2:
    umi2 = i2.strip()[:20]
    sample2_dict[umi2] = sample2_dict.get(umi2,0) + 1

for i3 in file3:
    umi3 = i3.strip()[:20]
    sample3_dict[umi3] = sample3_dict.get(umi3,0) + 1


X,Y,Z = Counter(sample1_dict),Counter(sample2_dict),Counter(sample3_dict)
allsample_dict = dict(X+Y+Z)

for line in geno_umi_file:
    umi = line.strip().split("\t")[0]
    geno = line.strip().split("\t")[1]
    geno_umi_dict[umi] = geno

for every in allsample_dict:
    if every in geno_umi_dict.keys():
        geno = geno_umi_dict[every]
        mut_num = 0
        for i in range(733):
            if geno[i] != wt[i]:
                mut_num += 1
        if mut_num == 0:
            out_wt.write(every + "," + str(allsample_dict[every]) + "\n")
        if mut_num == 1:
            dna = str(geno)
            dna = Seq.Seq(dna, IUPAC.unambiguous_dna)
            mrna = dna.transcribe()
            protein = mrna.translate()
            for a in range(733):
                if geno[a] != wt[a]:
                    AApos = math.ceil((a+1)/3)
                    DNA2 = geno[3*AApos-3:3*AApos]
                    DNA3 = Seq.Seq(DNA2, IUPAC.unambiguous_dna)
                    MRNA2 = DNA3.transcribe()
                    Protein2 = MRNA2.translate()
                    out_single.write(every + "," + str(a+1) + "," + wt[a] + str(a+1) + geno[a] + "," + str(DNA2) + "," +str(AApos) + "," + str(Protein2)+ "," + str(allsample_dict[every]) + "\n")        

out_wt.close()
out_single.close()
