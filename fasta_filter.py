# -*- coding: utf-8 -*-


from sys import argv
import os

input1,out1_fasta,out2,out3_filt_cluster=argv[1:]

file1=open(input1,"r")
out3_filt_cluster=open(out3_filt_cluster,"w")
for t in file1:
    a=t.split("-:")
    id=a[0]
    cluster=a[1]
    out1=open(out1_fasta,"w")
    # out1_fasta.truncate()
    dict={}
    umi_set=set()
    cluster_total = ""
    b=cluster.split(",")
    for c in b:
        out1.write(">"+c+"\n"+c[:20]+"\n")
    out1.close()
    os.system("slidesort_v1 -d 1 -i out1_fasta.fasta -j F -o out2.tree")
    file2=open(out2,"r")
    umi_total=""
    for every in file2:
        cluster_total = cluster_total + every
        line = every.strip().replace(",1","")
        umi_total = umi_total + "," + line
    line = umi_total.split(",")
    for every_umi in line:
        umi_set.add(every_umi)
    bef_num=len(umi_set)
    # print(bef_num)
    # r2=file2.read()
    # r3=str(r2)
    # r4=r3.replace("1","").replace("\n","")
    # r5=r4.rstrip(",").split(",")
    for i in line:
        if i in dict:
            dict[i]+=1
        else:
            dict[i]=1
    dict_sorted=sorted(dict.items(),key=lambda dict:dict[1],reverse=True)
    most_umi=dict_sorted[0][0]     #找到每一个cluster出现最多次的那个中心序列
    # print(dict_sorted)
    file2.seek(0)    #指针调初始
    pre_num=0
    for s in file2:
        if most_umi in s:
            pre_num = pre_num + 1
    if pre_num/bef_num >=0.5:
        out3_filt_cluster.write(id+"-"+cluster_total+"\n")

out3_filt_cluster.close()
