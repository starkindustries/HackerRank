# https://www.hackerrank.com/challenges/bomber-man/problem

def gridsMatch(g1, g2):
    for row in range(len(g1)):
        if not g1[row] == g2[row]:
            return False
    return True

def printGrid(grid):
    for row in grid:
        print(row)

def printGrids(g1, g2):
    for row in range(len(g1)):
        print(f"{g1[row]} {g2[row]}")

def bomberman(n, grid):    
    # for i in range(n):
    # initial state
    print("\nInitial:")
    printGrid(grid)
    if n % 4 == 1:
        return grid    

    # fill with bombs
    height = len(grid)
    width = len(grid[0])
    bombsFull = ["O" * width]*height

    print("\nBombs:")
    printGrid(bombsFull)
    if n % 4 == 2:
        return bombsFull

    # detonate bombs from initial state
    firstDet = [row for row in bombsFull]
    for row in range(height):
        for col in range(width):
            if grid[row][col] == "O":
                # explode locations to left and right
                x1 = (col - 1) if col > 1 else col
                x2 = (col + 1) if col < (width - 1) else col
                firstDet[row] = firstDet[row][:x1] + ("." * (x2-x1+1)) + firstDet[row][x2 + 1:]
                # explode locations above and below
                if row > 0:
                    firstDet[row - 1] = firstDet[row - 1][:col] + "." + firstDet[row-1][col+1:]
                if row < (height - 1):
                    firstDet[row + 1] = firstDet[row + 1][:col] + "." + firstDet[row + 1][col+1:]
    
    print("\nFirst Det:")
    printGrid(firstDet) 
    if n % 4 == 3:        
        return firstDet        

    print("\nBombs:")
    printGrid(bombsFull)
    if n % 4 == 0:
        return bombsFull     
        
    # bomber fills bombs again: return full state
    # second det happens: return original state
    # etc


# main
inputString = """
6 7 4
.......
...O.O.
....O..
..O....
OO...OO
OO.O...
"""
expectedString = """
.......
...O.O.
...OO..
..OOOO.
OOOOOOO
OOOOOOO
"""
lines = [line.strip() for line in inputString.splitlines() if not line.strip() == ""]
temp = lines.pop(0).split()
r, c, n = temp[0], temp[1], int(temp[2])
grid = bomberman(n, lines)
expectedGrid = [line.strip() for line in expectedString.splitlines() if not line.strip() == ""]
if gridsMatch(grid, expectedGrid):
    print("SUCCESS!")
else:
    print("TEST FAILED!")
    printGrids(grid, expectedGrid)