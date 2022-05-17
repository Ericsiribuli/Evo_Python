from sys import argv
import numpy as np

inputfile = open("90_precentage_data.txt","r")
outfile = open("single_pos_mut.txt","w") 
wt="CGCTGCTGCTGGGCAGCGCGCCGCTTTATGCGCAGACGAGTGCGGTGCAGCAAAAGCTGGCGGCGCTGGAGAAAAGCAGCGGAGGGCGGCTGGGCGTCGCGCTCATCGATACCGCAGATAATACGCAGGTGCTTTATCGCGGTGATGAACGCTTTCCAATGTGCAGTACCAGTAAAGTTATGGCGGCCGCGGCGGTGCTTAAGCAGAGTGAAACGCAAAAGCAGCTGCTTAATCAGCCTGTCGAGATCAAGCCTGCCGATCTGGTTAACTACAATCCGATTGCCGAAAAACACGTCAACGGCACAATGACGCTGGCAGAACTGAGCGCGGCCGCGTTGCAGTACAGCGACAATACCGCCATGAACAAATTGATTGCCCAGCTCGGTGGCCCGGGAGGCGTGACGGCTTTTGCCCGCGCGATCGGCGATGAGACGTTTCGTCTGGATCGCACTGAACCTACGCTGAATACCGCCATTCCCGGCGACCCGAGAGACACCACCACGCCGCGGGCGATGGCGCAGACGTTGCGTCAGCTTACGCTGGGTCATGCGCTGGGCGAAACCCAGCGGGCGCAGTTGGTGACGTGGCTCAAAGGCAATACGACCGGCGCAGCCAGCATTCGGGCCGGCTTACCGACGTCGTGGACTGTGGGTGATAAGACCGGCAGCGGCGACTACGGCACCACCAATGATATTGCGGTGATCTGGCCGCAGGGTCGTGCGCCGCTGGTTCTGGTGACCTATTTTACCCAGCCGCAACAGAACGCAGAGAGCCGCCGCGATGTGCTGGCTTCAGCGGCGAGAATCATCGCCGAAGGGCTGTAACCAGGCATCAAATAAAACGAAAGGCTCAGTCGAAAGACTGGGCCTTTCGTTTTATCTGTTGTTTGTCGGTGAACGCTCTCCTGAGTAGGACAAATCCGCCTTAATTAA"
# print(wt[932])
cluster = ""
for line in inputfile:
    if len(line) > 100:
        line = line.split("_")
        seq = line[1]
        cluster = cluster + seq
        
cluster2 = cluster.strip().split("\n")
cluster3 = np.unique(cluster2)
mut_num = 0
umi_geno_dic = {}
selected_seq = ""
for every in cluster3:
        geno = every.strip().split(" ")[0]
        umi = every.strip().split(" ")[1]
        if umi in umi_geno_dic:
                umi_geno_dic[umi].append(geno)
        else:
                umi_geno_dic[umi]=[geno]
# print(umi_geno_dic)
for a in umi_geno_dic:
        if len(umi_geno_dic[a]) == 1:
                selected_seq =selected_seq + str("".join(umi_geno_dic[a])) + " " + str(a) + "\n"
selected_seq2 = selected_seq.strip().split("\n")
# print(selected_seq2)
for x in selected_seq2:
        geno = x.strip().split(" ")[0]
        # print(geno)
        for i in range(932):
                # print(geno[i])
                if wt[i] != geno[i]:
                        mut_num += 1
        if mut_num == 1:
                for b in range(932):
                        if wt[b] != geno[b]:
                                outfile.write(str(b) +","+ str(wt[b]) +","+ str(geno[b]) + "\n")
        mut_num = 0
                
inputfile.close()
outfile.close()
