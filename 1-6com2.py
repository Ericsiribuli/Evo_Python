from sys import argv
import numpy as np

input_NGS_umi,input_ccs_genoumi,=argv[1:]
input_NGS_umi_file = open(input_NGS_umi,"r")
input_ccs_genoumi_file = open(input_ccs_genoumi,"r")

umi_cluster = []
for line in input_ccs_genoumi_file:
    umi = line.strip().split(",")[2]
    umi_cluster.append(umi)
num = 0
NGS_umi = input_NGS_umi_file.read()
uni_umi_cluster = np.unique(umi_cluster)
for every_umi in uni_umi_cluster:
    if every_umi in NGS_umi:
        num += 1
print(num)

input_NGS_umi_file.close()
input_ccs_genoumi_file.close()



