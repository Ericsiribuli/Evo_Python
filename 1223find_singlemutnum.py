from sys import argv
import numpy as np
#找单点突变覆盖度 数量
infile,=argv[1:]

file3st = open(infile,"r")
wt="ATGAGTAAAGGAGAAGAACTTTTCACTGGAGTTGTCCCAATTCTTGTTGAATTAGATGGTGATGTTAATGGGCACAAATTTTCTGTCAGTGGAGAGGGTGAAGGTGATGCAACATACGGAAAACTTACCCTTAAATTTATTTGCACTACTGGAAAACTACCTGTTCCATGGCCAACACTTGTCACTACTTTCACTTATGGTGTTCAATGCTTTTCAAGATACCCAGATCATATGAAACGGCATGACTTTTTCAAGAGTGCCATGCCCGAAGGTTATGTACAGGAAAGAACTATATTTTTCAAAGATGACGGGAACTACAAGACACGTGCTGAAGTCAAGTTTGAAGGTGATACCCTTGTTAATAGAATCGAGTTAAAAGGTATTGATTTTAAAGAAGATGGAAACATTCTTGGACACAAATTGGAATACAACTATAACTCACACAATGTATACATCATGGCAGACAAACAAAAGAATGGAATCAAAGTTAACTTCAAAATTAGACACAACATTGAAGATGGAAGCGTTCAACTAGCAGACCATTATCAACAAAATACTCCAATTGGCGATGGCCCTGTCCTTTTACCAGACAACCATTACCTGTCCACACAATCTGCCCTTTCGAAAGATCCCAACGAAAAGAGAGACCACATGGTCCTTCTTGAGTTTGTAACAGCTGCTGGGATTACACATGGCATGGATGAACTATACAAATAGGGCGCGCCACTTCTAA"
mut_num = 0
singlemut_num = 0
pos_mut = []
umi_geno_dic = {}
umi_toone_geno_num = 0
for line in file3st:
    geno = line.strip().split(",")[0]
    umi = line.strip().split(",")[1]
    if umi in umi_geno_dic:
        umi_geno_dic[umi].append(geno)
    else:
        umi_geno_dic[umi] = [geno]
    for i in range(733):
        if geno[i] != wt[i]:
            mut_num += 1
    if mut_num == 1:
        singlemut_num += 1        #单点突变数量
        for i in range(733):
            if geno[i] != wt[i]:
                pos_mut.append(str(i)+wt[i]+geno[i])

print("single_mut_num is" + " " + str(singlemut_num))
pos_mut_num = len(np.unique(pos_mut))
print("pos_mut_num is" + " " + str(pos_mut_num))
for every in umi_geno_dic:
    if len(umi_geno_dic[every]) == 1:
        umi_toone_geno_num += 1
print("The number of one umi whcih only has one geno is"+ " " + str(umi_toone_geno_num))

file3st.close()

