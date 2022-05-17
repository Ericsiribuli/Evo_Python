import re
from sys import argv
import os


#def将每个孔里的正负链拆分 并提出里面的序列
def sep(x):                    
    forward_blasr = ""
    reverse_blasr = ""
    for line in x.splitlines()[7:]:
        everysub=re.split(r'[ ]+',line.strip())
        if int(everysub[1]) == 0:
            forward_blasr = forward_blasr + ">" + everysub[0][21:27] + everysub[0][29:] + "\n" + everysub[9] + "\n" 
        elif int(everysub[1]) == 16:
            reverse_blasr = reverse_blasr + ">" + everysub[0][21:27] + everysub[0][29:] + "\n" + everysub[9] + "\n" 
    return forward_blasr,reverse_blasr

def select(seq):
    forward,reverse = sep(seq)
    # print(reverse)
    a = open("%s_umi.fasta"%(zwmname),"w")
    a.write(forward)
    a.close()
    ref_last = "TCAGGTTGCTTTCTCAGGTATAGTATGAGGTCGCTCTTATTGACCACACC"    #20N前的50bp
    for i in range(100):
        reference = open("%s_water_ref.fasta"%(zwmname),"w")
        reference.write(">ref" + "\n" + ref_last)
        reference.close()
        os.system("water -asequence %s_water_ref.fasta -bsequence %s_umi.fasta -gapopen 5 -gapextend 1 -aformat markx10 -outfile %s.water.txt"%(zwmname,zwmname,zwmname))
        genofile = open("%s_water_ref.fasta"%(zwmname),"r")         #打开输入文件
        genofile2 = genofile.read().strip(">").split(">")      
        num_A=0             #取出每一个最后的base 取最大值
        num_T=0
        num_G=0
        num_C=0
        waterfile = open("%s.water.txt","r"%(zwmname))
        for everywater in waterfile:         #对输出water文件分析
            if everywater.startswith(">0") or everywater.startswith(">1") or everywater.startswith(">2") or everywater.startswith(">3") or everywater.startswith(">4") or everywater.startswith(">5") or everywater.startswith(">6") or everywater.startswith(">7") or everywater.startswith(">8") or everywater.startswith(">9"):
                zwm_len = everywater.split(" ")[0][1:]      #找到能和原来文件对应的那一段名字找到geno
            if "al_stop" in everywater:
                base_pos = int(everywater.split(":")[1].strip()) + 1     #找到每一条subreads的下一个base位置
                genofile2.seek(0)
                for everygeno in genofile2:
                    if zwm_len in everygeno:           #在water算法输入的fasta文件中找到对应那条geno的对应base
                        base_cluster = everygeno.strip("\n").split("\n")[1][base_pos]
                        if base_cluster = "A":
                            num_A +=1
                        if base_cluster = "T":
                            num_T +=1
                        if base_cluster = "G":
                            num_G +=1
                        if base_cluster = "C":
                            num_C +=1
        num_dict = {"A":num_A,"T":num_T,"C":num_C,"G":num_G}    #比较ACGT哪个频数最高选出来 多个一样高都丢弃
        num_sorted_dict = sorted(num_dict.items(),key=lambda codon_dict:codon_dict[1],reverse=True)
        if num_sorted_dict[0][1] = 0:
            #
            break
        if num_sorted_dict[0][1] != num_sorted_dict[1][1]:
            #print一个为啥break
            break
        else:
            base_now = num_sorted_dict[0][1]
        ref_last = ref_last + base_now
        #到哪里终止？

