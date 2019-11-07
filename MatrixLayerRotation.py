# Matrix Layer Rotation
# https://www.hackerrank.com/challenges/matrix-rotation-algo/problem

#!/bin/python3
import math
import os
import random
import re
import sys
# https://stackoverflow.com/questions/2150108/efficient-way-to-rotate-a-list-in-python
from collections import deque

def traverseMatrixRings(matrix):
    x0, y0 = 0, 0
    xM, yM = len(matrix[0]), len(matrix)    
    rings = []
    while x0 < xM and y0 < yM:        
        ring = []
        # traverse outside of matrix
        # top-left to bottom-left
        x = x0
        for y in range(y0, yM):
            ring.append(matrix[y][x])
        
        # bottom-left to bottom-right
        y = yM-1
        for x in range(x0+1, xM):
            ring.append(matrix[y][x])
        
        # bottom-right to top-right
        x = xM-1
        for y in range(yM-2, y0-1, -1):
            ring.append(matrix[y][x])
        
        # top-right to top-left
        y = y0
        for x in range(xM-2, x0, -1):
            ring.append(matrix[y][x])            
                
        # ring traversed!        
        rings.append(ring)
        # move to inner ring
        x0 += 1
        y0 += 1
        xM -= 1
        yM -= 1            
    return rings

def reconstructMatrix(matrix, rings):
    x0, y0 = 0, 0
    xM, yM = len(matrix[0]), len(matrix)
    
    j = 0
    while x0 < xM and y0 < yM:
        ring = rings[j]
        # traverse outside of matrix
        # top-left to bottom-left
        i = 0
        x = x0
        for y in range(y0, yM):
            matrix[y][x] = ring[i]
            i += 1
        
        # bottom-left to bottom-right
        y = yM-1
        for x in range(x0+1, xM):
            matrix[y][x] = ring[i]
            i += 1
        
        # bottom-right to top-right
        x = xM-1
        for y in range(yM-2, y0-1, -1):
            matrix[y][x] = ring[i]
            i += 1
        
        # top-right to top-left
        y = y0
        for x in range(xM-2, x0, -1):
            matrix[y][x] = ring[i]
            i += 1        
        # ring traversed!                
        # move to inner ring
        x0 += 1
        y0 += 1
        xM -= 1
        yM -= 1
        j += 1    
    return matrix

# Complete the matrixRotation function below.
def matrixRotation(matrix, r):
    # Calculate number of rings
    # Start from 0,0 traverse edge. remove outer ring.
    # Next 1, 1 traverse this edge. that's another ring
    # next 2, 2, traverse. That's another
    # until you cannot traverse anymore
    # 1. Get all rings into their own array
    rings = traverseMatrixRings(matrix)
    
    # 2. Rotate rings
    # Any rotation can be reduced to: # rotations % len(rings)
    # This avoids full circle loops
    tempRings = []
    for ring in rings:
        temp = deque(ring)
        temp.rotate(r % len(ring))        
        tempRings.append(list(temp))
    rings = tempRings    

    # 3. Reconstruct matrix
    matrix = reconstructMatrix(matrix, rings)

    # 4. Return rotated matrix
    return matrix

def printMatrix(matrix):
    print("")
    for row in matrix:
        print(" ".join([str(n).zfill(2) for n in row]))
    print("")

if __name__ == '__main__':
    inputString = """
    5 4 7
    1 2 3 4 5
    7 8 9 10 11 
    13 14 15 16 22
    19 20 21 22 33    
    """
    lines = [line.strip() for line in inputString.splitlines() if not line.strip() == ""]
    mnr = list(map(int, lines.pop(0).split()))
    m, n, r = mnr[0], mnr[1], mnr[2]    
    
    matrix = [[int(n) for n in line.split()] for line in lines]    
    printMatrix(matrix)
    
    matrix = matrixRotation(matrix, r)
    printMatrix(matrix)
