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

    # if seconds is even, return the all bombs grid
    height, width = len(grid), len(grid[0])
    allBombsGrid = ["O" * width] * height
    if n % 2 == 0:
        return allBombsGrid    
    
    # If we made it this far, we need to detonate some bombs
    # store bomb states with key: value of state: order
    bombStateIndex = 0
    bombStateRepeatedIndex = None
    bombStates = { " ".join(grid) : bombStateIndex }    
    
    lastState = [row for row in grid]        
    for i in range(3, n + 1, 2):
        detonatedGrid = [row for row in allBombsGrid]
        for row in range(height):
            for col in range(width):
                if lastState[row][col] == "O":
                    # explode locations to left and right
                    x1 = (col - 1) if col > 0 else col
                    x2 = (col + 1) if col < (width - 1) else col
                    detonatedGrid[row] = detonatedGrid[row][:x1] + ("." * (x2-x1+1)) + detonatedGrid[row][x2 + 1:]
                    # explode locations above and below
                    if row > 0:
                        detonatedGrid[row - 1] = detonatedGrid[row - 1][:col] + "." + detonatedGrid[row-1][col+1:]
                    if row < (height - 1):
                        detonatedGrid[row + 1] = detonatedGrid[row + 1][:col] + "." + detonatedGrid[row + 1][col+1:]                    
        detGridString = " ".join(detonatedGrid)
        if detGridString in bombStates:
            bombStateRepeatedTime = i
            bombStateRepeatedIndex = bombStates[detGridString]
            break
        else:
            bombStateIndex += 1
            bombStates[detGridString] = bombStateIndex                
        lastState = [x for x in detonatedGrid]
        # Now repeat    
    
    if not bombStateRepeatedIndex is None:
        # Assume that there can only be a pair of two repeated states
        # print(f"max index: {bombStateIndex}, repeated at: {bombStateRepeatedIndex}, time: {bombStateRepeatedTime}")
        # n % 4 == 1 is determined by looking at the sequence
        # if 7s: return grid 1. if 9s return grid 2
        # if 11s: 1. if 13s: 2.
        # if 15s: 1. if 17s: 2. Note that all grid 2's have 'n' % 4 == 1.
        if n % 4 == 1:
            for gridString, index in bombStates.items():
                if index == 2:
                    return [line for line in gridString.split()]
        else:
            for gridString, index in bombStates.items():
                if index == 1:
                    return [line for line in gridString.split()]                    
    else:    
        return lastState

# main
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