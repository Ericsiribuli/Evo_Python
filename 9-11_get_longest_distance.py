from sys import argv
import re
from collections import Counter
import numpy as np

inputfile = open("distance_bwt_9-3.txt","r")

sum_distance = []
for line2 in inputfile:
    fifth_distance = []
    each = line2.strip().split()
    distance_sum = 0
    for other in each:
        distance = float(other.split(":")[1])
        fifth_distance.append(distance)
    most_dis = sorted(fifth_distance)[4]
    sum_distance.append(most_dis)

# sort_distance_dict=sorted(sum_distance_dict.items(),key=lambda sum_distance_dict:sum_distance_dict[1],reverse=True)

print(max(sum_distance))

