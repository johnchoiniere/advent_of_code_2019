#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Dec  6 00:09:20 2019

@author: john
"""
import pandas as pd

with open('input.txt') as f:
   infile = f.readlines()
    
infile = [x.strip().split(')') for x in infile]
    
infile_df = pd.DataFrame(infile)

chains = []

center = [x for x in infile if x[0]=='COM'][0]

chains.append(center)

for c in chains:
    for p in infile:
        if c[len(c)-1] == p[0]:
            newchain = c+[p[1]]
            chains.append(newchain)
            
steps = 0
for x in chains:
    steps += len(x)-1

print("Part 1 answer: "+str(steps))
    
SANTA_FULL = [x for x in chains if 'SAN' in x][0]
YOU_FULL = [x for x in chains if 'YOU' in x][0]

SANTA = [x for x in SANTA_FULL if x not in YOU_FULL]
YOU = [x for x in YOU_FULL if x not in SANTA_FULL]

transfers = len(SANTA) + len(YOU) - 2

print("Part 2 answer: "+str(transfers))