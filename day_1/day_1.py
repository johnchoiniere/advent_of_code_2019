# -*- coding: utf-8 -*-
"""
Created on Mon Dec  2 11:01:24 2019

@author: jchoiniere
"""

from math import floor

with open('input.txt') as f:
    lines = f.read().splitlines()
    
weights = []

for l in lines:
    weights.append(int(l))
    
fuel = []
for w in weights:
    fuel.append(floor(w/3)-2)
    
print("Part 1 answer: "+str(sum(fuel)))

fuel = []

for w in weights:
    new_fuel = floor(w/3)-2
    total = new_fuel
    while new_fuel > 0:
        new_fuel = max(0,floor(new_fuel/3)-2)
        total += new_fuel
    fuel.append(total)
    
print("Part 2 answer: "+str(sum(fuel)))