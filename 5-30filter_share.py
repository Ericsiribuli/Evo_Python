from sys import argv
import re
from collections import Counter
import numpy as np

# first_file,inputfile,out=argv[1:]

sum_file = open("input.txt", "r")

# first = open(first_file,"r")
# out_file = open(out,"w")

wt = "ATGAGTAAAGGAGAAGAACTTTTCACTGGAGTTGTCCCAATTCTTGTTGAATTAGATGGTGATGTTAATGGGCACAAATTTTCTGTCAGTGGAGAGGGTGAAGGTGATGCAACATACGGAAAACTTACCCTTAAATTTATTTGCACTACTGGAAAACTACCTGTTCCATGGCCAACACTTGTCACTACTTTCACTTATGGTGTTCAATGCTTTTCAAGATACCCAGATCATATGAAACGGCATGACTTTTTCAAGAGTGCCATGCCCGAAGGTTATGTACAGGAAAGAACTATATTTTTCAAAGATGACGGGAACTACAAGACACGTGCTGAAGTCAAGTTTGAAGGTGATACCCTTGTTAATAGAATCGAGTTAAAAGGTATTGATTTTAAAGAAGATGGAAACATTCTTGGACACAAATTGGAATACAACTATAACTCACACAATGTATACATCATGGCAGACAAACAAAAGAATGGAATCAAAGTTAACTTCAAAATTAGACACAACATTGAAGATGGAAGCGTTCAACTAGCAGACCATTATCAACAAAATACTCCAATTGGCGATGGCCCTGTCCTTTTACCAGACAACCATTACCTGTCCACACAATCTGCCCTTTCGAAAGATCCCAACGAAAAGAGAGACCACATGGTCCTTCTTGAGTTTGTAACAGCTGCTGGGATTACACATGGCATGGATGAACTATACAAATAGGGCGCGCCACTTCTAA"
ccs_dict = {}
for every in sum_file:
    if len(every)>40:
        geno = every.strip().split(" ")[0].split("_")[1]
        umi = every.strip().split(" ")[1]
        if umi in ccs_dict:
            ccs_dict[umi].append(geno)
        else:
            ccs_dict[umi] = [geno]

last_dict = {}
for line in ccs_dict:
    number_well = 0
    mut_dict = {}
    number_mut = 0
    if len(np.unique(ccs_dict[line]))==1:
        mut = ""
        number_well = len(ccs_dict[line])
        geno_myy = "".join(np.unique(ccs_dict[line]))
        if geno_myy == wt:
            last_dict[line] = wt + "," + "none" + "," + "0" + "," + str(number_well)
        else:
            mut_dict[geno_myy] = []
            for i in range(733):
                if geno_myy[i] != wt[i]:
                    mut_cluster = wt[i] + str(i) + geno_myy[i]
                    mut_dict[geno_myy].append(mut_cluster)
            number_mut = len(mut_dict[geno_myy])
            last_dict[line] = geno_myy + "," + str(mut_dict[geno_myy]) + "," + str(number_mut) + "," + str(number_well)
    else:
        mut_dict = {}
        geno_list = ccs_dict[line]
        geno_num = len(geno_list)
        all_mut = []
        mutlen_dict= {}
        for geno_i in geno_list:
            mut_cluster = ""
            if geno_i == wt:
                if geno_i in mut_dict:
                    mut_dict[geno_i].append('wt')
                else:
                    mut_dict[geno_i] = ['wt']
            else:
                if geno_i in mut_dict:
                    for i in range(733):
                        if geno_i[i] != wt[i]:
                            mut_cluster = wt[i] + str(i) + geno_i[i]
                            mut_dict[geno_i].append(mut_cluster)
                else:
                    mut_dict[geno_i] = []
                    for i in range(733):
                        if geno_i[i] != wt[i]:
                            mut_cluster = wt[i] + str(i) + geno_i[i]
                            mut_dict[geno_i].append(mut_cluster)
            mutlen_dict[geno_i] = len(np.unique(mut_dict[geno_i]))       #????????????geno?????????????????????????????????????????????geno

        for en in mut_dict:
            all_mut = all_mut + mut_dict[en]              #?????????????????????list

        number_wt = all_mut.count('wt')
        if number_wt >= geno_num *0.55:
            last_dict[line] = wt + "," + "none" + "," + "0" + "," + str(number_wt)
        else:
            # mutlen_dict.pop(wt)
            # min_len_mut = int(mutlen_dict[min(mutlen_dict, key=mutlen_dict.get)])  #??????????????????
            # print(mutlen_dict)
            mut_freq = Counter(all_mut)
            L = sorted(mut_freq.items(),key=lambda item:item[1],reverse=True)
            # L = L[:min_len_mut]   #????????????????????????mut
            dictdata = {}
            mut_list = []     #???????????????mut??????????????????list??????????????????geno???mut?????????????????????
            for each in L:
                dictdata[each[0]] = each[1]
                if each[1] >= geno_num *0.55:
                    number_well = each[1]
                    mut_list.append(each[0])

            for k,v in mut_dict.items():     #lastdict????????????????????????
                if mut_list == v:
                    geno_myy = k
                    number_mut = len(mut_list)
                    last_dict[line] = geno_myy + "," + str(mut_list) + "," + str(number_mut) + "," + str(number_well)

# print(last_dict)

xxx = len(last_dict)
print("The number of umi oto is" + str(xxx) )

for last_umi in last_dict.keys():
    print(last_umi)
    print(last_umi + "," + last_dict[last_umi] + "\n")

for line in first:
    mut_cluster = ""
    umi_first = line.strip().split(">")[1]
    num = line.strip().split(">")[0]
    if umi_first in last_dict:
        ccs_geno = last_dict[umi_first]
        for i in range(733):
            if ccs_geno[i] != wt[i]:
                mut_cluster = mut_cluster + wt[i] + str(i) + ccs_geno[i] + ","        
    else:
        mut_cluster = "NO"
    out_file.write(num + ":" + mut_cluster + "\n")

first.close()
sum_file.close()
out_file.close()

    




