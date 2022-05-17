from sys import argv
import os
import re
import time
import multiprocessing
import numpy as np

rawfile,filename,header,input_f,input_r,out_last=argv[1:]

os.system("blasr --bam --out %s.blasr.new.bam %s ref_nnn_gfp.fasta"%(filename,rawfile))
os.system("samtools view -h -o %s.blasr.new.sam %s.blasr.new.bam"%(filename,filename))
os.system("head -7 %s.blasr.new.sam > header.txt"%(filename))
os.system("samtools view %s.blasr.new.bam | awk '$2==0' > %s_f_pre.sam"%(filename,filename))
os.system("samtools view %s.blasr.new.bam | awk '$2==16' > %s_r_pre.sam"%(filename,filename))
os.system("cat %s %s_f_pre.sam > %s_f.sam"%(header,filename,filename))
os.system("cat %s %s_r_pre.sam > %s_r.sam"%(header,filename,filename))
os.system("samtools view -b -S %s_f.sam > %s_f.bam"%(filename,filename))
os.system("samtools view -b -S %s_r.sam > %s_r.bam"%(filename,filename))
os.system("ccs --reportFile=ccs_report.txt --minLength=900 --maxLength=1600 --minPasses=5 --num-threads 30 --minPredictedAccuracy=0.95 --logFile=mylog.txt %s_f.bam ./%s_f_ccs.bam"%(filename,filename))
os.system("ccs --reportFile=ccs_report.txt --minLength=900 --maxLength=1600 --minPasses=5 --num-threads 30 --minPredictedAccuracy=0.95 --logFile=mylog.txt %s_r.bam ./%s_r_ccs.bam"%(filename,filename))
os.system("samtools view -h -o %s_f_ccs.sam %s_f_ccs.bam"%(filename,filename))
os.system("samtools view -h -o %s_r_ccs.sam %s_r_ccs.bam"%(filename,filename))

inputf = open(input_f,"r")
inputr = open(input_r,"r")
outfile = open(out_last,"w")
umi_geno = {}
geno_pattern=re.compile("CAAACAAA\w{733}ATAAGCG")
umi_pattern=re.compile("ACCACACC\w{20}GCTTCG")
mud_dict={"A":"T","T":"A","C":"G","G":"C"}
Reverse_complemrnt= lambda x:"".join([mud_dict[i] for i in x][::-1])
ccs_dict1 = {}
ccs_dict3 = {}
for r in inputr:
    if r[0]=="m":
        r = r.strip()
        r_line_list=r.split()
        r_seq=r_line_list[9]
        r_reverse=Reverse_complemrnt(r_seq)
        geno2=re.search(geno_pattern,r_reverse,flags=0)        
        umi2=re.search(umi_pattern,r_reverse,flags=0)
        if geno2 is not None and umi2 is not None:
            geno3 = geno2.group()[8:741]
            umi3 = umi2.group()[8:28]
            zwm_number2 = r.split("/")[1]
            ccs_dict1[zwm_number2]=["r" + "_" + geno3 + " " + umi3 + " " + umi3]

for f in inputf:
    if f[0]=="m":
        f = f.strip()
        f_line_list=f.split()
        f_seq=f_line_list[9]
        geno=re.search(geno_pattern,f_seq,flags=0)
        umi=re.search(umi_pattern,f_seq,flags=0)
        if geno is not None and umi is not None:
            geno1 = geno.group()[8:741]
            umi1 = umi.group()[8:28]
            zwm_number = f.split("/")[1]
            if zwm_number in ccs_dict1.keys():
                ccs_dict1[zwm_number].append("f" + "_" + geno1 + " " + umi1 + " " + umi1)
            else:
                ccs_dict1[zwm_number]=["f" + "_" + geno1 + " " + umi1 + " " + umi1]

ccs_cluster = ""
for every in ccs_dict1:
    if len(ccs_dict1[every]) == 1:
        geno2 = "".join(ccs_dict1[every])
        ccs_cluster = ccs_cluster + ">" + every + "\n" + geno2 + "\n"
    else:
        geno2 = "\n".join(ccs_dict1[every])
        ccs_cluster = ccs_cluster + ">" + every + "\n" + geno2 + "\n"

pra_old54061 = ccs_cluster.strip(">").split(">")
for line in pra_old54061:
    zwm_name = line.strip().split("\n")[0]
    if line.find("r") == -1:
        line2 = line.strip().split("\n")
        f_geno = line.strip().split("\n")[1]
        outfile.write(">" + zwm_name + "\n" + "none" + "\n" + f_geno + "\n")
    if line.find("f") == -1:
        line2 = line.strip().split("\n")
        r_geno = line.strip().split("\n")[1]
        outfile.write(">" + zwm_name + "\n" + r_geno + "\n" + "none" + "\n")
    if line.find("r") != -1 and line.find("f") != -1:
        outfile.write(">" + line)


outfile.close()

