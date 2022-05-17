from sys import argv
import os

input1,out1=argv[1:]

inputfile = open(input1,"r")
outfile = open(out1,"w")
last_zwm_number = ""
zwm_sum = 0
seq = ""
header = ""
for i in inputfile.readlines()[0:7]:
    header = header + i
inputfile.seek(0)
for line in inputfile.readlines()[7:]:
    split_line = line.split("/")
    now_zwm_number = split_line[1]
    if now_zwm_number != last_zwm_number:
        zwm_sum += 1
        if zwm_sum >= 50001:
            break
        seq = seq + line
        last_zwm_number = now_zwm_number
    else:
        seq = seq + line

outfile.write(header+seq)
outfile.close()
inputfile.close()