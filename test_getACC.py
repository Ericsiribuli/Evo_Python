#!/usr/bin/env python
#coding=utf-8
from Bio.PDB import *
from imp import reload
import math
import sys 

filename = sys.argv[1]
p = PDBParser()
structure = p.get_structure("pdb", filename)
for model in structure:
    dssp = DSSP(model, filename)
    print(model)
    for chain in model:
        chain_id = chain.get_id()
        acc = []
        seq = []
        print(chain)
        print(chain_id)
        for residue in chain:
            print(residue)
            residue_id = residue.get_id()
            print(residue_id)
            try:
                relative_acc = dssp[(chain_id, residue_id)][3]
                if "NA" != relative_acc :
                    acc.append(str( round(relative_acc,2) ))
                    seq.append(Polypeptide.three_to_one( residue.get_resname() ))
            except:
                    #print "error",residue
                    continue

        print(">" + (filename.split("/")[-1][3:7]).upper() + ":" +chain.get_id())
        print(" ".join(seq))
        print(" ".join(acc))
        print("")

