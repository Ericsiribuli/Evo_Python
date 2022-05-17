from sys import argv
#2-22 算umi种类
inputfile=argv[1]

input_file = open(inputfile,"r")

k = set()
num = 0
for i in input_file:
    if len(i) > 30:
        num +=1
        umi = i.strip().split(" ")[1]
        k.add(umi)

print("The number of result is" + str(num))
print("The number of umi species is " + str(len(k)))


input_file.close()

