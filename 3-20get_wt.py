from sys import argv

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
        for a in range(733):
            if geno[a] != wt[a]:
                out_single.write(umi + "," + wt[a] + str(a) + geno[a] + "\n")

out_wt.close()
out_single.close()