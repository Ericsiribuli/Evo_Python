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

outfile=argv[1]
out = open(outfile,"w")

wt = "TCATATACCAGTAGAGCTGAGACTCATGCAAGTCCGGTTGCATCGAAACTTTTACGTTTAATGGATGAAAAGAAGACCAATTTGTGTGCTTCTCTTGACGTTCGTTCGACTGATGAGCTATTGAAACTTGTTGAAACGTTGGGTCCATACATTTGCCTTTTGAAAACACACGTTGATATCTTGGATGATTTCAGTTATGAGGGTACTGTCGTTCCATTGAAAGCATTGGCAGAGAAATACAAGTTCTTGATATTTGAGGACAGAAAATTCGCCGATATCGGTAACACAGTCAAATTACAATATACATCGGGCGTTTACCGTATCGCAGAATGGTCTGATATCACCAACGCCCACGGGGTTACTGGTGCTGGTATTGTTGCTGGCTTGAAACAAGGTGCGCAAGAGGTCACCAAAGAACCAAGGGGATTATTGATGCTTGCTGAATTGTCTTCCAAGGGTTCTCTAGCACACGGTGAATATACTAAGGGTACCGTTGATATTGCAAAGAGTGATAAAGATTTCGTTATTGGGTTCATTGCTCAGAACGATATGGGAGGAAGAGAAGAAGGGTTTGATTGGCTAATCATGACCCCAGGTGTAGGTTTAGACGACAAAGGCGATGCATTGGGTCAGCAGTACAGAACCGTCGACGAAGTTGTAAGTGGTGGATCAGATATCATCATTGTTGGCAGAGGACTTTTCGCCAAGGGTAGAGATCCTAAGGTTGAAGGTGAAAGATACAGAAATGCTGGATGGGAAGCGTACCAAAAG"

def multi_sub(string,p,c):
        new = []
        for s in string:
            new.append(s)
        for index,point in enumerate(p):
            new[point] = c[index]
        return ''.join(new)


for index,bp in enumerate(wt):
    mut_box = ['A','T','C','G']
    mut_box.remove(bp)
    for rest in mut_box:
        pos_list = []
        sub_list = []
        pos_list.append(index)
        sub_list.append(rest)
        geno = multi_sub(wt,pos_list,sub_list)
        dna = Seq.Seq(geno, IUPAC.unambiguous_dna)
        mrna = dna.transcribe()
        protein = mrna.translate()
        out.write('>' + bp + str(index+13) + rest + '\n' + str(protein) + '\n')

out.close()


