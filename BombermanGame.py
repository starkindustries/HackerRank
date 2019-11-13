# https://www.hackerrank.com/challenges/bomber-man/problem

def gridsMatch(g1, g2):
    for row in range(len(g1)):
        for col in range(len(g1[0])):
            if not g1[row][col] == g2[row][col]:
                print(f"Test failed at: [{row}][{col}]")
                return False
    return True

def printGrid(grid):
    fileName = "output.txt"
    with open(fileName, 'w') as file_handle:
        for row in grid:
            print(row, file=file_handle)

def printGrids(g1, g2):
    for row in range(len(g1)):
        print(f"{g1[row]} {g2[row]}")

def bomberman(n, grid):
    # 1 second, do nothing
    if n == 1:    
        return grid

    height, width = len(grid), len(grid[0])
    
    # store bomb states with key: value of state: order
    bombStates = {}
        
    lastState = None    
    for i in range(2, n + 1):     
        # 2 seconds, fill bombs
        if i % 2 == 0:            
            bombs = ["O" * width] * height
            lastState = bombs
            continue           
        else: # 3 seconds, detonate bombs     
            firstDet = [row for row in bombs]
            for row in range(height):
                for col in range(width):
                    if grid[row][col] == "O":
                        # explode locations to left and right
                        x1 = (col - 1) if col > 0 else col
                        x2 = (col + 1) if col < (width - 1) else col
                        firstDet[row] = firstDet[row][:x1] + ("." * (x2-x1+1)) + firstDet[row][x2 + 1:]
                        # explode locations above and below
                        if row > 0:
                            firstDet[row - 1] = firstDet[row - 1][:col] + "." + firstDet[row-1][col+1:]
                        if row < (height - 1):
                            firstDet[row + 1] = firstDet[row + 1][:col] + "." + firstDet[row + 1][col+1:]            
            lastState = firstDet
            grid = [x for x in firstDet]
        # Now repeat
    return lastState


# main
# inputString = """
# 6 7 5
# .......
# ...O.O.
# ....O..
# ..O....
# OO...OO
# OO.O...
# """
# expectedString = """
# .......
# ...O.O.
# ...OO..
# ..OOOO.
# OOOOOOO
# OOOOOOO
# """
# lines = [line.strip() for line in inputString.splitlines() if not line.strip() == ""]
# expectedGrid = [line.strip() for line in expectedString.splitlines() if not line.strip() == ""]

# Input file
fileName = "./BombermanTestInput.txt"
lines = []
with open(fileName, 'r') as file_handle:
    for line in file_handle:        
        lines.append(line.strip())

n = int(lines.pop(0).split()[2])
grid = bomberman(n, lines)

# Expected Output file
fileName = "./BombermanTestOutput.txt"
expectedGrid = []
with open(fileName, 'r') as file_handle:
    for line in file_handle:        
        expectedGrid.append(line.strip())

if gridsMatch(grid, expectedGrid):
    print("SUCCESS!")
else:
    print("TEST FAILED!")    
# printGrid(grid)