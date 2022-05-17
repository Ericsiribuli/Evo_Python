# -*- coding: utf-8 -*-
#输出umi+genotype+quality_menssage
#2018-8-11


from sys import argv
import re
import numpy as np


read1_fq, read2_fq, out_read1_fq,= argv[1:]

forword_primer="TACCAGACAACCATTACCTGT"
f=forword_primer[2:6]
reverse_primer="TTAGTATATGTGCTGCCGAAGC"
r=reverse_primer[2:6]
r1 = open(read1_fq,'r')
r2 = open(read2_fq,'r')
out_r1 = open(out_read1_fq,'w')


umi_dict = {}
umi_qua_dict={}
pattern=re.compile("GAAGC....................GGTGT") #定义要取的正则表达式  
for index,line in enumerate(zip(r1,r2)):
    if index % 4 == 1:#取出序列这一行
        seq1 = line[0].strip()#genotype的序列
        seq2 = line[1].strip()
    if index % 4 == 3:#取出测序质量这一行
        quality1= line[0].strip()#genotype的质量
        # quality2= line[1].strip()
        seq_qua=seq1[3:]+"\t"+quality1[3:]
        if len(seq1[3:])==147:
            umi_vague=seq2[3:50]
            umi_pre=re.search(pattern,umi_vague,flags=0)
            if umi_pre is None:
                pass
            else:
                umi_two_side=umi_pre.group()#获得数据
                umi=umi_two_side[5:25]#提取出umi
                if umi in umi_dict.keys():
                    umi_dict[umi].append(seq_qua)
                else:
                    umi_dict[umi] = [seq_qua]
            

i=0
Total_unique=0
umi_L=[]
umi_muti_L=[]
o=[]
u=0
for k in umi_dict.keys():
    value_list=umi_dict[k]
    seq_list=[]
    quality_list=[]
    for val in value_list:
        seq_list.append(val[:147])#取出genotype的序列
        quality_list.append(val[148:])#取出quality的序列
    s = np.unique(seq_list)#去重
    umi_L_l=umi_dict[k]
    l=len(s)
    if l==1:#umi只对应单个genoytpe
        qua_dict={}
        for total_qua in quality_list:
            qua_sum=0
            for asc in total_qua:#统计quality的sum,并建成ASC码与总数值对应的字典
                qua_sum=qua_sum+ord(asc)
            if total_qua in qua_dict.keys():#建立字典并除去重复
                pass
            else:
                qua_dict[total_qua]=qua_sum
        soted_qua_dict=sorted(qua_dict.items(),key=lambda qua_dict:qua_dict[1],reverse=True)#对value排逆序
        max_quality_seq=soted_qua_dict[0][0]#得到质量最好的ASC码
        umi_L=len(umi_L_l)
        o.append(umi_L)
        Total_unique=Total_unique+umi_L
        u=u+1
        out_r1.write(k+":"+s[0]+"_"+max_quality_seq+","+"\n")
    else:#当一个umi对应多种genotype的时候
        m_umi_dict={}
        m_genotype_qua=""
        for iii in value_list:#建立同一个genotype对应多个质量的字典
            if iii[:147] in m_umi_dict.keys():
                m_umi_dict[iii[:147]].append(iii[148:])
            else:
                m_umi_dict[iii[:147]]=[iii[148:]]
        for m_value in m_umi_dict.keys():#对于每一个键——值，取质量最好的那个值
            m_u_geno=m_umi_dict[m_value]
            qua_m_dict={}
            for m_same in m_u_geno:#取出同一个genotype的质量序列
                qua_m_sum=0
                for asc_m in m_same:#统计quality的sum,并建成ASC码与总数值对应的字典
                    qua_m_sum=qua_m_sum+ord(asc_m)
                if m_same in qua_m_dict.keys():#建立字典并除去重复
                    pass
                else:
                    qua_m_dict[m_same]=qua_m_sum
            soted_qua_m_dict=sorted(qua_m_dict.items(),key=lambda qua_m_dict:qua_m_dict[1],reverse=True)#对value排逆序
            max_quality_seq_m=soted_qua_m_dict[0][0]#得到质量最好的ASC码
            m_genotype_qua=m_genotype_qua+m_value+"_"+max_quality_seq_m+","
        out_r1.write(k+":"+m_genotype_qua+"\n")




    
total=len(umi_dict.keys())#umi一共有多少种
pre_unique_umi=u/total
umi_unique_max=max(o)
# zuida_umi=max(umi_muti_L)#umi最大能匹配的genotype
print("rugu_exp_total:"+str(total)+"\n"+"unique_umi:"+"\t"+str(pre_unique_umi)+"\n"+"o:"+str(umi_unique_max)+"\n")



        
        



r1.close()
r2.close()        
out_r1.close()


