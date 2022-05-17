# -*- coding: utf-8 -*-
#拆分one_two_three... 到 _one,_two,_three的格式

from sys import argv
import os
import numpy as np
inputfile,output=argv[1:]

file1 = open(inputfile,"r")
out = open(output,"w")
cluster = ""

for line in file1:
    if line[:2] == "id":
        if cluster == "":
            a = line.split("-")
            id = a[0]
            first_cluster = a[1]
            cluster = first_cluster
        else:
            cluster_total = cluster.strip().replace("\n","").replace("1","").split(",")
            cluster1 = np.unique(cluster_total)
            pra = ""
            for every in cluster1:              #将文件拆成umi与单个库的格式
                # print(every)
                if "one" in every:
                    pra = pra + every[:20]+"_one,"
                if "two" in every:
                    pra = pra + every[:20]+"_two,"
                if "three" in every:
                    pra = pra + every[:20]+"_three,"
                if "four" in every:
                    pra = pra + every[:20]+"_four,"
                if "five" in every:
                    pra = pra + every[:20]+"_five,"
                if "six" in every:
                    pra = pra + every[:20]+"_six,"
            out.write(id+"-"+pra+"\n")
            a = line.split("-")
            first_cluster = a[1]
            id = a[0]
            cluster = first_cluster
    else:
        cluster = cluster + line
#最后一个cluster进行最后的补充添加（因为没有下一个id进行返回）
cluster_total = cluster.strip().replace("\n","").replace("1","").split(",")
cluster1 = np.unique(cluster_total)
pra = ""
for every in cluster1:
    if "one" in every:
        pra = pra + every[:20]+"_one,"
    if "two" in every:
        pra = pra + every[:20]+"_two,"
    if "three" in every:
        pra = pra + every[:20]+"_three,"
    if "four" in every:
        pra = pra + every[:20]+"_four,"
    if "five" in every:
        pra = pra + every[:20]+"_five,"
    if "six" in every:
        pra = pra + every[:20]+"_six,"
out.write(id+"-"+pra+"\n")


out.close()

    

