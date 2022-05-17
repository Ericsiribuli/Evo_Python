# -*- coding: utf-8 -*-
#选出每一个库里每一个碱基质量最好的那一个组合视为标准序列

from sys import argv
import os
import time
import multiprocessing

inputfile,out=argv[1:]

# file=open(inputfile,"r")   
output=open(out,"w") 

def select(seq_x):
    last_x_seq = ""
    for i in range(147):                      #循环147次选出每个里面最好的
        best_seq = ""
        best_qual = 0
        best_sum_seq = 0
        codon_dict = {}
        for k in seq_x:
            kk =  k.split("_")
            seq = kk[0]
            qual = kk[1]
            # print(ord(qual[i]))
            sum_seq = 0    
            # print(qual)
            for every_qual in qual:                            #算出每一行的质量总和
                sum_seq = sum_seq + ord(every_qual)
            # print(codon_dict)
            if seq[i] in codon_dict:
                codon_dict[seq[i]][0] = codon_dict[seq[i]][0] + ord(qual[i])
                if sum_seq >= codon_dict[seq[i]][1]:
                    codon_dict[seq[i]][1] = sum_seq
            else:
                codon_dict[seq[i]] = [ord(qual[i])]
                codon_dict[seq[i]].append(sum_seq)
        dict_sorted=sorted(codon_dict.items(),key=lambda codon_dict:codon_dict[1],reverse=True)
        best_seq = dict_sorted[0][0]
        last_x_seq = last_x_seq + best_seq
    return last_x_seq

def dealwith_every(x):
    seq_split = x.strip().rstrip(",").split(">")
    # print(seq_split)
    seq_id = seq_split[0].replace("-one","")
    seq_one = seq_split[1].replace(",two","").split(",")
    seq_two = seq_split[2].replace(",three","").split(",")
    seq_three = seq_split[3].replace(",four","").split(",")
    seq_four = seq_split[4].replace(",five","").split(",")
    seq_five = seq_split[5].replace(",six","").split(",")
    seq_six = seq_split[6].split(",")

    toge = map(select,[seq_one,seq_two,seq_three,seq_four,seq_five,seq_six])
    last_cluster = ""
    for everyline in toge:
        last_cluster = last_cluster + everyline + "," 
    last_cluster = last_cluster.rstrip(",")
    last_cluster = seq_id + ">" + last_cluster
    return last_cluster

with open(inputfile,"r") as file:
    p = multiprocessing.Pool(processes=20)
    result = []
    for every_id in file:
        res = p.apply_async(dealwith_every,args=(every_id,))
        result.append(res)
    print("Waiting For All To End")
    p.close()                          #关闭进程池，不再加入新的进程
    p.join()                           #等待子进程结束
    print("ALL DONE")
    for every_geno in result:
        output.write(every_geno.get() + "\n")

output.close()