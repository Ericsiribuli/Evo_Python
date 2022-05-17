from sys import argv
input,output=argv[1:]

file = open(input,"r")
out = open(output,"w")
cluster = ""
for every in file:
    if "one_two_three_four_five_six" in every:
        cluster = cluster + every
out.write(cluster)
out.close()

