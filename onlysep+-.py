import re
# import pysam
from sys import argv

inputfile,out_f,out_r=argv[1:]

inputfile = open("input.txt","r")
outf = open("pra_f.txt", "w")
outr = open("pra_r.txt", "w")
header = ""
for i in inputfile.readlines()[0:7]:
    header = header + i
inputfile.seek(0)
outf.write(header)
outr.write(header)
for line in inputfile.readlines()[7:]:
    everysub=re.split(r'[	]+',line.strip())
    print(everysub)
    if int(everysub[1]) == 0:
        outf.write(line)
    elif int(everysub[1]) == 16:
        outr.write(line)

inputfile.close()
outf.close()
outr.close()

