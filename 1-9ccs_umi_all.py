from sys import argv

input_ccs_f_genoumi,input_ccs_r_genoumi,out_umi=argv[1:]
input_ccs_f_genoumi_file = open(input_ccs_f_genoumi,"r")
input_ccs_r_genoumi_file = open(input_ccs_r_genoumi,"r")
outfile = open(out_umi,"w")

k = set()
umi_cluster = ""
for line in input_ccs_f_genoumi_file:
  umi = line.strip().split(",")[2]
  k.add(umi)

for line in input_ccs_r_genoumi_file:
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
  k.add(reverse_seq)

for every in k:
    umi_cluster = umi_cluster + "\n" + every
outfile.write(umi_cluster)

input_ccs_f_genoumi_file.close()
input_ccs_r_genoumi_file.close()
outfile.close()