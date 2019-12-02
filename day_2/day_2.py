# -*- coding: utf-8 -*-
"""
Created on Mon Dec  2 11:06:47 2019

@author: jchoiniere
"""

with open('input.txt') as f:
    infile = f.readlines()
    
def intcode_d2(cl, n, v, l):
    l[1] = n
    l[2] = v
    for c in cl:
        cmd = l[c]
        if cmd == 1:
            i = l[l[c+1]]
            j = l[l[c+2]]
            l[l[c+3]] = i+j
        elif cmd == 2:
            i = l[l[c+1]]
            j = l[l[c+2]]
            l[l[c+3]] = i*j
        elif cmd == 99:
            break
    return(l[0])
    
# Part one
int_list = [int(n) for n in infile[0].split(',')]
int_list[1] = 12
int_list[2] = 2

command_list = [i for i in range(len(int_list)) if i % 4 == 0]

print("Part 1 answer: "+str(intcode_d2(cl = command_list, n = 12, v = 2, l = int_list)))


# Part two
nlist = [i for i in range(0,100)]
vlist = [i for i in range(0,100)]

for n in nlist:
    for v in vlist:
        int_list = [int(n) for n in infile[0].split(',')]
        r = intcode_d2(command_list, n, v, int_list)
        if r == 19690720:
            print("Part 2 answer: "+str(100*n+v))