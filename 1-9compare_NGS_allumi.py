from sys import argv

NGS_umi,ccs_umi,=argv[:1]
NGS_umi_file = open(NGS_umi,"r")
ccs_umi_file = open(ccs_umi,"r")

ccs = ccs_umi_file.read()
for every in NGS_umi_file:
    every = every.strip()
    if every[0] != ">":
        if every in ccs:
            num+=1

print(num)

NGS_umi_file.close()
ccs_umi_file.close()