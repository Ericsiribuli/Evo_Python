from sys import argv
import re
from collections import Counter
import numpy as np

input_fitness,input_position,out=argv[1:]

fitness_file = open(input_fitness,"r")
position_file = open(input_position,"r")
out_file = open(out,"w")

fitness_dict = {}
for line1 in fitness_file:
    pos = line1.strip().split()[0]
    fitness = line1.strip().split()[1]
    fitness_dict[pos] = fitness

for line2 in position_file:
    each = line2.strip().split()
    centre = str(int(each[0].split("-")[0][:-1])-23)
    num = len(each)+1
    centre_fitness = fitness_dict[centre]
    sum_fitness = 0
    sum_fitness = float(centre_fitness)
    for other in each:
        other_pos = str(int(other.split("-")[1].split(":")[0][:-1])-23)
        other_fitness = float(fitness_dict[other_pos])
        sum_fitness = sum_fitness + other_fitness
    aver_fitness = sum_fitness/num
    out_file.write(centre + "," + str(aver_fitness) + "\n")

fitness_file.close()
position_file.close()
out_file.close()