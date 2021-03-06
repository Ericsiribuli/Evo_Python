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
'''

from Bio.Seq import translate
import math
import copy
from pymol import cmd
#定义空间欧式距离函数
diff_len = lambda x1,y1 : math.sqrt((x1[0]-y1[0])*(x1[0]-y1[0]) + (x1[1]-y1[1])*(x1[1]-y1[1]) + (x1[2]-y1[2])*(x1[2]-y1[2]))
# a=[14.916000366210938, 19.33300018310547, 90.18499755859375]
# b=[24.292999267578125, 41.37200164794922, 104.74400329589844]
# print(diff_len(a,b))
ctx_gene="ACGAGTGCGGTGCAGCAAAAGCTGGCGGCGCTGGAGAAAAGCAGCGGAGGGCGGCTGGGCGTCGCGCTCATCGATACCGCAGATAATACGCAGGTGCTTTATCGCGGTGATGAACGCTTTCCAATGTGCAGTACCAGTAAAGTTATGGCGGCCGCGGCGGTGCTTAAGCAGAGTGAAACGCAAAAGCAGCTGCTTAATCAGCCTGTCGAGATCAAGCCTGCCGATCTGGTTAACTACAATCCGATTGCCGAAAAACACGTCAACGGCACAATGACGCTGGCAGAACTGAGCGCGGCCGCGTTGCAGTACAGCGACAATACCGCCATGAACAAATTGATTGCCCAGCTCGGTGGCCCGGGAGGCGTGACGGCTTTTGCCCGCGCGATCGGCGATGAGACGTTTCGTCTGGATCGCACTGAACCTACGCTGAATACCGCCATTCCCGGCGACCCGAGAGACACCACCACGCCGCGGGCGATGGCGCAGACGTTGCGTCAGCTTACGCTGGGTCATGCGCTGGGCGAAACCCAGCGGGCGCAGTTGGTGACGTGGCTCAAAGGCAATACGACCGGCGCAGCCAGCATTCGGGCCGGCTTACCGACGTCGTGGACTGTGGGTGATAAGACCGGCAGCGGCGACTACGGCACCACCAATGATATTGCGGTGATCTGGCCGCAGGGTCGTGCGCCGCTGGTTCTGGTGACCTATTTTACCCAGCCGCAACAGAACGCAGAGAGCCGCCGCGATGTGCTGGCTTCAGCGGCGAGAATCATCGCCGAAGGGCTG"
ctx_aa=translate(ctx_gene)

ctx_in_pymol="TSAVQQKLAALEKSSGGRLGVALIDTADNTQVLYRGDERFPMCSTSKVMAAAAVLKQSETQKQLLNQPVEIKPADLVNYNPIAEKHVNGTMTLAELSAAALQYSDNTAMNKLIAQLGGPGGVTAFARAIGDETFRLDRTEPTLNTAIPGDPRDTTTPRAMAQTLRQLTLGHALGETQRAQLVTWLKGNTTGAASIRAGLPTSWTVGDKTGSGDYGTTNDIAVIWPQGRAPLVLVTYFTQPQQNAESRRDVLASAARIIAEGL"
start_p=26
start_aa=26
aa_3D_dict={}
print("ok")
for aa in range(len(ctx_aa)+3):
    aa_list=[]
    po_3d=[]
    cmd.iterate_state (1, "resi %s and n. CA"%(start_p),"aa_list.append(oneletter),po_3d.append([x,y,z])")
    
    # print(start_p,aa_list,po_3d)
    
    if aa_list and po_3d:
        print(start_aa,start_p,aa_list[0],po_3d[0])
        if aa_list[0]==ctx_aa[start_aa-26]:
            aa_3D_dict[str(start_aa)+ctx_aa[start_aa-26]]=po_3d[0]
        else:
            print("match is error")
        start_p+=1
        start_aa+=1
    # elif aa_list is None and po_3d is None:
    else:
        # start_p+=1
        # if aa_list[0]==ctx_aa[start_aa-26]:
        #     aa_3D_dict[str(start_p)+ctx_aa[start_p-26]]=po_3d

        # aa_3D_dict[str(start_p)+ctx_aa[start_p-26]]="*"
        print(start_aa,start_p,aa_list,po_3d)
        start_p+=1
    # else:
    #     print(aa_list,po_3d)
    #     print("unknow error",start_aa,aa)
    #     break
print("dict is ok")
# print(aa_3D_dict)
with open("distance_bwt_9-3.txt","w") as out:
    for aa_1 in aa_3D_dict.keys():
        if aa_3D_dict[aa_1]!="*":
            dele_dict=copy.deepcopy(aa_3D_dict)
            dele_dict.pop(aa_1)
            for another_aa in dele_dict.keys():
                if dele_dict[another_aa]!="*":
                    distance_bwt=diff_len(aa_3D_dict[aa_1],dele_dict[another_aa])
                    if distance_bwt<=13:
                        out.write(str(aa_1)+"-"+str(another_aa)+":"+str('%.2f'%(distance_bwt))+"\t")
            out.write("\n")


# from Bio.Seq import translate
# gfp="AGCAAGGGCGAGGAGCTGTTCACCGGGGTGGTGCCCATCCTGGTCGAGCTGGACGGCGACGTAAACGGCCACAAGTTCAGCGTGTCCGGCGAGGGCGAGGGCGATGCCACCTACGGCAAGCTGACCCTGAAGTTCATCTGCACCACCGGCAAGCTGCCCGTGCCCTGGCCCACCCTCGTGACCACCCTGTCGTACGGCGTGCAGTGCTTCAGCCGCTACCCCGACCACATGAAGCAGCACGACTTCTTCAAGTCCGCCATGCCCGAAGGCTACGTCCAGGAGCGCACCATCTTCTTCAAGGACGACGGCAACTACAAGACCCGCGCCGAGGTGAAGTTCGAGGGCGACACACTAGTGAACCGCATCGAGCTGAAGGGCATCGACTTCAAGGAGGACGGCAACATCCTGGGGCACAAGCTGGAGTACAACTACAACAGCCACAACGTCTATATCATGGCCGACAAGCAGAAGAACGGCATCAAGGTGAACTTCAAGATCCGCCACAACATCGAGGACGGCAGCGTGCAGCTCGCCGACCACTACCAGCAGAACACCCCCATCGGCGACGGCCCCGTGCTGCTGCCCGACAACCACTACCTGAGCACCCAGTCCGCCCTGAGCAAAGACCCCAACGAGAAGCGCGATCACATGGTCCTGCTGGAGTTCGTGACCGCCGCCGGGATCACTCACGGCATGGACGAGCTGTACAAGTGA"
# print(translate(gfp))
# a="GCGCAGACGAGTGCGGTGCAGCAAAAGCTGGCGGCGCTGGAGAAAAGCAGCGGAGGGCGGCTGGGCGTCGCGCTCATCGATACCGCAGATAATACGCAGGTGCTTTATCGCGGTGATGAACGCTTTCCAATGTGCAGTACCAGTAAAGTTATGGCGGCCGCGGCGGTGCTTAAGCAGAGTGAAACGCAAAAGCAGCTGCTTAATCAGCCTGTCGAGATCAAGCCTGCCGATCTGGTTAACTACAATCCGATTGCCGAAAAACACGTCAACGGCACAATGACGCTGGCAGAACTGAGCGCGGCCGCGTTGCAGTACAGCGACAATACCGCCATGAACAAATTGATTGCCCAGCTCGGTGGCCCGGGAGGCGTGACGGCTTTTGCCCGCGCGATCGGCGATGAGACGTTTCGTCTGGATCGCACTGAACCTACGCTGAATACCGCCATTCCCGGCGACCCGAGAGACACCACCACGCCGCGGGCGATGGCGCAGACGTTGCGTCAGCTTACGCTGGGTCATGCGCTGGGCGAAACCCAGCGGGCGCAGTTGGTGACGTGGCTCAAAGGCAATACGACCGGCGCAGCCAGCATTCGGGCCGGCTTACCGACGTCGTGGACTGTGGGTGATAAGACCGGCAGCGGCGACTACGGCACCACCAATGATATTGCGGTGATCTGGCCGCAGGGTCGTGCGCCGCTGGTTCTGGTGACCTATTTTACCCAGCCGCAACAGAACGCAGAGAGCCGCCGCGATGTGCTGGCTTCAGCGGCGAGAATCATCGCCGAAGGGCTG"
# b="TSAVQQKLAALEKSSGGRLGVALIDTADNTQVLYRGDERFPMCSTSKVMAAAAVLKQSETQKQLLNQPVEIKPADLVNYNPIAEKHVNGTMTLAELSAAALQYSDNTAMNKLIAQLGGPGGVTAFARAIGDETFRLDRTEPTLNTAIPGDPRDTTTPRAMAQTLRQLTLGHALGETQRAQLVTWLKGNTTGAASIRAGLPTSWTVGDKTGSGDYGTTNDIAVIWPQGRAPLVLVTYFTQPQQNAESRRDVLASAARIIAEGL"
# aa=translate(a)
# if aa[2:]==b:
#     print("ok")
# print(aa[2:])
# print(aa[60-26])
# # print(aa[216])
# k="TACGGCACCACCAATGATATTGCG"
# print(translate(k))

