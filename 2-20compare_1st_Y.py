from sys import argv
import numpy as np
#一代和ccs进行对比

first_file,ccs_file,out=argv[1:]
first = open(first_file,"r")
ccs = open(ccs_file,"r")
out = open(out,"w")

wt = "ATGAGTAAAGGAGAAGAACTTTTCACTGGAGTTGTCCCAATTCTTGTTGAATTAGATGGTGATGTTAATGGGCACAAATTTTCTGTCAGTGGAGAGGGTGAAGGTGATGCAACATACGGAAAACTTACCCTTAAATTTATTTGCACTACTGGAAAACTACCTGTTCCATGGCCAACACTTGTCACTACTTTCACTTATGGTGTTCAATGCTTTTCAAGATACCCAGATCATATGAAACGGCATGACTTTTTCAAGAGTGCCATGCCCGAAGGTTATGTACAGGAAAGAACTATATTTTTCAAAGATGACGGGAACTACAAGACACGTGCTGAAGTCAAGTTTGAAGGTGATACCCTTGTTAATAGAATCGAGTTAAAAGGTATTGATTTTAAAGAAGATGGAAACATTCTTGGACACAAATTGGAATACAACTATAACTCACACAATGTATACATCATGGCAGACAAACAAAAGAATGGAATCAAAGTTAACTTCAAAATTAGACACAACATTGAAGATGGAAGCGTTCAACTAGCAGACCATTATCAACAAAATACTCCAATTGGCGATGGCCCTGTCCTTTTACCAGACAACCATTACCTGTCCACACAATCTGCCCTTTCGAAAGATCCCAACGAAAAGAGAGACCACATGGTCCTTCTTGAGTTTGTAACAGCTGCTGGGATTACACATGGCATGGATGAACTATACAAATAGGGCGCGCCACTTCTAA"
ccs_dict = {}
for every in ccs:
    if len(every)>40:
        geno = every.strip().split(" ")[0].split("_")[1]
        umi = every.strip().split(" ")[1]
        if umi in ccs_dict:
            ccs_dict[umi].append(geno)
        else:
            ccs_dict[umi] = [geno]

umi_geno_my_dict = {}
for umi_myy in ccs_dict:
    if len(np.unique(ccs_dict[umi_myy]))==1:
        geno_myy = "".join(np.unique(ccs_dict[umi_myy]))
        umi_geno_my_dict[umi_myy] = geno_myy


for line in first:
    mut_cluster = ""
    umi_first = line.strip().split(">")[1]
    num = line.strip().split(">")[0]
    if umi_first in umi_geno_my_dict:
        ccs_geno = umi_geno_my_dict[umi_first]
        for i in range(733):
            if ccs_geno[i] != wt[i]:
                mut_cluster = mut_cluster + wt[i] + str(i) + ccs_geno[i] + ","        
    else:
        mut_cluster = "NO"
    out.write(num + ":" + mut_cluster + "\n")

first.close()
ccs.close()
out.close()

