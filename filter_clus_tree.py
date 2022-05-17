# -*- coding: utf-8 -*-
#将tree筛选长度小于60且含有1-6的,并输出为fasta格式
import numpy as np
from sys import argv
import os

file1,out_umi=argv[1:]

file1=open(file1,"r")
out2=open(out_umi,"w")
cluster=""
for a in file1:
    a=a.strip()
    if a[:2]=="id":
        if "one" in cluster and "two" in cluster and "three" in cluster and "four" in cluster and "five" in cluster and "six" in cluster:
            cluster0=cluster.replace(":",",").replace("(1.0)","").replace(" ","")
            cluster1=cluster0.rstrip(",").split(",")
            cluster_last=np.unique(cluster1)          
            c=','.join(cluster_last)
            out2.write(id+":"+c+"\n")
        else:
            pass
        id=a.replace(" --","-")
        cluster=""
        i=0
    else:
        cluster=cluster+a
        i=i+1
        if i>=60:
            cluster=""
if "one" in cluster and "two" in cluster and "three" in cluster and "four" in cluster and "five" in cluster and "six" in cluster:
    cluster0=cluster.replace(":",",").replace("(1.0)","").replace(" ","")
    cluster1=cluster0.rstrip(",").split(",")
    cluster_last=np.unique(cluster1)
    c=",".join(cluster_last)
    out2.write("id"+":"+c+"\n")   

out2.close()