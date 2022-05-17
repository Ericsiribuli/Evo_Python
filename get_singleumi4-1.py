from sys import argv
import numpy as np

inputmy,inputccs,out=argv[1:]

inpumy = open(inputmy,"r")
inpuccs = open(inputccs,"r")
outfile = open(out,"w")

umi_genot_dict={}
for line in inpumy:
    line=line.strip()
    if len(line)>700:
        umi_g_list=line.split(" ")
        if len(umi_g_list[0])==735 and umi_g_list[1]==umi_g_list[2] and len(umi_g_list[1])==20:
            umi_pre=umi_g_list[1]
            ctx_pre=umi_g_list[0].split("_")[1]                
            if umi_pre in umi_genot_dict.keys():
                umi_genot_dict[umi_pre].append(ctx_pre[:714])
            else:
                umi_genot_dict[umi_pre]=[ctx_pre[:714]] 
n_myy=0
umi_geno_my_dict = {}
for umi_myy in umi_genot_dict:
    if len(np.unique(umi_genot_dict[umi_myy]))==1:
        n_myy+=1
        geno_myy = "".join(np.unique(umi_genot_dict[umi_myy]))
        umi_geno_my_dict[umi_myy] = geno_myy

#ccs
umi_genot_dict2={}
for line in inpuccs:
    line=line.strip()
    if len(line)>700:
        umi_g_list=line.split(" ")
        if len(umi_g_list[0])==735 and umi_g_list[1]==umi_g_list[2] and len(umi_g_list[1])==20:
            umi_pre=umi_g_list[1]
            ctx_pre=umi_g_list[0].split("_")[1]                
            if umi_pre in umi_genot_dict2.keys():
                umi_genot_dict2[umi_pre].append(ctx_pre[:714])
            else:
                umi_genot_dict2[umi_pre]=[ctx_pre[:714]] 
n_same=0
n_diff=0
n_ccs=0
n_ccs_notin_myy=0
for umi_ccs in umi_genot_dict2:
    if len(np.unique(umi_genot_dict2[umi_ccs]))==1:
        n_ccs +=1
        geno_ccs = "".join(np.unique(umi_genot_dict2[umi_ccs]))
        if umi_ccs in umi_geno_my_dict:
            if geno_ccs == umi_geno_my_dict[umi_ccs]:
                n_same+=1
            else:
                outfile.write(umi_ccs + "," + geno_ccs + "," + umi_geno_my_dict[umi_ccs] + "\n")
                n_diff+=1
        else:
            n_ccs_notin_myy+=1

print("myy:" + str(n_myy))
print("ccs:" + str(n_ccs))
print("same:" + str(n_same))
print("diff:" + str(n_diff))
print("ccs_not_in_myy:" + str(n_ccs_notin_myy))

inpumy.close()
inpuccs.close()
outfile.close()