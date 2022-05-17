import re

ccsfile = open("ccs.am","r")
umifile = open("T_umi_more_than_five.txt","r")

umifile1 = umifile.read()
pattern = re.compile('TTAATTAA\w{20}CTGCAG')
same_num = 0
for line in ccsfile:
    umi1 = re.search(pattern,line,flags=0)
    if umi1 is None:
        pass
    else:
        umi2 = umi1.group()
        umi = umi2[8:28]
        if umi in umifile1:
            same_num +=1
print(same_num)

ccsfile.close()
umifile.close()

