from sys import argv
#把ccs和water的结果进行一个一个的比对,看有没有对出来call得不一样的
ccs_file,water_file,out=argv[1:]

ccs_file = open(ccs_file,"r")
water_file = open(water_file,"r")
outfile = open(out,"w")

wt = "CGCTGCTGCTGGGCAGCGCGCCGCTTTATGCGCAGACGAGTGCGGTGCAGCAAAAGCTGGCGGCGCTGGAGAAAAGCAGCGGAGGGCGGCTGGGCGTCGCGCTCATCGATACCGCAGATAATACGCAGGTGCTTTATCGCGGTGATGAACGCTTTCCAATGTGCAGTACCAGTAAAGTTATGGCGGCCGCGGCGGTGCTTAAGCAGAGTGAAACGCAAAAGCAGCTGCTTAATCAGCCTGTCGAGATCAAGCCTGCCGATCTGGTTAACTACAATCCGATTGCCGAAAAACACGTCAACGGCACAATGACGCTGGCAGAACTGAGCGCGGCCGCGTTGCAGTACAGCGACAATACCGCCATGAACAAATTGATTGCCCAGCTCGGTGGCCCGGGAGGCGTGACGGCTTTTGCCCGCGCGATCGGCGATGAGACGTTTCGTCTGGATCGCACTGAACCTACGCTGAATACCGCCATTCCCGGCGACCCGAGAGACACCACCACGCCGCGGGCGATGGCGCAGACGTTGCGTCAGCTTACGCTGGGTCATGCGCTGGGCGAAACCCAGCGGGCGCAGTTGGTGACGTGGCTCAAAGGCAATACGACCGGCGCAGCCAGCATTCGGGCCGGCTTACCGACGTCGTGGACTGTGGGTGATAAGACCGGCAGCGGCGACTACGGCACCACCAATGATATTGCGGTGATCTGGCCGCAGGGTCGTGCGCCGCTGGTTCTGGTGACCTATTTTACCCAGCCGCAACAGAACGCAGAGAGCCGCCGCGATGTGCTGGCTTCAGCGGCGAGAATCATCGCCGAAGGGCTGTAACCAGGCATCAAATAAAACGAAAGGCTCAGTCGAAAGACTGGGCCTTTCGTTTTATCTGTTGTTTGTCGGTGAACGCTCTCCTGAGTAGGACAAATCCGCCTTAATTAA"
ccs_f_dict = {}
ccs_r_dict = {}
water_f_dict = {}
water_r_dict = {}
ccs_cluster = ccs_file.read()
ccs_cluster = ccs_cluster.strip(">").strip().split(">")
for line in ccs_cluster:
    line = line.strip().split("\n")
    zwmname = line[0]
    line_f = line[1]
    line_r = line[2]
    mut_num_f = 0
    mut_num_r = 0
    if len(line_f) >30:
        geno_f = line_f.split("_")[1].split(",")[0]
        for i in range(932):
            if geno_f[i] != wt[i]:
                mut_num_f += 1
        if mut_num_f == 1:
            for a in range(932):
                if geno_f[a] != wt[a]:
                    ccs_f_dict[zwmname] = wt[a] + str(a) + geno_f[a]
    if len(line_r) >30:
        geno_r = line_r.split("_")[1].split(",")[0]
        for i in range(932):
            if geno_r[i] != wt[i]:
                mut_num_r += 1
        if mut_num_r == 1:
            for a in range(932):
                if geno_r[a] != wt[a]:
                    ccs_r_dict[zwmname] = wt[a] + str(a) + geno_r[a] 

water_cluster = water_file.read()
water_cluster = water_cluster.strip(">").strip().split(">")
for line in water_cluster:
    line = line.strip().split("\n")
    zwmname = line[0]
    line_f = line[1]
    line_r = line[2]
    mut_num_f = 0
    mut_num_r = 0
    if len(line_f) >30:
        if line_f[2:].split(" ")[1] == line_f[2:].split(" ")[2]:
            geno_f = line_f[2:].split(" ")[0]
            for i in range(932):
                if geno_f[i] != wt[i]:
                    mut_num_f += 1
            if mut_num_f == 1:
                for a in range(932):
                    if geno_f[a] != wt[a]:
                        water_f_dict[zwmname] = wt[a] + str(a) + geno_f[a]
    if len(line_r) >30:
        if line_r[2:].split(" ")[1] == line_r[2:].split(" ")[2]:
            geno_r = line_r[2:].split(" ")[0]
            for i in range(932):
                if geno_r[i] != wt[i]:
                    mut_num_r += 1
            if mut_num_r == 1:
                for a in range(932):
                    if geno_r[a] != wt[a]:
                        water_r_dict[zwmname] = wt[a] + str(a) + geno_r[a]

mut_f = 0
mut_r = 0
for zwm in water_f_dict:
    if zwm in ccs_f_dict:
        mut_f +=1
        if water_f_dict[zwm] != ccs_f_dict[zwm]:
            outfile.write(zwm + "f" + "," + "water" + ":" + water_f_dict[zwm] + "," + "ccs" + ":" + ccs_f_dict[zwm] + "\n")
for zwm in water_r_dict:
    if zwm in ccs_r_dict:
        mut_r +=1
        if water_r_dict[zwm] != ccs_r_dict[zwm]:
            outfile.write(zwm + "r" + "," + "water" + ":" + water_r_dict[zwm] + "," + "ccs" + ":" + ccs_r_dict[zwm] + "\n")

print(mut_f)
print(mut_r)
ccs_file.close()
water_file.close()
outfile.close()

