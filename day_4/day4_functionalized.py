#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Dec  3 21:54:16 2019

@author: john
"""

# This function takes a starting and ending integer and returns the number
# of integers in that range that match the criteria of AOC day 4

def number_of_matches(start,end):
    # Empty lists to append to
    matches = []
    refined_matches = []

    # Loop over the defined range to find P1 matches
    for x in range(start, end):
        n = [int(i) for i in [char for char in str(x)]]     # The only way to satisfy the criteria is if the set of sequential differences between the numbers in the list
        diffs = []                                          # has a minimum value of zero; if it does, that means there's at least one pair of consecutive numbers and no decreases.
        for j in range(len(n)-1):                           #  
            diffs.append(n[j+1]-n[j])                       # This stage therefore creates a list of all differences and checks if the min is zero.
        if min(diffs)==0:                                   #
            matches.append(x)                               # It should be flexible to any length integer, though I can't speak to run times for long ones.
    
    # Loop through *those* matches to apply the additional criterion      
    for x in matches:
        n = [int(i) for i in [char for char in str(x)]]     # Rather than starting from scratch, it operates only on the saved match
        for j in range(len(n)-1):                           # and applies the single additional criterion -- checking surrounding numbers
            if j == 0:                                      # to find at least one pair-match (rather than longer runs)
                if n[j] == n[j+1] and n[j] != n[j+2]:
                    refined_matches.append(x)
            elif j == len(n)-2:
                if n[j] == n[j+1] and n[j] != n[j-1]:
                    refined_matches.append(x)
            else:
                if n[j] == n[j+1] and n[j] != n[j+2] and n[j] != n[j-1]:
                    refined_matches.append(x)
    
    # Remove duplicates -- this method is fast, but does not preserve order
    refined_matches = list(set(refined_matches))
    
    # Return the two values of interest
    return len(matches), len(refined_matches)

# My particular starts and ends
s = 153517
e = 630395

# Run the function
p1, p2 = number_of_matches(s, e)

#Print the results
print("Part 1 answer: "+str(p1))
print("Part 2 answer: "+str(p2))