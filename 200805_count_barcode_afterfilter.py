from sys import argv
import os
import re
import multiprocessing
import numpy as np
import math
import random

# 二代barcode有多少在三代筛选前能找到
threefile,input1,input2,input3,input4,input5,input6,input7,input8,input9,input10,input11,input12=argv[1:]

umi_three_dict = {}

with open(threefile,'r') as threegs:
    for line in threegs:
        mut_block = line.strip().split(" * ")[0].split("> ")[1]
        umi_list = line.strip().split(" * ")[1].split(" ")
        for every in umi_list:
            umi_three_dict[every[:20]] = mut_block

print('number of three umi : '+ str(len(umi_three_dict)))

match_num = 0
single_set = set()
double_set = set()
triple_set = set()
with open(input1,'r') as file1:
    te = file1.read().strip(">").split('>')
    for line in te:
        num = line.strip().split('\n')[1].split(' ')[0]
        umi = line.strip().split('\n')[1].split(' ')[1][:20]
        if umi in umi_three_dict:
            match_num +=int(num)
            mut_list = umi_three_dict[umi].split(' ')
            if len(mut_list) ==1:
                if ''.join(mut_list) == 'WT':
                    pass
                else:
                    single_set.add(''.join(mut_list))
            if len(mut_list) ==2:
                double_set.add(' '.join(mut_list))
            if len(mut_list) ==3:
                triple_set.add(' '.join(mut_list))
    
print('s1d1: ' + str(match_num))
print('single: ' + str(len(single_set)))
print('double: ' + str(len(double_set)))
print('triple: ' + str(len(triple_set)))


match_num = 0
single_set = set()
double_set = set()
triple_set = set()
with open(input2,'r') as file2:
    te = file2.read().strip(">").split('>')
    for line in te:
        num = line.strip().split('\n')[1].split(' ')[0]
        umi = line.strip().split('\n')[1].split(' ')[1][:20]
        if umi in umi_three_dict:
            match_num +=int(num)
            mut_list = umi_three_dict[umi].split(' ')
            if len(mut_list) ==1:
                if ''.join(mut_list) == 'WT':
                    pass
                else:
                    single_set.add(''.join(mut_list))
            if len(mut_list) ==2:
                double_set.add(' '.join(mut_list))
            if len(mut_list) ==3:
                triple_set.add(' '.join(mut_list))
    
print('s2d1: ' + str(match_num))
print('single: ' + str(len(single_set)))
print('double: ' + str(len(double_set)))
print('triple: ' + str(len(triple_set)))

match_num = 0
single_set = set()
double_set = set()
triple_set = set()
with open(input3,'r') as file3:
    te = file3.read().strip(">").split('>')
    for line in te:
        num = line.strip().split('\n')[1].split(' ')[0]
        umi = line.strip().split('\n')[1].split(' ')[1][:20]
        if umi in umi_three_dict:
            match_num +=int(num)
            mut_list = umi_three_dict[umi].split(' ')
            if len(mut_list) ==1:
                if ''.join(mut_list) == 'WT':
                    pass
                else:
                    single_set.add(''.join(mut_list))
            if len(mut_list) ==2:
                double_set.add(' '.join(mut_list))
            if len(mut_list) ==3:
                triple_set.add(' '.join(mut_list))
    
print('s3d1: ' + str(match_num))
print('single: ' + str(len(single_set)))
print('double: ' + str(len(double_set)))
print('triple: ' + str(len(triple_set)))


#day3
match_num = 0
single_set = set()
double_set = set()
triple_set = set()
with open(input4,'r') as file4:
    te = file4.read().strip(">").split('>')
    for line in te:
        num = line.strip().split('\n')[1].split(' ')[0]
        umi = line.strip().split('\n')[1].split(' ')[1][:20]
        if umi in umi_three_dict:
            match_num +=int(num)
            mut_list = umi_three_dict[umi].split(' ')
            if len(mut_list) ==1:
                if ''.join(mut_list) == 'WT':
                    pass
                else:
                    single_set.add(''.join(mut_list))
            if len(mut_list) ==2:
                double_set.add(' '.join(mut_list))
            if len(mut_list) ==3:
                triple_set.add(' '.join(mut_list))
    
