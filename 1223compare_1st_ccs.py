from sys import argv

infile_3st,infile_1st,=argv[1:]
file3st = open(infile_3st,"r")
file1st = open(infile_1st,"r")

num = 0
file_1st = file1st.read()
for line in file3st:
    geno = line.strip().split(",")[0]
    umi = line.strip().split(",")[1]
    if geno in file_1st and umi in file_1st:
        num+=1
print(num)

file1st.close()
file3st.close()
