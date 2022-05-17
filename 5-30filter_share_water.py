from sys import argv
import re
from collections import Counter
import numpy as np

first_file,inputfile,out=argv[1:]

sum_file = open(inputfile, "r")
first = open(first_file,"r")
out_file = open(out,"w")

wt = "ACATAAACAAACAAAATGAGTAAAGGAGAAGAACTTTTCACTGGAGTTGTCCCAATTCTTGTTGAATTAGATGGTGATGTTAATGGGCACAAATTTTCTGTCAGTGGAGAGGGTGAAGGTGATGCAACATACGGAAAACTTACCCTTAAATTTATTTGCACTACTGGAAAACTACCTGTTCCATGGCCAACACTTGTCACTACTTTCACTTATGGTGTTCAATGCTTTTCAAGATACCCAGATCATATGAAACGGCATGACTTTTTCAAGAGTGCCATGCCCGAAGGTTATGTACAGGAAAGAACTATATTTTTCAAAGATGACGGGAACTACAAGACACGTGCTGAAGTCAAGTTTGAAGGTGATACCCTTGTTAATAGAATCGAGTTAAAAGGTATTGATTTTAAAGAAGATGGAAACATTCTTGGACACAAATTGGAATACAACTATAACTCACACAATGTATACATCATGGCAGACAAACAAAAGAATGGAATCAAAGTTAACTTCAAAATTAGACACAACATTGAAGATGGAAGCGTTCAACTAGCAGACCATTATCAACAAAATACTCCAATTGGCGATGGCCCTGTCCTTTTACCAGACAACCATTACCTGTCCACACAATCTGCCCTTTCGAAAGATCCCAACGAAAAGAGAGACCACATGGTCCTTCTTGAGTTTGTAACAGCTGCTGGGATTACACATGGCATGGATGAACTATACAAATAGGGCGCGCCACTTCTAAATAAGCGAATTTCTTATGATTTATGATTTTTATTATTAAATAAGTTATAAAAAAAATAAGTGTATACAAATTTTAAAGTGACTCTTAGGTTTTAAAACGAAAATTCTTATTCTTGAGTAACTCTTTCCTGTAGGTCAGGTTGCTTTCTCAGGTATAGTATGAGGTCGCTCTTATTGACCACACC"
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
    if len(np.unique(ccs_dict[line]))==1:
        geno_myy = "".join(np.unique(ccs_dict[line]))
        last_dict[line] = geno_myy
    else:
        mut_dict = {}
        geno_list = ccs_dict[line]
        geno_num = len(geno_list)
        all_mut = []
        mutlen_dict= {}
        for geno_i in geno_list:
            mut_cluster = ""
            if geno_i == wt:
                pass
            else:
                mut_dict[geno_i] = []
                for i in range(932):
                    if geno_i[i] != wt[i]:
                        mut_cluster = wt[i] + str(i) + geno_i[i]
                        mut_dict[geno_i].append(mut_cluster)
                mutlen_dict[geno_i] = len(mut_dict[geno_i])       #得到所有geno突变数量的长度，取出突变最短的geno
                all_mut = all_mut + mut_dict[geno_i]              #得到所有突变的list

        min_len_mut = int(mutlen_dict[min(mutlen_dict, key=mutlen_dict.get)])  #得到最短的值
        mut_freq = Counter(all_mut) 
        L = sorted(mut_freq.items(),key=lambda item:item[1],reverse=True)
        L = L[:min_len_mut]   #取出最小值数量的mut
        dictdata = {}
        for B in L:
            dictdata[B[0]] = B[1]
        exam = 0
        for x in dictdata:              #这些mut的数量是否都大于所有条数的60%
            if dictdata[x] < geno_num * 0.6:
                exam = 1
        mut_list = []     #讲符合了的mut取出组成一个list，去和之前的geno的mut比较，是否存在
        if exam == 0:
            for x in dictdata:
                mut_list.append(x)
        for k,v in mut_dict.items():     #lastdict得到最后的一对一
            if mut_list == v:
                last_dict[line] = k

xxx = len(last_dict)
print("The number of umi oto is" + str(xxx) )

for line in first:
    mut_cluster = ""
    umi_first = line.strip().split(">")[1]
    num = line.strip().split(">")[0]
    if umi_first in last_dict:
        ccs_geno = last_dict[umi_first]
        for i in range(932):
            if ccs_geno[i] != wt[i]:
                mut_cluster = mut_cluster + wt[i] + str(i) + ccs_geno[i] + ","        
    else:
        mut_cluster = "NO"
    out_file.write(num + ":" + mut_cluster + "\n")

first.close()
sum_file.close()
out_file.close()

    