print('s1d3: ' + str(match_num))
print('single: ' + str(len(single_set)))
print('double: ' + str(len(double_set)))
print('triple: ' + str(len(triple_set)))

match_num = 0
single_set = set()
double_set = set()
triple_set = set()
with open(input5,'r') as file5:
    te = file5.read().strip(">").split('>')
    for line in te:
        num = line.strip().split('\n')[1].split(' ')[0]
        umi = line.strip().split('\n')[1].split(' ')[1][:20]
        if umi in umi_three_dict:
            match_num +=int(num)
            mut_list = umi_three_dict[umi].split(' ')
            if len(mut_list) ==1:
                if ''.join(mut_list) == 'WT':
                    pass
                else:
                    single_set.add(''.join(mut_list))
            if len(mut_list) ==2:
                double_set.add(' '.join(mut_list))
            if len(mut_list) ==3:
                triple_set.add(' '.join(mut_list))
    
print('s2d3: ' + str(match_num))
print('single: ' + str(len(single_set)))
print('double: ' + str(len(double_set)))
print('triple: ' + str(len(triple_set)))

match_num = 0
single_set = set()
double_set = set()
triple_set = set()
with open(input6,'r') as file6:
    te = file6.read().strip(">").split('>')
    for line in te:
        num = line.strip().split('\n')[1].split(' ')[0]
        umi = line.strip().split('\n')[1].split(' ')[1][:20]
        if umi in umi_three_dict:
            match_num +=int(num)
            mut_list = umi_three_dict[umi].split(' ')
            if len(mut_list) ==1:
                if ''.join(mut_list) == 'WT':
                    pass
                else:
                    single_set.add(''.join(mut_list))
            if len(mut_list) ==2:
                double_set.add(' '.join(mut_list))
            if len(mut_list) ==3:
                triple_set.add(' '.join(mut_list))
    
print('s3d3: ' + str(match_num))
print('single: ' + str(len(single_set)))
print('double: ' + str(len(double_set)))
print('triple: ' + str(len(triple_set)))


#day5
match_num = 0
single_set = set()
double_set = set()
triple_set = set()
with open(input7,'r') as file7:
    te = file7.read().strip(">").split('>')
    for line in te:
        num = line.strip().split('\n')[1].split(' ')[0]
        umi = line.strip().split('\n')[1].split(' ')[1][:20]
        if umi in umi_three_dict:
            match_num +=int(num)
            mut_list = umi_three_dict[umi].split(' ')
            if len(mut_list) ==1:
                if ''.join(mut_list) == 'WT':
                    pass
                else:
                    single_set.add(''.join(mut_list))
            if len(mut_list) ==2:
                double_set.add(' '.join(mut_list))
            if len(mut_list) ==3:
                triple_set.add(' '.join(mut_list))
    
print('s1d5: ' + str(match_num))
print('single: ' + str(len(single_set)))
print('double: ' + str(len(double_set)))
print('triple: ' + str(len(triple_set)))

match_num = 0
single_set = set()
double_set = set()
triple_set = set()
with open(input8,'r') as file8:
    te = file8.read().strip(">").split('>')
    for line in te:
        num = line.strip().split('\n')[1].split(' ')[0]
        umi = line.strip().split('\n')[1].split(' ')[1][:20]
        if umi in umi_three_dict:
            match_num +=int(num)
            mut_list = umi_three_dict[umi].split(' ')
            if len(mut_list) ==1:
                if ''.join(mut_list) == 'WT':
                    pass
                else:
                    single_set.add(''.join(mut_list))
            if len(mut_list) ==2:
                double_set.add(' '.join(mut_list))
            if len(mut_list) ==3:
                triple_set.add(' '.join(mut_list))
    
