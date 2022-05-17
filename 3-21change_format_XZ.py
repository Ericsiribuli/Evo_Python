from sys import argv

inputfile,out_last,=argv[1:]

ccs_dict1 = {}

inpu = open(inputfile,"r")
outfile = open(out_last,"w")


input_file = inpu.read().strip(">").split(">")
for line in input_file:
    aa = line.strip().split("\n")
    zwm_number2 = aa[0]
    for a in aa[1:]:
        if len(a) >30:
            split = a.strip().split(" ")
            geno3 = split[0]
            umi3 = split[1]
            if umi3 in ccs_dict1.keys():
                ccs_dict1[umi3].append(zwm_number2 + "_"  + geno3)
            else:
                ccs_dict1[umi3]=[zwm_number2 + "_" + geno3]

ccs_cluster = ""
for every in ccs_dict1:
        if len(ccs_dict1[every]) == 1:
                geno2 = "".join(ccs_dict1[every])
                ccs_cluster = ccs_cluster + geno2 + " " + every + " " + every + "\n"
        else:
                geno_list = ccs_dict1[every]
                first = geno_list[0].split("_")[2]
                cluster = ""
                for zwm_geno in geno_list[1:]:
                        if first != zwm_geno.split("_")[2]:
                                first = "wrong"
                                break
                        else: continue
                if first != "wrong":
                        for last_zwm_geno in geno_list:
                            ccs_cluster = ccs_cluster + last_zwm_geno + " " + every + " " + every + "\n"

ccs_dict3 = {}
ccs_cluster = ccs_cluster.strip().strip("\n").split("\n")
for x in ccs_cluster:
    zwmname = x.split("_")[0]
    left = "_".join(x.split("_")[1:])
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
