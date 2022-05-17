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
    umi_geno_my_dict[umi_myy] = ccs_dict[umi_myy]

for line in first:
    cluster = ""
    umi_first = line.strip().split(">")[1]
    num = line.strip().split(">")[0]
    if umi_first in umi_geno_my_dict:
        ccs_geno = umi_geno_my_dict[umi_first]
        for inn in ccs_geno:
            mut_cluster = ""
            for i in range(733):
                if inn[i] != wt[i]:
                    mut_cluster = mut_cluster + wt[i] + str(i) + inn[i] + ","
            if mut_cluster == "":
                mut_cluster = "WT"
            cluster = cluster + mut_cluster + "\n"

    else:
        cluster = "NO" + "\n"
    out.write(num + ":" + cluster + "\n")

first.close()
ccs.close()
out.close()

