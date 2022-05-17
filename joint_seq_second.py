# -*- coding: utf-8 -*-
# 除去引物拼接六段
from sys import argv
import os

input,output=argv[1:]

file = open(input,"r")
out = open(output,"w")

for every_id in file:
    split_seq = every_id.split("-")
    seq_id = split_seq[0]
    seq = split_seq[1].split(",")
    seq1 = seq[5][21:143]
    seq2 = seq[4][17:147]
    seq3 = seq[3][19:143]
    seq4 = seq[2][21:147]
    seq5 = seq[1][24:128]
    seq6 = seq[0][18:147]
    out.write(seq_id + ">"+ seq1 + seq2 + seq3 + seq4 + seq5 + seq6 + "\n")


out.close()