print('s2d5: ' + str(match_num))
print('single: ' + str(len(single_set)))
print('double: ' + str(len(double_set)))
print('triple: ' + str(len(triple_set)))

match_num = 0
single_set = set()
double_set = set()
triple_set = set()
with open(input9,'r') as file9:
    te = file9.read().strip(">").split('>')
    for line in te:
        num = line.strip().split('\n')[1].split(' ')[0]
        umi = line.strip().split('\n')[1].split(' ')[1][:20]
        if umi in umi_three_dict:
            match_num +=int(num)
            mut_list = umi_three_dict[umi].split(' ')
            if len(mut_list) ==1:
                if ''.join(mut_list) == 'WT':
                    pass
                else:
                    single_set.add(''.join(mut_list))
            if len(mut_list) ==2:
                double_set.add(' '.join(mut_list))
            if len(mut_list) ==3:
                triple_set.add(' '.join(mut_list))
    
print('s3d5: ' + str(match_num))
print('single: ' + str(len(single_set)))
print('double: ' + str(len(double_set)))
print('triple: ' + str(len(triple_set)))


#day7
mmatch_num = 0
single_set = set()
double_set = set()
triple_set = set()
with open(input10,'r') as file10:
    te = file10.read().strip(">").split('>')
    for line in te:
        num = line.strip().split('\n')[1].split(' ')[0]
        umi = line.strip().split('\n')[1].split(' ')[1][:20]
        if umi in umi_three_dict:
            match_num +=int(num)
            mut_list = umi_three_dict[umi].split(' ')
            if len(mut_list) ==1:
                if ''.join(mut_list) == 'WT':
                    pass
                else:
                    single_set.add(''.join(mut_list))
            if len(mut_list) ==2:
                double_set.add(' '.join(mut_list))
            if len(mut_list) ==3:
                triple_set.add(' '.join(mut_list))
    
print('s1d7: ' + str(match_num))
print('single: ' + str(len(single_set)))
print('double: ' + str(len(double_set)))
print('triple: ' + str(len(triple_set)))


match_num = 0
single_set = set()
double_set = set()
triple_set = set()
with open(input11,'r') as file11:
    te = file11.read().strip(">").split('>')
    for line in te:
        num = line.strip().split('\n')[1].split(' ')[0]
        umi = line.strip().split('\n')[1].split(' ')[1][:20]
        if umi in umi_three_dict:
            match_num +=int(num)
            mut_list = umi_three_dict[umi].split(' ')
            if len(mut_list) ==1:
                if ''.join(mut_list) == 'WT':
                    pass
                else:
                    single_set.add(''.join(mut_list))
            if len(mut_list) ==2:
                double_set.add(' '.join(mut_list))
            if len(mut_list) ==3:
                triple_set.add(' '.join(mut_list))
    
print('s2d7: ' + str(match_num))
print('single: ' + str(len(single_set)))
print('double: ' + str(len(double_set)))
print('triple: ' + str(len(triple_set)))


match_num = 0
single_set = set()
double_set = set()
triple_set = set()
with open(input12,'r') as file12:
    te = file12.read().strip(">").split('>')
    for line in te:
        num = line.strip().split('\n')[1].split(' ')[0]
        umi = line.strip().split('\n')[1].split(' ')[1][:20]
        if umi in umi_three_dict:
            match_num +=int(num)
            mut_list = umi_three_dict[umi].split(' ')
            if len(mut_list) ==1:
                if ''.join(mut_list) == 'WT':
                    pass
                else:
                    single_set.add(''.join(mut_list))
            if len(mut_list) ==2:
                double_set.add(' '.join(mut_list))
            if len(mut_list) ==3:
                triple_set.add(' '.join(mut_list))
    
print('s3d7: ' + str(match_num))
print('single: ' + str(len(single_set)))
print('double: ' + str(len(double_set)))
print('triple: ' + str(len(triple_set)))