#-*-coding:utf-8 -*-
from sys import argv
import os
import re
import time
import multiprocessing
input,input0,input1=argv[1:]
os.system("samtools view -h -o %s.sam %s"%(input0,input))
f=open("%s.f.sam"%(input1[:-4]),"w")
r=open("%s.r.sam"%(input1[:-4]),"w")
with open("%s.sam"%(input0),"r") as sam_file:
    subreads_s_dict={}
    for read_line in sam_file:#将每一个zmw的subreads提取出来输出成一个sam文件
        read_line=read_line.strip()
        if read_line[0]=="m":
            
            read_line1_list=read_line.split()
            subreads_s_dict[read_line1_list[0]]=read_line
        else:
            f.write(read_line+"\n")
            r.write(read_line+"\n")
os.system("samtools view -h -o %s.sam %s"%(input1[:-4],input1))

mud_dict={"A":"T","T":"A","C":"G","G":"C"}
Reverse_complemrnt= lambda x:"".join([mud_dict[i] for i in x][::-1])
with open("%s.sam"%(input1[:-4]),"r") as input_bam:#把每一个zmw分成正负链两部分
        f_subreads_count=0
        r_subreads_count=0
        f_read_dict={}
        r_read_dict={}
        for bam_line in input_bam:
            bam_line=bam_line.strip()
            if bam_line[0]=="m":
                # line2=re.sub(r"\s+"," ",bam_line)
                line2_list=bam_line.split()
                # names=line2_list[1].split("/")
                # if len(line2_list[9])<=1600 and len(line2_list[9])>=900:
                if line2_list[1]=="16":
                    r.write(subreads_s_dict[line2_list[0]]+"\n")
                    # r_umi.write(">"+"m"+line2_list[0][-10:].replace("/","")+"\n"+line2_list[9]+"\n")  
                    # r_read_dict["m"+line2_list[0][-10:].replace("/","")]=line2_list[9]
                    # r_subreads_count+=1
                elif line2_list[1]=="0":
                    f.write(subreads_s_dict[line2_list[0]]+"\n")
                    # f_umi.write(">"+"m"+line2_list[0][-10:].replace("/","")+"\n"+line2_list[9]+"\n")
                    # f_read_dict["m"+line2_list[0][-10:].replace("/","")]=line2_list[9]
                    # f_subreads_count+=1
           
f.close()
r.close()
os.system("rm *%s.sam"%(input1[:-4]))
os.system("rm *%s.sam"%(input0))

def run_ccs(name):
    os.system("samtools view -bS %s.sam -o %s.bam"%(name[:-4],name[:-4]))
    os.system("ccs --min-length 900 --max-length 1600 -j 10 --min-passes 5 --log-file %s_ccs_report.txt %s.bam %s_ccs.bam"%(input0,name[:-4],name[:-4]))
    os.system("samtools view -h -o %s_ccs.sam %s_ccs.bam"%(name[:-4],name[:-4]))
f_r=[input1[:-4]+".f.sam",input1[:-4]+".r.sam"]
pp=multiprocessing.Pool(2)
qq=0

for file in f_r:
    ress=pp.apply_async(run_ccs,args=(file,))
     
print('Waiting for all subprocesses done...')
pp.close()
pp.join()
print('All subprocesses done.')
os.system("rm *%s.r.bam"%(input1[:-4]))
os.system("rm *%s.f.bam"%(input1[:-4]))
os.system("rm *%s.r.sam"%(input1[:-4]))
os.system("rm *%s.f.sam"%(input1[:-4]))

geno_pattern=re.compile("AACACACATAAACAAACAAA\w{733}ATAAGCGAATTTCTTATGAT")
umi_pattern=re.compile("TCGCTCTTATTGACCACACC\w{25}GCTTCGGCAGCACATATACT")
outfile=open("%s.result"%(input1[:-4]),"w")
with open("%s.r_ccs.sam"%(input1[:-4]),"r") as inputr:
    for r in inputr:    
        if r[0]=="m":
            r = r.strip()
            r_line_list=r.split()
            r_seq=r_line_list[9]
            zmwr=r_line_list[0].split("/")[1]
            r_reverse=Reverse_complemrnt(r_seq)
            # print(r_reverse)
            geno2=re.search(geno_pattern,r_reverse,flags=0)
            umi2=re.search(umi_pattern,r_reverse,flags=0)
            if geno2 is not None and umi2 is not None:
                # print("ok")
                geno3 = geno2.group()[20:753]
                umi3 = umi2.group()[20:45]
                outfile.write(">"+str(zmwr)+"r"+"\n"+"r_"+geno3+" "+umi3+"\n")
with open("%s.f_ccs.sam"%(input1[:-4]),"r") as inputf:          
    for f in inputf:
        if f[0]=="m":
            f = f.strip()
            f_line_list=f.split()
            f_seq=f_line_list[9]
            zmwf=f_line_list[0].split("/")[1]
            geno=re.search(geno_pattern,f_seq,flags=0)
            umi=re.search(umi_pattern,f_seq,flags=0)
            if geno is not None and umi is not None:
                # print("oko")
                geno1 = geno.group()[20:753]
                umi1 = umi.group()[20:45]
                outfile.write(">"+str(zmwf)+"f"+"\n"+"f_"+geno1+" "+umi1+"\n")
                

os.system("rm *%s.*_ccs.bam.pbi"%(input1[:-4]))
os.system("rm *%s.*_ccs.sam"%(input1[:-4]))
outfile.close()