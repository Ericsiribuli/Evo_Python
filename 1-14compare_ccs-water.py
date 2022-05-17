from sys import argv
#对比ccs和water的结果，看是否存在子集关系

in_ccs,in_water,out=argv[1:]
ccs_file = open(in_ccs,"r")
water_file = open(in_water,"r")
outfile = open(out,"w")
water_dict = {}
water_cluster = water_file.read()
water_cluster = water_cluster.strip(">").split(">")
for line in water_cluster:
    line = line.strip().split("\n")
    water_dict[line[0]] = line[1] + "," + line[2]


num1 = 0
num2 = 0
for every_ccs in ccs_file:
    every = every_ccs.strip().split(",")
    geno_ccs = every[1]
    umi_ccs = every[2]
    zwmname_ccs_raw = every[0][21:]
    if zwmname_ccs_raw[7] == "/":
        zwmname_ccs = every[0][21:28]
    else:
        zwmname_ccs = every[0][21:29]
    if zwmname_ccs in water_dict:
        num1 +=1
        if geno_ccs in water_dict[zwmname_ccs] and umi_ccs in water_dict[zwmname_ccs]:
            num2+=1
        else:
            outfile.write(zwmname_ccs + "\n" + geno_ccs + "," + umi_ccs + "\n" + water_dict[zwmname_ccs] + "\n")

print("The number of zwmname in waterdict is " + str(num1))
print("The number of ccs_water 100match is " + str(num2))

ccs_file.close()
water_file.close()
outfile.close()