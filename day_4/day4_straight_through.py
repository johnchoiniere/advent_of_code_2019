#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Dec  3 23:29:57 2019

@author: john
"""

start = 153517
end = 630395

matches = []

for x in range(start, end):
    n = [int(i) for i in [char for char in str(x)]]
    diffs = []
    for j in range(len(n)-1):
        diffs.append(n[j+1]-n[j])
    if min(diffs)==0:
        matches.append(x)


print("Part 1 answer: "+str(len(matches)))

p2matches = []

for x in matches:
    n = [int(i) for i in [char for char in str(x)]]
    if n[0] == n[1] and n[0] != n[2]:
        p2matches.append(x)
    elif n[1] == n[2] and n[1] != n[0] and n[1] != n[3]:
        p2matches.append(x)
    elif n[2] == n[3] and n[2] != n[1] and n[2] != n[4]:
        p2matches.append(x)
    elif n[3] == n[4] and n[3] != n[2] and n[3] != n[5]:
        p2matches.append(x)
    elif n[4] == n[5] and n[4] != n[3]:
        p2matches.append(x)


print("Part 2 answer: "+str(len(p2matches)))