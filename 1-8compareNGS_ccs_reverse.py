from sys import argv

input_NGS_umi,input_ccs_genoumi,=argv[1:]
input_NGS_umi_file = open(input_NGS_umi,"r")
input_ccs_genoumi_file = open(input_ccs_genoumi,"r")

umi_cluster= ""
num = 0
k = set()
for line in input_ccs_genoumi_file:
  umi = line.strip().split(",")[2]
  reverse_seq = ""
  for i in umi:
    if i == "A":
      reverse_seq = "T" + reverse_seq
    if i == "T":
      reverse_seq = "A" + reverse_seq
    if i == "C":
      reverse_seq = "G" + reverse_seq
    if i == "G":
      reverse_seq = "C" + reverse_seq
  umi_cluster = umi_cluster + "\n" + reverse_seq
  k.add(reverse_seq)
number=len(k)

for every in input_NGS_umi_file:
    every = every.strip()
    if every[0] != ">":
        if every in umi_cluster:
            num+=1
print("The number of umi that ccs in NGS is " + str(num))
print("The number of CCS's umi is " + str(number))
print(num/number)

input_NGS_umi_file.close()
input_ccs_genoumi_file.close()