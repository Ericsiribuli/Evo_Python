from sys import argv
import os
import re
import time
import multiprocessing
import numpy as np

input_code,input_awk,outfile=argv[1:]

input1 = open(input_code,"r")
input2 = open(input_awk,"r")
out = open(outfile,"w")

code_list = []
awk_list = []
for r in input1:
    if r[0]==">":
        code_list.append(r[1:])

for a in input2:
    if a[0]==">":
        awk_list.append(a[1:])

out.write("\n" + "awk not in code:" + "\n")

for every in awk_list:
    if every in code_list:
        pass
    else:
        out.write(every + ",,")

out.write("\n" + "code not in awk:" + "\n")

for every2 in code_list:
    if every2 in awk_list:
        pass
    else:
        out.write(every2 + ",,")

out.close()



def multi_sub(string,p,c):
        new = []
        for s in string:
            new.append(s)
        for index,point in enumerate(p):
            new[point] = c[index]
        return ''.join(new)

xxx = [3,5,8]
string = 'ATCGATCGAAA * JGAAAGYGJYGA'
cc = ['x','x','x']

print(string.split(" "))

for index,point in enumerate(xxx):
    print(str(index) + "," + str(point))


print(multi_sub(string,xxx,cc))




geno_umi_file = open('sp_gene.txt',"r")
wt = "ATGAGTAAAGGAGAAGAACTTTTCACTGGAGTTGTCCCAATTCTTGTTGAATTAGATGGTGATGTTAATGGGCACAAATTTTCTGTCAGTGGAGAGGGTGAAGGTGATGCAACATACGGAAAACTTACCCTTAAATTTATTTGCACTACTGGAAAACTACCTGTTCCATGGCCAACACTTGTCACTACTTTCACTTATGGTGTTCAATGCTTTTCAAGATACCCAGATCATATGAAACGGCATGACTTTTTCAAGAGTGCCATGCCCGAAGGTTATGTACAGGAAAGAACTATATTTTTCAAAGATGACGGGAACTACAAGACACGTGCTGAAGTCAAGTTTGAAGGTGATACCCTTGTTAATAGAATCGAGTTAAAAGGTATTGATTTTAAAGAAGATGGAAACATTCTTGGACACAAATTGGAATACAACTATAACTCACACAATGTATACATCATGGCAGACAAACAAAAGAATGGAATCAAAGTTAACTTCAAAATTAGACACAACATTGAAGATGGAAGCGTTCAACTAGCAGACCATTATCAACAAAATACTCCAATTGGCGATGGCCCTGTCCTTTTACCAGACAACCATTACCTGTCCACACAATCTGCCCTTTCGAAAGATCCCAACGAAAAGAGAGACCACATGGTCCTTCTTGAGTTTGTAACAGCTGCTGGGATTACACATGGCATGGATGAACTATACAAATAGGGCGCGCCACTTCTAA"
def multi_sub(string,p,c):
        new = []
        for s in string:
            new.append(s)
        for index,point in enumerate(p):
            new[point] = c[index]
        return ''.join(new)

geno_umi_dict = {}

for line in geno_umi_file:
    pos_list = []
    sub_list = []
    umi = line.strip().split(" * ")[1]
    mut = line.strip().split(" * ")[0].split(" ")[1:]
    if "".join(mut) == "WT":
        for every_umi in umi.strip().split(" "):
            geno_umi_dict[every_umi] = wt
    else:
        for every_mut in mut:
            pos_list.append(int(every_mut[1:-1]) -1)
            sub_list.append(every_mut[-1])
        geno = multi_sub(wt,pos_list,sub_list)
        for every_umi in umi.strip().split(" "):
            geno_umi_dict[every_umi] = geno

print(geno_umi_dict)