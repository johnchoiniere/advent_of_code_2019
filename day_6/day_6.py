#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Dec  6 00:09:20 2019

@author: john
"""

# The number of orbits in a map formatted in this way -- INNER)OUTER ---
# can be counted by turning the map into a list of lists, where every 
# list within the uberlist is a distinct chain of orbits.
#
# I don't know if it's the most efficient way or not, but this can be
# created here within python by initializing with the center pairing of
# the map data (specified as COM)___, where COM = 'center of mass' and 
# the paired thing is unknown) and then finding matches of outer/inner.

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ Function Definitions ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# orbit_lister is a function that turns a map into a wide-formatted map. It
# requires a map file (where each line looks like 'AAA)BBB') read in with readlines().
def orbit_lister(l):
    # reformat the list to a list of lists, splitting on the ')' and 
    # cleaning up a little.
    l = [x.strip().split(')') for x in l]
    
    # a place to put the orbital chains
    chains = []
    
    # Identify the center of mass. Assumes it only links to
    # one outer object, but that can be changed in the future if needed. 
    # Add it to the chains list when found.
    center = [x for x in l if x[0]=='COM'][0]
    chains.append(center)
    
    # loop through all the chains that exist, including ones
    # that get added within the loop, which is neat. For each,
    # any matching next orbital object gets added on, but then
    # -- crucially -- it's added on to chains as a *new list*.
    # This ensures that all the sub-chains still exist independently
    # of the later, longer ones.
    for c in chains:
        for p in l:
            if c[len(c)-1] == p[0]:
                newchain = c+[p[1]]
                chains.append(newchain)
    
    # Return the list of lists
    return chains            

# transfer_counter takes a widened orbit map, as created by orbit_lister,
# and two object codes that are found within that map, and returns the 
# number of orbit transfers required to go from one to the other.
def transfer_counter(chain_list, obj1, obj2):
    
    # Pull out the full path to each object of interest
    obj1_FULL = [x for x in chain_list if obj1 in x][0]
    obj2_FULL = [x for x in chain_list if obj2 in x][0]
    
    # Isolate only the path points that are unique to the object;
    # that is, anything past the last shared point in the path back
    # to COM for each.
    obj1_UNIQUE = [x for x in obj1_FULL if x not in obj2_FULL]
    obj2_UNIQUE = [x for x in obj2_FULL if x not in obj1_FULL]
    
    # The number of orbital transfers between the two is the sum of
    # the length of each path, plus one to account for the fork, minus
    # two because you're not counting each object itself, minus one because
    # it takes n-1 moves to move a metaphorical cursor from position 0 to
    # position n (this is clearer in the explanation of the challenge at the
    # AoC site). That nets out to the lengths added, minus 2.
    transfers = len(obj1_UNIQUE) + len(obj2_UNIQUE) - 2
    
    return transfers


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ My specific problems ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# Read in my data
with open('input.txt') as f:
   infile = f.readlines()

# Use the function to make the wide map
chains = orbit_lister(infile)

# For part one I'm interested in the total number of orbits
# in the map, which is the sum of the length-minus-1 of each list in the 
# orbit_lister output. It's length minus 1 because the length is the number
# of objects in the path, and the orbits of the last object must necessarily
# be one less than that.
steps = 0
for x in chains:
    steps += len(x)-1

print("Part 1 answer: "+str(steps))


# For part two it's the output of the transfer_counter function
print("Part 2 answer: "+str(transfer_counter(chains, 'YOU','SAN')))