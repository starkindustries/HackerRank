#!/bin/python3

def searchGridForPlus(grid, plusLength):    
    # check edge cases where plus length is greater than the grid
    if len(grid) < plusLength:
        return None
    if len(grid[0]) < plusLength:
        return None

    # For plus length of 1, if 'G' exists return True        
    if plusLength == 1:
        for row in grid:
            if "G" in row:
                return True

    # For plus len > 1, return [row][col] coords of plus's center
    horizontalSegments = []
    # first check all horizontal segments of plusLen
    # spokeLen is one spoke on the plus, not including center
    spokeLen = plusLength // 2
    for row in range(spokeLen, len(grid) - spokeLen):
        for col in range(len(grid[0]) - spokeLen + 1):            
            # check substring of length plusLength
            segment = grid[row][col:col+plusLength]                
            if segment == ("G" * plusLength):
                horizontalSegments.append([row, col+(plusLength//2)])
    # then check the vertical portions of the horizontal segments
    validPluses = []
    for segment in horizontalSegments:        
        isValidPlus = True
        for i in range(1, spokeLen + 1):            
            if (grid[segment[0] + i][segment[1]] != "G") or (grid[segment[0] - i][segment[1]] != "G"):
                isValidPlus = False
                break            
        if isValidPlus:
            validPluses.append(segment)
    return validPluses

# Returns new grid if the plus can be placed
# Returns false if plus cannot be placed
def placePlusInGrid(grid, plus, symbol):
    symbol = str(symbol)    
    plusOrigin = plus[0]
    plusLength = plus[1]
    spokeLength = plusLength // 2
        
    # check all spoke coordinates
    coords = [[x, plusOrigin[1]] for x in range(plusOrigin[0]-spokeLength, plusOrigin[0]+spokeLength+1)]
    coords.extend([[plusOrigin[0], y] for y in range(plusOrigin[1]-spokeLength, plusOrigin[1]+spokeLength+1)])
    # Center is duplicated so remove one copy
    coords.remove([plusOrigin[0], plusOrigin[1]])
    for coord in coords:
        row, col = coord[0], coord[1]
        if not grid[row][col] == "G":
            return False
        else:
            grid[row] = grid[row][:col] + symbol + grid[row][col+1:]
    return grid

# Complete the twoPluses function below.
def twoPluses(grid):
    width = len(grid[0])
    height = len(grid)
    shorterSide = width if width < height else height
    
    # check for plus with len 3 to len shorterSize of grid
    validPluses = []
    for plusLength in range(3, shorterSide + 1, 2):
        pluses = searchGridForPlus(grid, plusLength)
        plusesAndLength = [[plus, plusLength] for plus in pluses]
        validPluses.extend(plusesAndLength)
            
    # From this point, I have all possible plus coordinates
    # Now determine largest two valid pluses    
    maxArea = 1 if searchGridForPlus(grid, 1) else 0
    # Loop through all pluses and place them in grid one at a time
    for plus1 in validPluses:
        onePlusGrid = placePlusInGrid([row for row in grid], plus1, 1)
        # now try placing all other pluses
        for plus2 in validPluses: 
            twoPlusGrid = placePlusInGrid([row for row in onePlusGrid], plus2, 2)
            if twoPlusGrid == False:
                continue
            # If plus successfully placed, multiply their areas
            area = (plus1[1] * 2 - 1) * (plus2[1] * 2 - 1)            
            maxArea = area if area > maxArea else maxArea
        # try placeing a plus of size 1        
        if searchGridForPlus(grid, 1):
            area = (plus1[1] * 2 - 1)
            maxArea = area if area > maxArea else maxArea                    
    return maxArea

if __name__ == '__main__':
    # Get input from test file
    fileName = "./EmaTestFile.txt"
    lines = []
    with open(fileName, 'r') as file_handle:
        for line in file_handle:        
            lines.append(line.strip())
    numTests = int(lines.pop(0).strip())

    # Loop through all test cases
    for _ in range(numTests):
        # first line is height width
        height = int(lines.pop(0)[0])
        grid = []
        for _ in range(height):
            grid.append(lines.pop(0))
        result = twoPluses(grid)
        expectedOutput = int(lines.pop(0))
        if expectedOutput == result:
            print(f"SUCCESS: {result}")
        else:
            print(f"TEST FAILED: {result} {expectedOutput}\n")            
            for row in grid:
                print(row)
            print("\n")
