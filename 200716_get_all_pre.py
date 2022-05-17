from sys import argv
import os
import re
import time

outfile,p1,p2,p3,p4,p5,genofile=argv[1:]
with open(outfile,"w") as out:
    for line in os.popen("python GlobPipeold.py %s %s %s %s %s %s"%(p1,p2,p3,p4,p5,genofile)):
        if len(line) >3:
            out.write(line)
