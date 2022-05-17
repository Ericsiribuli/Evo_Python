from sys import argv
import os
import re
import time
import multiprocessing
import numpy as np

input_file1_dict,input_file2_total,cpu,output_f,output_r,input_f,input_r,out_last=argv[1:]
cpu_number=int(cpu)
header=""
with open(input_file2_total,"r") as input_subreads:
    # count_reads=0
    for liness in input_subreads:
        liness=liness.strip()
        if liness[0]=="m":
            break
        else:
            header=header+liness+"\n"
start=time.time()

def blasr_subreads_to_ccs(zmw_single,read_list):#定义把每一个zmw的subredas通过blasr转换成ccs
    
    file1=open(zmw_single+".new.sam","w")
    file1.write(header)
    subreads_s_dict={}
    for read_line in read_list:#将每一个zmw的subreads提取出来输出成一个sam文件
        read_line1=re.sub(r"\s+"," ",read_line)
        read_line1_list=read_line1.split(' ')
        subreads_s_dict[read_line1_list[0]]=read_line
        file1.write(read_line+"\n")
    file1.close()#生成每一个zmw的sam文件
    os.system("samtools view -bS %s.new.sam -o %s.new.bam"%(zmw_single,zmw_single))
    os.system("blasr --bam --out %s.blasr.new.bam %s.new.bam ref_nnn_gfp.fasta"%(zmw_single,zmw_single))
    os.system("samtools view -h -o %s.blasr.new.sam %s.blasr.new.bam"%(zmw_single,zmw_single))
    with open("%s.blasr.new.sam"%(zmw_single),"r") as input_bam:#把每一个zmw分成正负链两部分
        f_list = []
        r_list = []
        for bam_line in input_bam:
            bam_line=bam_line.strip()
            if bam_line[0]=="m":
                line2=re.sub(r"\s+"," ",bam_line)
                line2_list=line2.split(" ")
                if line2_list[1]=="16" and len(line2_list[9])>900 and len(line2_list[9])<1600:
                    r_list.append(subreads_s_dict[line2_list[0]])
                elif line2_list[1]=="0" and len(line2_list[9])>900 and len(line2_list[9])<1600:
                    f_list.append(subreads_s_dict[line2_list[0]])
        f_list2= "\n".join(f_list)
        r_list2= "\n".join(r_list)
    os.system("rm %s*"%(zmw_single))
    return (f_list2,r_list2)
def parse(x):
    f_list3 = x[0]
    r_list3 = x[1]
    forward_file.write(f_list3 + "\n")
    reverse_file.write(r_list3 + "\n")

forward_file = open(output_f,"w")
reverse_file = open(output_r,"w")
forward_file.write(header)
reverse_file.write(header)
p=multiprocessing.Pool(cpu_number)
with open(input_file1_dict,"r") as input_dict:
    for subreads in input_dict:
        subreads=subreads.strip()
        subreads_list=subreads.split(" m ")
        all_subreads_list=subreads_list[1:] 
        res=p.apply_async(blasr_subreads_to_ccs,args=(subreads_list[0],all_subreads_list,),callback=parse)
    print('Waiting for all subprocesses done...')
    p.close()
    p.join()
    print('All subprocesses done.')
forward_file.close()
reverse_file.close()

os.system("sed '/^\s*$/d' 54061old_f.txt > 54061old_f.sam")
os.system("sed '/^\s*$/d' 54061old_r.txt > 54061old_r.sam")
os.system("samtools view -b -S 54061old_f.sam > 54061old_f.bam")
os.system("samtools view -b -S 54061old_r.sam > 54061old_r.bam")
os.system("ccs --reportFile=ccs_report.txt --minLength=900 --maxLength=1600 --minPasses=5 --numThreads 30 --minPredictedAccuracy=0.95 --logFile=mylog.txt /mnt/data/home/smrtanalysis/opt/pacbio/smrtlink/install/smrtlink-release_5.1.0.26412/bundles/smrttools/install/smrttools-release_5.1.0.26366/smrtcmds/bin/pacbio_new_yang/Y_3-18_old54061/54061old_f.bam ./54061old_f_ccs.bam")
os.system("ccs --reportFile=ccs_report.txt --minLength=900 --maxLength=1600 --minPasses=5 --numThreads 30 --minPredictedAccuracy=0.95 --logFile=mylog.txt /mnt/data/home/smrtanalysis/opt/pacbio/smrtlink/install/smrtlink-release_5.1.0.26412/bundles/smrttools/install/smrttools-release_5.1.0.26366/smrtcmds/bin/pacbio_new_yang/Y_3-18_old54061/54061old_r.bam ./54061old_r_ccs.bam")
os.system("samtools view -h -o 54061old_f_ccs.sam 54061old_f_ccs.bam")
os.system("samtools view -h -o 54061old_r_ccs.sam 54061old_r_ccs.bam")


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
            if umi3 in ccs_dict1.keys():
                ccs_dict1[umi3].append(zwm_number2 + "," + "r" + "," + geno3)
            else:
                ccs_dict1[umi3]=[zwm_number2 + "," + "r" + "," + geno3]

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
            if umi1 in ccs_dict1.keys():
                ccs_dict1[umi1].append(zwm_number + "," + "f" + "," + geno1)
            else:
                ccs_dict1[umi1]=[zwm_number + "," + "f" + "," + geno1]

ccs_cluster = ""
for every in ccs_dict1:
        if len(ccs_dict1[every]) == 1:
                geno2 = "".join(ccs_dict1[every])
                ccs_cluster = ccs_cluster + geno2 + "," + every + "\n"
        else:
                geno_list = ccs_dict1[every]
                first = geno_list[0].split(",")[2]
                cluster = ""
                for zwm_geno in geno_list[1:]:
                        if first != zwm_geno.split(",")[2]:
                                first = "wrong"
                                break
                        else: continue
                if first != "wrong":
                        for last_zwm_geno in geno_list:
                            ccs_cluster = ccs_cluster + last_zwm_geno + "," + every + "\n"

ccs_cluster = ccs_cluster.strip().strip("\n").split("\n")
for x in ccs_cluster:
    zwmname = x.split(",")[0]
    left = ",".join(x.split(",")[1:])
    if zwmname in ccs_dict3:
        ccs_dict3[zwmname].append(left)
    else:
        ccs_dict3[zwmname] = [left] 

for zwmname2 in ccs_dict3:
    if len(ccs_dict3[zwmname2]) ==1:
        cluster2 = "".join(ccs_dict3[zwmname2])
        outfile.write(">" + zwmname2 + "\n" + cluster2 + "\n")
    else:
        cluster2 = "\n".join(ccs_dict3[zwmname2])
        outfile.write(">" + zwmname2 + "\n" + cluster2 + "\n")

outfile.close()

