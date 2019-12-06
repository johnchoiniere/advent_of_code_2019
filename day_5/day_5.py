# -*- coding: utf-8 -*-
"""
Created on Mon Dec  2 11:06:47 2019

@author: jchoiniere
"""

# read in the data; I'm... not great at doing I/O in python, tbh
with open('input.txt') as f:
    infile = f.readlines()[0].strip().split(',')

# A function to return the 'diagnostic code' based on
# a provided input value and a list that is the 'opcode program'.
def opcode_d5(input_val, l):
    l = [int(x) for x in l]     # Convert list values to ints
    end = False                 # set up a condition for the while
    pointer = 0                 # initialize the pointer to the first position
    
    # Enter the while loop. Continues as long as end is false,
    # and hitting operation 99 sets end to true.
    while not end:
        instruct = str(l[pointer]).rjust(5,'0')
        operation = instruct[len(instruct)-2:]
        
        # Do a little error-handling: break if the mode parameter is invalid for a or b
        if(int(instruct[2])>1):
            print("A_MODE INVALID\nPointer: "+str(pointer)+", Instruction: "+instruct+"\n")
            break
        
        if(int(instruct[1])>1):
            print("B_MODE INVALID\nPointer: "+str(pointer)+", Instruction: "+instruct+"\n")
            break
        
        # Safe because error-handling above means instruct[1] and [2] _must_ be 0 or 1.
        # This absolutely will assign values that are outside of the scope of the command
        # but since they won't be used who cares.
        if operation in ('01','02','05','06','07','08'):
            a_val = l[l[pointer+1]] if instruct[2]=='0' else l[pointer+1]
        if operation in ('01','02','05','06','07','08'):
            b_val = l[l[pointer+2]] if instruct[1]=='0' else l[pointer+2]
        
        # Run through the possible operations. 99: end.
        if operation == '99':
            end = True
        
        # 01: add and place
        elif operation == '01':
            l[l[pointer+3]] = a_val + b_val
            pointer += 4
        
        # 02: multiply and place
        elif operation == '02':
            l[l[pointer+3]] = a_val * b_val
            pointer += 4
        
        # 03: input
        elif operation == '03':
            l[l[pointer+1]] = input_val
            pointer += 2
        
        # 04: return
        elif operation == '04':
            ret = l[l[pointer+1]]
            pointer += 2

        # 05: jump-if-true
        elif operation == '05':
            if a_val != 0:
                pointer = b_val
            else:
                 pointer += 3
        
        # 06: jump-if-false
        elif operation == '06':
            if a_val == 0:
                pointer = b_val
            else:
                pointer += 3

        # 07: less-than flag
        elif operation == '07':
            if a_val < b_val:
                l[l[pointer+3]] = 1
            else:
                l[l[pointer+3]] = 0
            pointer += 4
        
        # 08: equals flag
        elif operation == '08':
            if a_val == b_val:
                l[l[pointer+3]] = 1
            else:
                l[l[pointer+3]] = 0
            pointer += 4
            
    return ret

# Execute my specific stuff.
p1 = opcode_d5(1, infile)
p2 = opcode_d5(5, infile)

print("Part 1 answer: "+str(p1))
print("Part 2 answer: "+str(p2))