# -*- coding: utf-8 -*-


from sys import argv
import re
import numpy as np
read1,read2,output= argv[1:]

r1 = open(read1,'r')
r2 = open(read2,'r')
out_r1 = open(output,'w')
dic_umi={}
pattern=re.compile('GAAGC\w{20}GGTGT')
       
for index,line in enumerate(zip(r1,r2)):
    
    if index % 4 == 1:
        genotype = line[0].strip()
        umi_raw = line[1].strip()
    if index % 4==3:
        qual_geno=line[0].strip() #质量
        seq_qual= genotype[3:]+'\t'+qual_geno[3:] #geno+quality
        if len(genotype)==150:
            umi2=re.search(pattern,umi_raw,flags=0) #.search和.match
            if umi2 is None:
                pass
            else:
                umi1=umi2.group() #获得数据?misunderstanding
                umi=umi1[5:25] #提取
                if umi in dic_umi:
                    dic_umi[umi].append(seq_qual)
                else:
                    dic_umi[umi]=[seq_qual]
# print(dic_umi)

#将一对一中选出质量最好的
#将seq与qual分别提出 qual要计算出ASC 后来一对一or一对多的时候方便选max

for z in dic_umi.keys():
    seq_qual_list=dic_umi[z]
    # print(seq_qual_list)
    seq_list=[]
    qual_list=[]
    for seq_qual in seq_qual_list:  #提取seq与qual
        seq_list.append(seq_qual[:147])
        qual_list.append(seq_qual[148:])
        # print(qual_list)
    x=np.unique(seq_list) #去重
    s=len(x)
    if s==1: #一对一的情况 取ASC总值
        dict_qual={}
        for qual in qual_list:
            qual_sum=0
            for asc in qual:
                qual_sum=qual_sum+ord(asc)
            if qual in dict_qual:
                pass
            else:
                dict_qual[qual]=qual_sum
        # print(dict_qual)
        sorted_qual_dict=sorted(dict_qual.items(),key=lambda dict_qual:dict_qual[1],reverse=True)
        # print(sorted_qual_dict)
        max_qual_seq=sorted_qual_dict[0][0] #逆排序取最大
        # print(max_qual_seq)
        # print(z)
        out_r1.write(z+":"+x[0]+"_"+max_qual_seq+","+"\n")
    
    else: #一对多的情况
        dict_m_seq={}
        
        m_best_geno_qual = ""
        for r in seq_qual_list:
            # print(seq_qual_list)
            if r[:147] in dict_m_seq:                          #建geno(不止一种)：qual(多个)的字典
                dict_m_seq[r[:147]].append(r[148:])             
            else:
                dict_m_seq[r[:147]]=[r[148:]]     
        for b in dict_m_seq.keys():
            dict_m_qual={}
            m_qual_list=dict_m_seq[b]
            m_qual_sum=0
            for m_qual in m_qual_list:                   #取出每一种geno对应的qual选最好
                for m_asc in m_qual:
                    m_qual_sum=m_qual_sum+ord(m_asc)                    
                if m_qual in dict_m_qual:
                    pass
                else:
                    dict_m_qual[m_qual]=m_qual_sum
            sorted_m_qual_dict=sorted(dict_m_qual.items(),key=lambda dict_m_qual:dict_m_qual[1],reverse=True)
            max_m_qual_seq=sorted_m_qual_dict[0][0]
            m_best_geno_qual=m_best_geno_qual+b+"_"+max_m_qual_seq+","
        out_r1.write(z+":"+m_best_geno_qual+"\n")


r1.close()
r2.close()        
out_r1.close()
            
            

