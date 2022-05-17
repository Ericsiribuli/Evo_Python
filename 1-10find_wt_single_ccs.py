# -*- coding: utf-8 -*-


from sys import argv
import numpy as np

infile = open("Y_geno_umi_ccs.txt","r")
# out = open(output)

wild_type = "ATGAGTAAAGGAGAAGAACTTTTCACTGGAGTTGTCCCAATTCTTGTTGAATTAGATGGTGATGTTAATGGGCACAAATTTTCTGTCAGTGGAGAGGGTGAAGGTGATGCAACATACGGAAAACTTACCCTTAAATTTATTTGCACTACTGGAAAACTACCTGTTCCATGGCCAACACTTGTCACTACTTTCACTTATGGTGTTCAATGCTTTTCAAGATACCCAGATCATATGAAACGGCATGACTTTTTCAAGAGTGCCATGCCCGAAGGTTATGTACAGGAAAGAACTATATTTTTCAAAGATGACGGGAACTACAAGACACGTGCTGAAGTCAAGTTTGAAGGTGATACCCTTGTTAATAGAATCGAGTTAAAAGGTATTGATTTTAAAGAAGATGGAAACATTCTTGGACACAAATTGGAATACAACTATAACTCACACAATGTATACATCATGGCAGACAAACAAAAGAATGGAATCAAAGTTAACTTCAAAATTAGACACAACATTGAAGATGGAAGCGTTCAACTAGCAGACCATTATCAACAAAATACTCCAATTGGCGATGGCCCTGTCCTTTTACCAGACAACCATTACCTGTCCACACAATCTGCCCTTTCGAAAGATCCCAACGAAAAGAGAGACCACATGGTCCTTCTTGAGTTTGTAACAGCTGCTGGGATTACACATGGCATGGATGAACTATACAAATAGGGCGCGCCACTTCTAA"
wild_type_num = 0
single_mut_num = 0
codon_dict = {} 
single_mut_cluster = ""
for every_id in infile:
    every = every_id.strip().split(",")
    geno = every[1]
    umi = every[2]
    mut_num = 0
    if geno == wild_type:
        wild_type_num +=1
    else:
        for i in range(733):
            if geno[i] != wild_type[i]:
                mut_num +=1
        if mut_num == 1:
            single_mut_cluster = single_mut_cluster + "," + geno
            single_mut_num +=1

single_mut_cluster = single_mut_cluster.split(",")
single_mut_nq = np.unique(single_mut_cluster)
single_mut_nq_num=len(single_mut_nq)

            

print('The number of wildtype is',wild_type_num)
print('The number of single mutation is',single_mut_num)
print('The number of single mutation  np is',single_mut_nq_num)    

infile.close()