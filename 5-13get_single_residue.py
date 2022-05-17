from sys import argv
from Bio import Seq
from Bio.Alphabet import IUPAC
from Bio.SeqRecord import SeqRecord
from Bio import SeqIO
import math

inputfile,outwt,outsingle=argv[1:]

input_umi_geno = open(inputfile,"r")
out_wt = open(outwt,"w")
out_single = open(outsingle,"w")

wt = "ATGAGTAAAGGAGAAGAACTTTTCACTGGAGTTGTCCCAATTCTTGTTGAATTAGATGGTGATGTTAATGGGCACAAATTTTCTGTCAGTGGAGAGGGTGAAGGTGATGCAACATACGGAAAACTTACCCTTAAATTTATTTGCACTACTGGAAAACTACCTGTTCCATGGCCAACACTTGTCACTACTTTCACTTATGGTGTTCAATGCTTTTCAAGATACCCAGATCATATGAAACGGCATGACTTTTTCAAGAGTGCCATGCCCGAAGGTTATGTACAGGAAAGAACTATATTTTTCAAAGATGACGGGAACTACAAGACACGTGCTGAAGTCAAGTTTGAAGGTGATACCCTTGTTAATAGAATCGAGTTAAAAGGTATTGATTTTAAAGAAGATGGAAACATTCTTGGACACAAATTGGAATACAACTATAACTCACACAATGTATACATCATGGCAGACAAACAAAAGAATGGAATCAAAGTTAACTTCAAAATTAGACACAACATTGAAGATGGAAGCGTTCAACTAGCAGACCATTATCAACAAAATACTCCAATTGGCGATGGCCCTGTCCTTTTACCAGACAACCATTACCTGTCCACACAATCTGCCCTTTCGAAAGATCCCAACGAAAAGAGAGACCACATGGTCCTTCTTGAGTTTGTAACAGCTGCTGGGATTACACATGGCATGGATGAACTATACAAATAGGGCGCGCCACTTCTAA"

for line in input_umi_geno:
    umi = line.strip().split(",")[0]
    geno = line.strip().split(",")[1]
    mut_num = 0
    for i in range(733):
        if geno[i] != wt[i]:
            mut_num += 1
    if mut_num == 0:
        out_wt.write(umi + "\n")
    if mut_num == 1:
        dna = str(geno)
        dna = Seq.Seq(dna, IUPAC.unambiguous_dna)
        mrna = dna.transcribe()
        protein = mrna.translate()
        for a in range(733):
            if geno[a] != wt[a]:
                AApos = math.ceil((a+1)/3)
                DNA2 = geno[3*AApos-3:3*AApos]
                DNA3 = Seq.Seq(DNA2, IUPAC.unambiguous_dna)
                MRNA2 = DNA3.transcribe()
                Protein2 = MRNA2.translate()
                out_single.write(umi + "," + str(a+1) + "," + wt[a] + str(a+1) + geno[a] + "," + str(DNA2) + "," +str(AApos) + "," + str(Protein2) + "\n")        

out_wt.close()
out_single.close()

for a in range(10):
    print(a)

