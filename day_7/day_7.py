# -*- coding: utf-8 -*-
"""
Created on Sun Dec  8 11:35:38 2019

@author: john
"""

def intcode(input_list, l):
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
            l[l[pointer+1]] = int(input_list.pop(0))
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



# Read the parameter permutations in
with open('permutations.txt') as f:
    param_list = f.readlines()

# Format it to how I want it
param_list = [i.strip().strip('\"') for i in param_list][1:]

# Read the program in, five times
with open('input.txt') as f:
    program = f.readlines()[0].split(',')
    
# Make it into an instruction list
p1 = [int(i.strip()) for i in program]
p2 = [int(i.strip()) for i in program]
p3 = [int(i.strip()) for i in program]
p4 = [int(i.strip()) for i in program]
p5 = [int(i.strip()) for i in program]

# Make a place for the results
results = []

# Loop through the permutations
for p in param_list:
    input_val = 0
    input_list = [p[0],input_val]
    
    new_val = intcode(input_list, p1)
    new_list = [p[1],new_val]
    
    new_val = intcode(new_list, p2)
    new_list = [p[2],new_val]
    
    new_val = intcode(new_list, p3)
    new_list = [p[3], new_val]
    
    new_val = intcode(new_list, p4)
    new_list = [p[4], new_val]
    
    new_val = intcode(new_list, p5)
    
    results.append([new_val, p])

# Pull the max output
best_param = [i[1] for i in results if i[0] == max([j[0] for j in results])]