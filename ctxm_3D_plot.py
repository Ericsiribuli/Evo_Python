#-*-coding:utf-8 -*-
'''
from Bio.Seq import translate
alter protA, b=0.0
alter protA and n. CA, b=stored.newB.pop(0)
spectrum b, blue_red, minimum=10, maximum=50
color red, name ca 
show surface,name ca
id_atom
select resi 1#选择某个氨基酸位点
alter (resi 30),b=0.5#更改某个位置的B_factor
print(cmd.get_fastastr('all'))
atoms = cmd.get_model("resi 26")#找出某个位置氨基酸的名称
atoms = cmd.get_model("chain A")
for at in atoms.atom:
    print("ATOM DEFINITION: "+at.chain+" "\
        +at.resn+" "\
        +str(at.resi)+" "\
        +at.name+" "\
        +str(at.index)+" "\
        +"%.2f " % (at.b)\
        +str(at.coord[0])+" "\
        +str(at.coord[1])+" "\
        +str(at.coord[2]))
spectrum b, red_yellow_blue, minimum=20, maximum=50
set_color fitlow,[51,51,255]
set_color fitmid,[204,204,255]
set_color fithig,[255,0,51]
spectrum b, fitlow_fitmid_fithig, minimum=0, maximum=1.5
'''
from Bio.Seq import translate
import math
import copy
from pymol import cmd
aa_pymol_seq="TSAVQQKLAALEKSSGGRLGVALIDTADNTQVLYRGDERFPMCSTSKVMAAAAVLKQSETQKQLLNQPVEIKPADLVNYNPIAEKHVNGTMTLAELSAAALQYSDNTAMNKLIAQLGGPGGVTAFARAIGDETFRLDRTEPTLNTAIPGDPRDTTTPRAMAQTLRQLTLGHALGETQRAQLVTWLKGNTTGAASIRAGLPTSWTVGDKTGSGDYGTTNDIAVIWPQGRAPLVLVTYFTQPQQNAESRRDVLASAARIIAEGL"
with open("fitness_0.75_0.5mic_aa_mean_new_all_mutant_10-7.txt","r") as fit:
    fit_dict={}
    fitness_list=[]
    for line in fit:
        line_list=line.strip().split(" ")
        fit_dict[int(line_list[0])]=float(line_list[1])
        fitness_list.append(float(line_list[1]))
aa_ctxm=3
aa_pymol=26
for i in range(len(aa_pymol_seq)):
    aa_name=aa_pymol_seq[aa_ctxm-3]
    aa_list=[]
    cmd.iterate_state(1, "resi %s"%(aa_pymol),"aa_list.append(oneletter)")
    ef=fit_dict[aa_ctxm]
    if aa_list:
        if aa_list[0]==aa_name:
            cmd.alter("resi %s"%(aa_pymol),"b=%s"%(ef))
        else:   
            print(aa_pymol,"amino error")
    else:
        aa_pymol+=1
        cmd.iterate_state(1, "resi %s"%(aa_pymol),"aa_list.append(oneletter)")
        if aa_list:
            if aa_list[0]==aa_name:
                cmd.alter("resi %s"%(aa_pymol),"b=%s"%(ef))
            else:
                print(aa_pymol,"amino no_match error")
        else:
            print("amino again error")
    aa_ctxm+=1
    aa_pymol+=1
       
print("min",min(fitness_list),"   max",max(fitness_list))