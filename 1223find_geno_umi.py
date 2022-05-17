import re
from sys import argv

infile,out,=argv[1:]
inputfile = open(infile,"r")
outfile = open(out,"w")

geno_pattern=re.compile("ACAAA\w{733}ATAAG")
umi_pattern=re.compile("ACACC\w{20}GCTTC")
umi_geno = {}

for line in inputfile:
    geno=re.search(geno_pattern,line,flags=0)
    umi=re.search(umi_pattern,line,flags=0)
    if geno is not None and umi is not None:
        geno1 = geno.group()[5:738]
        umi1 = umi.group()[5:25]

        outfile.write(geno1 + "," + umi1 + "\n")

inputfile.close()
outfile.close()

