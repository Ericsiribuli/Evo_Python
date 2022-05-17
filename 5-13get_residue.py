from Bio import Seq
from Bio.Alphabet import IUPAC
from Bio.SeqRecord import SeqRecord
from Bio import SeqIO
from sys import argv
import numpy as np
#讲cell没有去掉一对多的原始文件，去掉一对多，再用氨基酸表得到突变位置改变后的氨基酸

ccs_file,out=argv[1:]
# first = open(first_file,"r")
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

for line in umi_geno_my_dict:
    new_geno = umi_geno_my_dict[line]
    mut_num = 0
    for i in range(733):
        if new_geno[i] != wt[i]:
            mut_num += 1
        if mut_num == 1:     #取单点突变
            dna = str(new_geno)
            dna = Seq.Seq(dna, IUPAC.unambiguous_dna)
            mrna = dna.transcribe()
            protein = mrna.translate()
            for a in range(733):
                if new_geno[a] != wt[a]:
                    AApos = a//3 + 1
                    DNA2 = new_geno[2*AApos-1,3*AApos]
                    DNA2 = Seq.Seq(DNA2, IUPAC.unambiguous_dna)
                    MRNA2 = DNA2.transcribe()
                    Protein2 = MRNA2.translate()
                    out.close(str(a) + "," + wt[a] + str(a) + ccs_geno[a] + "," + str(AApos) + "," + Protein2 + "\n")        

ccs.close()
out.close()