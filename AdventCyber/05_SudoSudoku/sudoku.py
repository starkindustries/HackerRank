from pprint import pprint as print
import logging

# sudoku

logging.basicConfig(level=logging.DEBUG)

"""
Santa's little helpers are notoriously good at solving Sudoku puzzles.
Because regular Sudoku puzzles are too trivial, they have invented a variant.

    1 2 3   4 5 6   7 8 9
  +-------+-------+-------+
A | . . . | . . . | . . 1 |
B | . 1 2 | . . . | . . . |
C | . . . | . . . | 2 . . |
  +-------+-------+-------+
D | . . . | . . . | . . 2 |
E | . 2 . | . . . | . . . |
F | . . . | . . . | . . . |
  +-------+-------+-------+
G | . . . | . . . | 1 2 . |
H | 1 . . | . . 2 | . . . |
I | . . . | 1 . . | . . . |
  +-------+-------+-------+

In addition to the standard Sudoku puzzle above,
the following equations must also hold:

B9 + B8 + C1 + H4 + H4 = 23
A5 + D7 + I5 + G8 + B3 + A5 = 19
I2 + I3 + F2 + E9 = 15
I7 + H8 + C2 + D9 = 26
I6 + A5 + I3 + B8 + C3 = 20
I7 + D9 + B6 + A8 + A3 + C4 = 27
C7 + H9 + I7 + B2 + H8 + G3 = 31
D3 + I8 + A4 + I6 = 27
F5 + B8 + F8 + I7 + F1 = 33
A2 + A8 + D7 + E4 = 21
C1 + I4 + C2 + I1 + A4 = 20
F8 + C1 + F6 + D3 + B6 = 25

If you then read the numbers clockwise starting from A1 to A9, to I9, to I1 and
back to A1, you end up with a number with 32 digits.  Enclose that in AOTW{...}
to get the flag.
"""


class Equation:
    def __init__(self, left, right):
        self.left = left
        self.right = right

    def __repr__(self):
        return f"{self.left} = {self.right}"

    def __str__(self):
        return f"{self.left} = {self.right}"

    def solve(self, value, position, puzzle):
        result = 0
        for pos in self.left:
            if pos == position:
                result += value
            else:
                result += puzzle[position[0]][int(position[1])].value
        if result > self.right:
            return False
        return (result, self.right)


class Cell:
    def __init__(self):
        self.value = None
        self.possibleValues = set()

    def __init__(self, value):
        self.value = value
        self.possibleValues = set()

    def update(self):
        if self.value == 0 and len(self.possibleValues) == 1:
            print("YESSSSSSSSSSSSSS!!!!!!!!!!!!!")
            self.value = self.possibleValues[0]
            self.possibleValues = set()

    def addPossible(self, value):
        self.possibleValues.add(value)

    def removePossible(self, value):
        if value in self.possibleValues:
            self.possibleValues.remove(value)

    def __repr__(self):
        return f"{self.value}:{''.join(str(x) for x in self.possibleValues)}"

    def __str__(self):
        return f"{self.value}:{''.join(str(x) for x in self.possibleValues)}"


# Maps positions to equations.
# E.g. B9 => (B9 + B8 + C1 + H4 + H4 = 23)
equationMap = {}


def convertToEquation(line):
    left, right = [x.strip() for x in line.split("=")]
    left = [x.strip() for x in left.split("+")]
    right = int(right)
    equation = Equation(left, right)

    # add equation to the equationMap
    for position in left:
        if position in equationMap:
            equationMap[position].append(equation)
        else:
            equationMap[position] = [equation]
    return equation


def convertRowToInt(row):
    return ["A", "B", "C", "D", "E", "F", "G", "H", "I"].index(row)


def isPossiblyValid(number, position, puzzle):
    # check validity using the rules of sudoku
    row = position[0]
    for cell in puzzle[row]:
        if cell.value == number:
            return False

    col = int(position[1])
    for key, cells in puzzle.items():
        if cells[col].value == number:
            return False

    # check quadrant
    colRanges = [[0, 1, 2], [3, 4, 5], [6, 7, 8]]
    rowRanges = [["A", "B", "C"], ["D", "E", "F"], ["G", "H", "I"]]
    colRange = colRanges[col // 3]
    rowRange = rowRanges[convertRowToInt(row) // 3]
    for row in rowRange:
        for col in colRange:
            if puzzle[row][col].value == number:
                return False

    # AND using the equations
    # EquationMap maps positions to equations.
    # E.g. B9 => (B9 + B8 + C1 + H4 + H4 = 23)
    if position in equationMap:
        equations = equationMap[position]
        for e in equations:
            result = e.solve(number, position, puzzle)
            if not result:
                return False
    return True


def solve(tempPuzzle, equations):
    # convert puzzle to 2d array of cells
    puzzle = {}
    for key, values in tempPuzzle.items():
        cellValues = [Cell(x) for x in values]
        puzzle[key] = cellValues

    # iterate through each cell.
    for key, row in puzzle.items():
        for i in range(len(row)):
            currentCell = row[i]
            if currentCell.value == 0:
                # for each cell, check if a number is valid.
                for possibleValue in range(1, 10):
                    # if a number is valid, add it to potential values
                    if isPossiblyValid(possibleValue, f"{key}{i}", puzzle):
                        currentCell.addPossible(possibleValue)
                    else:  # if not, remove it from potential values
                        currentCell.removePossible(possibleValue)

    # once done iterating through all cells, check if any cell has only one potential value
    for key, row in puzzle.items():
        for cell in row:
            # this checks if the cell has only 1 value
            cell.update()

    print("=================================")
    print(puzzle)
    pass


if __name__ == "__main__":
    puzzle = {
        "A": [0, 0, 0,  0, 0, 0,  0, 0, 1],
        "B": [0, 1, 2,  0, 0, 0,  0, 0, 0],
        "C": [0, 0, 0,  0, 0, 0,  2, 0, 0],

        "D": [0, 0, 0,  0, 0, 0,  0, 0, 2],
        "E": [0, 2, 0,  0, 0, 0,  0, 0, 0],
        "F": [0, 0, 0,  0, 0, 0,  0, 0, 0],

        "G": [0, 0, 0,  0, 0, 0,  1, 2, 0],
        "H": [1, 0, 0,  0, 0, 2,  0, 0, 0],
        "I": [0, 0, 0,  1, 0, 0,  0, 0, 0],
    }
    for key, value in puzzle.items():
        print(f"{key}: {value}")

    rawEquations = """
    B9 + B8 + C1 + H4 + H4 = 23
    A5 + D7 + I5 + G8 + B3 + A5 = 19
    I2 + I3 + F2 + E9 = 15
    I7 + H8 + C2 + D9 = 26
    I6 + A5 + I3 + B8 + C3 = 20
    I7 + D9 + B6 + A8 + A3 + C4 = 27
    C7 + H9 + I7 + B2 + H8 + G3 = 31
    D3 + I8 + A4 + I6 = 27
    F5 + B8 + F8 + I7 + F1 = 33
    A2 + A8 + D7 + E4 = 21
    C1 + I4 + C2 + I1 + A4 = 20
    F8 + C1 + F6 + D3 + B6 = 25
    """
    rawEquations = [x.strip() for x in rawEquations.splitlines() if x.strip() != ""]
    equations = []
    for e in rawEquations:
        equations.append(convertToEquation(e))
    print(equations)

    # Solve
    solve(puzzle, equations)
