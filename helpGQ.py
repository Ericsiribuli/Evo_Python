#-*-coding:utf-8 -*-
#2018-11-19
#Pacbio_sequence analysis yang, find illumina_sequencing umi
from sys import argv
import os
import regex

input1,input2,output1,output2=argv[1:]
out1=open(output1,"w")
out2=open(output2,"w")
# out3=open(output3,"w")
# out3=open(output3,"w")
f_re="(?e)(?P<p1>TCGCTCTTATTGACCACACC){e<=1}(?P<umi_f>[ATCG]{25})(?P<p2>GCTTCGGCAGCACATATACT){e<=1}"
r_re="(?e)(?P<p3>AGTATATGTGCTGCCGAAGC){e<=1}(?P<umi_r>[ATCG]{25})(?P<p4>GGTGTGGTCAATAAGAGCGA){e<=1}"
f_re_alter="(?e)(?P<p5>TAGGACAAATCCGCC){e<=1}(?P<umi_f_alter>[ATCG]{20})(?P<p6>CTGCAGGCATGCCTCGAGATG){e<=1}"
r_re_alter="(?e)(?P<p7>CATCTCGAGGCATGCCTGCAG){e<=1}(?P<umi_r_alter>[ATCG]{20})(?P<p8>GGCGGATTTGTCCTA){e<=1}"

ref="CGTTTTATCTGTTGTTTGTCGGTGAACGCTCTCCTGAGTAGGACAAATCCGCCTTAATTAANNNNNNNNNNNNNNNNNNNNCTGCAGGCATGCATTTAAATCTCGAGATGCATGGCGCCTAACCTAAACTGACAGGC"
ref_rev="GCCTGTCAGTTTAGGTTAGGCGCCATGCATCTCGAGATTTAAATGCATGCCTGCAGNNNNNNNNNNNNNNNNNNNNTTAATTAAGGCGGATTTGTCCTACTCAGGAGAGCGTTCACCGACAAACAACAGATAAAACG"
# a="CTGCAGGCATGCCTCGAGATG"
mud_dict={"A":"T","T":"A","C":"G","G":"C","N":"N"}
reverComple=lambda s: "".join([mud_dict[c] for c in s])[::-1]

# print(reverComple(a))
with open(input1,"r") as r1,open(input2,"r") as r2:
    ilumi_umi_set=set()
    # ilumi_umi_list=[]
    count_read=0
    count_read_p=0
    for i,j in enumerate(zip(r1,r2)):
        if i % 4==1 :
            j0=j[0].strip()
            # j1=reverComple(j[1].strip())
            j1=j[1].strip()
            f_pre=regex.search(f_re,j0,flags=0)
            r_pre=regex.search(r_re,j1,flags=0)
            f_pre_alter=regex.search(f_re_alter,j0,flags=0)
            r_pre_alter=regex.search(r_re_alter,j1,flags=0)
            # count_read+=1
            if f_pre is not None and r_pre is not None:
                f=f_pre.groupdict()["umi_f"]
                r=reverComple(r_pre.groupdict()["umi_r"])
                # print(f,r)
                if f==r:
                    ilumi_umi_set.add(f)
                    count_read_p+=1
                    # print(f)
                    out1.write(f+"\n")
                """
            if f_pre is  None and r_pre is None and f_pre_alter is not None and r_pre_alter is not None:
                f_alter=f_pre_alter.groupdict()["umi_f_alter"]
                r_alter=reverComple(r_pre_alter.groupdict()["umi_r_alter"])
                # print(f,r)
                if f_alter==r_alter:
                    # ilumi_umi_set.add(f)
                    count_read_p+=1
                    # print(f)
                    out1.write(f_alter+"\n")
                    # ilumi_umi_list.append(f)
# print(len(ilumi_umi_set),count_read_p,count_read)
"""
out1.close()
with open(output1,"r") as input_illu:
    umi_set=set()
    umi_dict={}
    for line in input_illu:
        line=line.strip()
        if line in umi_dict.keys():
            umi_dict[line]=umi_dict[line]+1
        else:
            umi_dict[line]=1

for i in umi_dict.keys():
    out2.write(">"+i+"\n"+str(umi_dict[i])+" "+i+"\n")




out2.close()


grep AAAACAAAAATATAAAATAG "/mnt/data2/disk/smrtanalysis/pacbio_data_new/new_illumina_data_2-14/20202015_sample_data/TGY/s2-62_d7_num_umi.txt"
grep AAAACAAAAATATAAAATAG "/mnt/data2/disk/smrtanalysis/pacbio_data_new/new_illumina_data_2-14/20202015_sample_data/TGY/s3-63_d7_num_umi.txt"
grep AAAACAAAAATATAAAATAG "/mnt/data2/disk/smrtanalysis/pacbio_data_new/new_illumina_data_2-14/20202015_sample_data/TGY/s3-63_d7_num_umi.txt"

x = open("input.txt",'r')
for i in x:
    print(i.strip())