#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Dec  3 00:19:41 2019

@author: john
"""
# read in input
with open('input.txt') as f:
    infile = f.readlines()

# make it intotwo nice, easy lists of steps    
wire1 = infile[0].split(',')
wire2 = infile[1].split(',')

def intersect_finder(wire1, wire2):
    # set up coordinate lists
    coords_w1 = []
    coords_w2 = []

    # set up starting points
    x1 = 0
    y1 = 0
    x2 = 0
    y2 = 0

    # loop through wire, adding the new coordinates to the lisy
    for d in wire1:
        w = d[0]        # the direction to go
        n = int(d[1:])  # the number of steps
        for i in range(n):
            if w == 'R':
                x1 += 1
                coords_w1.append([x1,y1])
            elif w == 'L':
                x1 -= 1
                coords_w1.append([x1,y1])
            elif w == 'U':
                y1 += 1
                coords_w1.append([x1,y1])
            elif w == 'D':
                y1 -= 1
                coords_w1.append([x1,y1])

    # same for wire 2
    for d in wire2:
        w = d[0]
        n = int(d[1:])
        for i in range(n):
            if w == 'R':
                x2 += 1
                coords_w2.append([x2,y2])
            elif w == 'L':
                x2 -= 1
                coords_w2.append([x2,y2])
            elif w == 'U':
                y2 += 1
                coords_w2.append([x2,y2])
            elif w == 'D':
                y2 -= 1
                coords_w2.append([x2,y2])

    # intersecting pts are the coords that
    # are in both lists
    intersections = [i for i in coords_w1 if i in coords_w2]
    
    # Manhattan distances of intersects
    distances = [abs(c[0])+abs(c[1]) for c in intersections]
    p1 = min(distances)

    # use index to find n(steps) to get to point
    steps = [coords_w1.index(i) + coords_w2.index(i) + 2 for i in intersections]
    p2 = min(steps)
    return p1, p2

part1, part2 = intersect_finder(wire1,wire2)
print("Part 1 answer: " + str(part1))
print("Part 2 answer: " + str(part2))
