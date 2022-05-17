from sys import argv
#1/22 改之前的一个错误/这次把正负链合在一起
ccs_f,ccs_r,out_geno_umi=argv[1:]

forward_ccs = open(ccs_f,"r")
out = open(out_geno_umi,"w")

forward_dict = {}
forward_umi_geno_dict = {}
out_cluster = ""
for every in forward_ccs:
    zwmname_ccs_raw = every.strip().split(",")[0][21:]
    if zwmname_ccs_raw[7] == "/":
        zwm_name_f = zwmname_ccs_raw[:7]
    else:
        zwm_name_f = zwmname_ccs_raw[:8]
    geno_f = every.strip().split(",")[1]
    umi_f = every.strip().split(",")[2]
    forward_umi_geno_dict[umi_f] = geno_f
    forward_dict[zwm_name_f] = geno_f + "," + umi_f
with open(ccs_r,"r") as reverse_ccs:
    for line in reverse_ccs:
        zwmname_ccs_raw = line.strip().split(",")[0][21:]
        if zwmname_ccs_raw[7] == "/":
            zwm_name_r = zwmname_ccs_raw[:7]
        else:
            zwm_name_r = zwmname_ccs_raw[:8]
        geno_r = line.strip().split(",")[1]
        reverse_geno = ""
        reverse_umi = ""
        for geno_base in geno_r:
            if geno_base == "A":
                reverse_geno = "T" + reverse_geno
            if geno_base == "T":
                reverse_geno = "A" + reverse_geno
            if geno_base == "C":
                reverse_geno = "G" + reverse_geno
            if geno_base == "G":
                reverse_geno = "C" + reverse_geno
        umi_r = line.strip().split(",")[2]
        for umi_base in umi_r:
            if umi_base == "A":
                reverse_umi = "T" + reverse_umi
            if umi_base == "T":
                reverse_umi = "A" + reverse_umi
            if umi_base == "C":
                reverse_umi = "G" + reverse_umi
            if umi_base == "G":
                reverse_umi = "C" + reverse_umi
        if reverse_umi in forward_umi_geno_dict:
            if forward_umi_geno_dict[reverse_umi] == reverse_geno:
                if zwm_name_r in forward_dict:
                    out_cluster = out_cluster + ">" + zwm_name_r + "\n" + "f_" + forward_dict[zwm_name_r] + "\n" + "r_" + reverse_geno + "," + reverse_umi + "\n" 
                else:
                    out_cluster = out_cluster + ">" + zwm_name_r + "\n" + "f_none" + "\n" + "r_" + reverse_geno + "," + reverse_umi + "\n" 
        else:
            if zwm_name_r in forward_dict:
                out_cluster = out_cluster + ">" + zwm_name_r + "\n" + "f_" + forward_dict[zwm_name_r] + "\n" + "r_" + reverse_geno + "," + reverse_umi + "\n" 
            else:
                out_cluster = out_cluster + ">" + zwm_name_r + "\n" + "f_none" + "\n" + "r_" + reverse_geno + "," + reverse_umi + "\n" 

for i in forward_dict:
    if i in out_cluster:
        pass
    else:
        out_cluster = out_cluster + ">" + i + "\n" + "f_" + forward_dict[i] + "\n" + "r_none" + "\n" 
out.write(out_cluster)
        
forward_ccs.close()
out.close()

