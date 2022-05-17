import re

inputfile = open("input2.txt","r")
forward = open("pra_f.fasta","w")
reverse = open("pra_r.fasta","w")

forward_blasr = ""
reverse_blasr = ""
for line in inputfile.readlines()[7:]:
    everysub=re.split(r'[	]+',line.strip())
    # print(everysub)
    if int(everysub[1]) == 0:
        forward_blasr = forward_blasr + ">" + everysub[0][21:27] + "_" +everysub[0][29:] + "\n" + everysub[9] + "\n" 
    elif int(everysub[1]) == 16:
        reverse_blasr = reverse_blasr + ">" + everysub[0][21:27] + "_" +everysub[0][29:] + "\n" + everysub[9] + "\n"
forward.write(forward_blasr)
reverse.write(reverse_blasr)

inputfile.close()
forward.close()
reverse.close()