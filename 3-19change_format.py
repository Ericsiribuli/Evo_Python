from sys import argv
import re
import numpy as np


input_file, outfile= argv[1:]

file_old54061 = open(input_file,"r")

out = open(outfile,"w")

pra_old54061 = file_old54061.read().strip(">").split(">")
for line in pra_old54061:
    zwm_name = line.strip().split("\n")[0]
    if line.find("r") == -1:
        line2 = line.strip().split("\n")
        f_geno = line.strip().split("\n")[1]
        out.write(">" + zwm_name + "\n" + "none" + "\n" + f_geno + "\n")
    if line.find("f") == -1:
        line2 = line.strip().split("\n")
        r_geno = line.strip().split("\n")[1]
        out.write(">" + zwm_name + "\n" + r_geno + "\n" + "none" + "\n")
    if line.find("r") != -1 and line.find("f") != -1:
        out.write(">" + line)

out.close()


