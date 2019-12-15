from pprint import pprint
import logging

# sudoku

USE_EQUATIONS = False
logging.basicConfig(level=logging.INFO)


def debug():
    return logging.getLogger().isEnabledFor(logging.DEBUG)


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
                logging.debug(f" {pos} = {puzzle[pos[0]][int(pos[1])-1].value}")
                cell = puzzle[pos[0]][int(pos[1])-1]
                if cell.value != 0:
                    result += cell.value
                elif len(cell.possibleValues) > 0:
                    result += list(cell.possibleValues)[0]
        logging.debug(f"result: {result}")
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

    def setValue(self, value):
        self.value = value
        self.possibleValues = set()

    def update(self):
        if self.value == 0 and len(self.possibleValues) == 1:
            self.value = list(self.possibleValues)[0]
            self.possibleValues = set()
            return True
        return False

    def addPossible(self, value):
        if self.value == 0:
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


def convertIntToRow(n):
    return ["A", "B", "C", "D", "E", "F", "G", "H", "I"][n]


def isPossiblyValid(number, position, puzzle):
    # check validity using the rules of sudoku
    row = position[0]
    col = int(position[1])
    for i, cell in enumerate(puzzle[row]):
        if cell.value == number and i != col:
            return False

    for key, cells in puzzle.items():
        if cells[col].value == number and key != row:
            return False

    # check quadrant
    colRanges = [[0, 1, 2], [3, 4, 5], [6, 7, 8]]
    rowRanges = [["A", "B", "C"], ["D", "E", "F"], ["G", "H", "I"]]
    colRange = colRanges[col // 3]
    rowRange = rowRanges[convertRowToInt(row) // 3]
    for row in rowRange:
        for col in colRange:
            if puzzle[row][col].value == number and f"{row}{col}" != position:
                return False

    # check if the number is the only valid number using crosshatching
    validCells = []
    for row in rowRange:
        for col in colRange:
            validCells.append(f"{row}{col}")
    for row in rowRange:
        for cell in puzzle[row]:
            if number == cell.value:
                validCells = [x for x in validCells if row not in x]
    for row in puzzle:
        for col in colRange:
            if number == puzzle[row][col].value:
                validCells = [x for x in validCells if str(col) not in x]
    # also remove any cells that already contain a value
    for cell in list(validCells):
        value = puzzle[cell[0]][int(cell[1])].value
        if value != 0 and value in validCells:
            validCells.remove(cell)
    # check if only one valid cell remains
    if len(validCells) == 1:
        return validCells[0]

    if not USE_EQUATIONS:
        return True
    # AND check using the equations
    # EquationMap maps positions to equations.
    # E.g. B9 => (B9 + B8 + C1 + H4 + H4 = 23)
    if position in equationMap:
        for e in equationMap[position]:
            result = e.solve(number, position, puzzle)
            if not result:
                logging.debug(f"Result: {result}. Value {number} at {position} failed to pass equation: {e}")
                return False
    return True


def attemptToSolveOneValue(puzzle):
    # iterate through each cell.
    for key, row in puzzle.items():
        for i in range(len(row)):
            currentCell = row[i]
            if currentCell.value == 0:
                # for each cell, check if a number is valid.
                for possibleValue in range(1, 10):
                    # if a number is valid, add it to potential values
                    result = isPossiblyValid(possibleValue, f"{key}{i}", puzzle)
                    if isinstance(result, str):
                        # if string returned then a confirmed location was found
                        puzzle[result[0]][int(result[1])].setValue(possibleValue)
                        logging.info(f"updated cell: {key}{i} with value {possibleValue}")
                        return True
                    elif result:
                        currentCell.addPossible(possibleValue)
                    else:  # if not, remove it from potential values
                        currentCell.removePossible(possibleValue)

    # once done iterating through all cells, check if any cell has only one potential value
    for key, row in puzzle.items():
        for i, cell in enumerate(row):
            # this checks if the cell has only 1 value
            if cell.update():
                logging.info(f"updated cell: {key}{i} with value {cell.value}")
                return True
    return False


def validatePuzzle(puzzle):
    for key, row in puzzle.items():
        for i, cell in enumerate(row):
            if cell.value == 0:
                continue
            elif not isPossiblyValid(cell.value, f"{key}{i}", puzzle):
                logging.error(f" Incorrect value {cell.value} at {key}{i}.")


def solve(tempPuzzle):
    # convert puzzle to 2d array of cells
    puzzle = {}
    for key, values in tempPuzzle.items():
        cellValues = [Cell(x) for x in values]
        puzzle[key] = cellValues

    while True:
        if attemptToSolveOneValue(puzzle):
            continue
        else:
            break

    logging.info("\n=================================")
    for key, row in puzzle.items():
        print(f"{key}: {row}")
    print("\n")

    validatePuzzle(puzzle)


if __name__ == "__main__":
    puzzle = {
        #     0  1  2   3  4  5   6  7  8
        "A": [0, 0, 0,  0, 0, 0,  0, 0, 1],
        "B": [0, 1, 2,  0, 0, 0,  0, 0, 0],
        "C": [0, 0, 0,  0, 0, 0,  2, 0, 0],

        "D": [0, 0, 0,  0, 0, 0,  0, 0, 2],
        "E": [0, 2, 0,  0, 0, 0,  0, 0, 0],
        "F": [0, 0, 0,  0, 0, 0,  0, 0, 0],

        "G": [0, 0, 0,  0, 0, 0,  1, 2, 0],
        "H": [1, 0, 0,  0, 0, 2,  0, 0, 0],
        "I": [2, 0, 0,  1, 0, 0,  0, 0, 0],
    }

    for key, value in puzzle.items():
        logging.debug(f"{key}: {value}")

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
    if debug():
        print("\nEquation map:")
        pprint(equationMap)

    temp = """
        000004903
        004019600
        109086204
        010940020
        030602090
        060070000
        650001070
        090000008
        000000002
    """
    temp = [x.strip() for x in temp.splitlines() if x.strip() is not ""]
    print(temp)
    for i in range(9):
        row = convertIntToRow(i)
        tempRow = [int(x) for x in list(temp[i])]
        puzzle[row] = tempRow
    pprint(puzzle)
    # Solve
    solve(puzzle)
