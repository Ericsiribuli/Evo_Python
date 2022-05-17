inputfile = open("T_geno_umi_ccs.txt","r")

k = set()
umi_cluster = ""
for line in inputfile:
  umi = line.strip().split(",")[2]
  k.add(umi)

print(len(k))
inputfile.close()