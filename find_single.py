# -*- coding: utf-8 -*-


from sys import argv
import numpy as np

file = open("joint_seq.txt","r")
# out = open(output)

wild_type = "ATGAGTAAAGGAGAAGAACTTTTCACTGGAGTTGTCCCAATTCTTGTTGAATTAGATGGTGATGTTAATGGGCACAAATTTTCTGTCAGTGGAGAGGGTGAAGGTGATGCAACATACGGAAAACTTACCCTTAAATTTATTTGCACTACTGGAAAACTACCTGTTCCATGGCCAACACTTGTCACTACTTTCACTTATGGTGTTCAATGCTTTTCAAGATACCCAGATCATATGAAACGGCATGACTTTTTCAAGAGTGCCATGCCCGAAGGTTATGTACAGGAAAGAACTATATTTTTCAAAGATGACGGGAACTACAAGACACGTGCTGAAGTCAAGTTTGAAGGTGATACCCTTGTTAATAGAATCGAGTTAAAAGGTATTGATTTTAAAGAAGATGGAAACATTCTTGGACACAAATTGGAATACAACTATAACTCACACAATGTATACATCATGGCAGACAAACAAAAGAATGGAATCAAAGTTAACTTCAAAATTAGACACAACATTGAAGATGGAAGCGTTCAACTAGCAGACCATTATCAACAAAATACTCCAATTGGCGATGGCCCTGTCCTTTTACCAGACAACCATTACCTGTCCACACAATCTGCCCTTTCGAAAGATCCCAACGAAAAGAGAGACCACATGGTCCTTCTTGAGTTTGTAACAGCTGCTGGGATTACACATGGCATGGATGAACTATACAAATAGGGCGCGCCACTTCTAA"
wild_type_num = 0
single_mut_num = 0
codon_dict = {} 
single_mut = ""
for every_id in file:
    every = every_id.split(">")
    seq_id = every[0]
    seq = every[1][2:735]
    same_num = 0
    if seq == wild_type:
        wild_type_num = wild_type_num + 1
    else:
        for i in range(733):
            if seq[i] == wild_type[i]:
                same_num = same_num + 1
    if same_num == 732:
        single_mut = single_mut + "," + seq
        single_mut_num = single_mut_num +1

single_mut = single_mut.split(",")
single_mut_nq = np.unique(single_mut)
single_mut_nq_num=len(single_mut_nq)
# for a in range(733):
#     for every_single_mut in single_mut_nq:
#         if a in codon_dict:
#             if every_single_mut[a] != wild_type[a]:
#                 codon_dict[a] = codon_dict[a] + 1
#         else:
#             if every_single_mut[a] != wild_type[a]:
#                 codon_dict[a] = 1

            

print('The number of wildtype is',wild_type_num)
print('The number of single mutation is',single_mut_num)
print('The number of single mutation  np is',single_mut_nq_num)    
