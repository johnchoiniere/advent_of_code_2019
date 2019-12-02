# -*- coding: utf-8 -*-
"""
Created on Mon Dec  2 11:06:47 2019

@author: jchoiniere
"""

# read in the data; I'm... not great at doing I/O in python, tbh
with open('input.txt') as f:
    infile = f.readlines()

'''
Retrospectively I made it a function rather than loose code. That should make it more reusable, too.

intcode_d2 is a function with the following four arguments:
    cl -- a list of command locations for the loop to look at
    n  -- a "noun", in the parlance of the game; will be placed in input list position 1
    v  -- a "verb", in the parlance of the game; will be placed in input list position 2
    l  -- the complete input list
'''
def intcode_d2(cl, n, v, l):
    l[1] = n # assign the noun to its spot
    l[2] = v # assign the verb to its spot
    for c in cl:
        cmd = l[c]     # pull the command instruction
        i = l[l[c+1]]  # pull the first value
        j = l[l[c+2]]  # pull the second value
        if cmd == 1:
        # if it's a one, it's addition
            l[l[c+3]] = i+j # place the sum in the specified spot
        elif cmd == 2:
        # if it's a two, it's multiplication
            l[l[c+3]] = i*j # place the product in the specified spot
        elif cmd == 99:
        # if it's 99, it's the end
            break
        # maybe later add in error-handling?
    return(l[0]) # return the new value at the inital position.
    
#------------------------- Part one -------------------------
int_list = [int(n) for n in infile[0].split(',')]
int_list[1] = 12
int_list[2] = 2

# commands happen every four positions beginning with zero
command_list = [i for i in range(len(int_list)) if i % 4 == 0]

print("Part 1 answer: "+str(intcode_d2(cl = command_list, n = 12, v = 2, l = int_list)))


#------------------------- Part two -------------------------

nlist = [i for i in range(0,100)]
vlist = [i for i in range(0,100)]

# loop over 0-99 for noun and verb
for n in nlist:
    for v in vlist:
        int_list = [int(n) for n in infile[0].split(',')]
        r = intcode_d2(command_list, n, v, int_list)
        # if it's the sought-after value, print what the game wants
        if r == 19690720:
            print("Part 2 answer: "+str(100*n+v))