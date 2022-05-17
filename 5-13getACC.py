#!/usr/bin/env python
#coding=utf-8
from Bio.PDB import *
from imp import reload
import math
import sys 

filename,outfile = sys.argv[1:]
p = PDBParser()
structure = p.get_structure("pdb", filename)
out = open(outfile,"w")
for model in structure:
    dssp = DSSP(model, filename)
    for chain in model:
        chain_id = chain.get_id()
        acc = []
        seq = []
        for residue in chain:
            residue_id = residue.get_id()
            try:
                relative_acc = dssp[(chain_id, residue_id)][3]
                if "NA" != relative_acc :
                    acc.append(str( round(relative_acc,2) ))
                    seq.append(Polypeptide.three_to_one( residue.get_resname() ))
            except:
                    #print "error",residue
                    continue

        seq2 = ",".join(seq)
        acc2 = ",".join(acc)
        out.write(seq2 + "\n" + acc2)

out.close()
