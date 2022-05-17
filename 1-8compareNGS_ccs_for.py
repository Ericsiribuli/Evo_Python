from sys import argv

input_NGS_umi,input_ccs_genoumi,=argv[1:]
input_NGS_umi_file = open(input_NGS_umi,"r")
input_ccs_genoumi_file = open(input_ccs_genoumi,"r")


num = 0
k = set()
for line in input_ccs_genoumi_file:
  umi = line.strip().split(",")[2]
  k.add(umi)
number=len(k)

for every in input_NGS_umi_file:
  every = every.strip()
  if every[0] != ">":
    if every in k:
      num+=1
print("The number of umi that ccs in NGS is " + str(num))
print("The number of CCS's umi is " + str(number))
print(num/number)

input_NGS_umi_file.close()
input_ccs_genoumi_file.close()

