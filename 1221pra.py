import os
import re

inputblasr,inputsam,out_f,out_r=argv[1:]

inputfile1 = open(inputblasr,"r")
inputfile2 = open(inputsam,"r")
out = open(output,"w")

forward_caller_ccs = ""
reverse_caller_ccs = ""

for line in inputfile1.readlines()[7:]:
    everysub=re.split(r'[	]+',line.strip())
    if int(everysub[1]) == 0:
        forward_blasr = forward_blasr + "\n" + everysub[0]
    elif int(everysub[1]) == 16:
        reverse_blasr = reverse_blasr + "\n" + everysub[0]

header = ""
for i in inputfile2.readlines()[0:5]:
    header =header + i
inputfile2.seek(0)
for pra in inputfile2.readlines()[5:]:
    