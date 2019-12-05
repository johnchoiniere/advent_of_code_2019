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
def opcode_d5(input_val, l):
    l = [int(x) for x in l]
    end = False
    pointer = 0
    while not end:
        instruct = str(l[pointer]).rjust(5,'0')
        operation = instruct[len(instruct)-2:]
        a_mode = int(instruct[2])
        b_mode = int(instruct[1])
        
        if operation == '99':
            end = True
        
        elif operation == '01':
            if a_mode == 0:
                a_val = l[l[pointer+1]]
            elif a_mode == 1:
                a_val = l[pointer+1]
            else:
                print("ERROR IN ASSIGNING A_VAL")
                break
            if b_mode == 0:
                b_val = l[l[pointer+2]]
            elif b_mode == 1:
                b_val = l[pointer+2]
            else:
                print("ERROR IN ASSIGNING B_VAL")
                break
            l[l[pointer+3]] = a_val + b_val
            pointer += 4
        
        elif operation == '02':
            if a_mode == 0:
                a_val = l[l[pointer+1]]
            elif a_mode == 1:
                a_val = l[pointer+1]
            else:
                print("ERROR IN ASSIGNING A_VAL")
                break
            if b_mode == 0:
                b_val = l[l[pointer+2]]
            elif b_mode == 1:
                b_val = l[pointer+2]
            else:
                print("ERROR IN ASSIGNING B_VAL")
                break
            l[l[pointer+3]] = a_val * b_val
            pointer += 4
        
        elif operation == '03':
            l[l[pointer+1]] = input_val
            pointer += 2
            
        elif operation == '04':
            ret = l[l[pointer+1]]
            pointer += 2

        elif operation == '05':
            if a_mode == 0:
                a_val = l[l[pointer+1]]
            elif a_mode == 1:
                a_val = l[pointer+1]
            if a_val != 0:
                if b_mode == 0:
                    pointer = l[l[pointer+2]]
                r
                
            
    return ret
