# https://stackoverflow.com/questions/201461/shortest-sudoku-solver-in-python-how-does-it-work#

# Single array Sudoku Grid
# 00 01 02 03 04 05 06 07 08
# 09 10 11 12 13 14 15 16 17
# 18 19 20 21 22 23 24 25 26
# 27 28 29 30 31 32 33 34 35
# 36 37 38 39 40 41 42 43 44
# 45 46 47 48 49 50 51 52 53
# 54 55 56 57 58 59 60 61 62
# 63 64 65 66 67 68 69 70 71
# 72 73 74 75 76 77 78 79 80
from pprint import pprint
import sys
import logging

logging.basicConfig(level=logging.DEBUG)


# ========================================
# Sudoku Functions
# ========================================


def sameRow(a, b):
    return (a // 9 == b // 9)


def sameCol(a, b):
    return (a % 9 == b % 9)


def sameNonet(a, b):
    same3Rows = a // 27 == b // 27
    same3Cols = (a % 9 // 3) == (b % 9 // 3)
    return same3Rows and same3Cols


def solve(puzzle, equations):
    emptyCell = puzzle.find('.')
    if emptyCell == -1:
        logging.info(f"{puzzle} <== solution found")
        sys.exit(puzzle)

    # rule out all invalid numbers.
    # if a number is within the same row, col, or nonet then it is invalid
    invalidNumbers = set()
    for i in range(81):
        if sameRow(emptyCell, i) or sameCol(emptyCell, i) or sameNonet(emptyCell, i):
            invalidNumbers.add(puzzle[i])

    # Now iterate through all valid numbers and place into puzzle
    for number in "123456789":
        if number in invalidNumbers:
            continue
        # check if modifying the empty cell with one of the numbers creates an invalid equation
        puzzle = puzzle[:emptyCell] + number + puzzle[emptyCell+1:]
        if number in equations:
            for e in equations[number]:
                result = e.solve(puzzle)
                if result > 0:
                    # result > 0 means the result is greater than equation's right side
                    continue
        solve(puzzle, equations)
    logging.debug(f"No solution for: {puzzle}")


# ========================================
# Equation Functions
# ========================================


def convertPosToIndex(pos):
    return "ABCDEFGHI".find(pos[0]) * 9 + (int(pos[1]) - 1)


class Equation:
    def __init__(self, line):
        left, right = [x.strip() for x in line.split("=")]
        left = [x.strip() for x in left.split("+")]
        right = int(right)
        self.left = left
        self.right = right

    def __repr__(self):
        return f"{self.left} = {self.right}"

    def __str__(self):
        return f"{self.left} = {self.right}"

    def solve(self, puzzle):
        result = 0
        for pos in self.left:
            index = convertPosToIndex(pos)
            logging.debug(f" {pos} = {puzzle[index]}")
            result += int(puzzle[index])
        logging.debug(f"result: {result}, expected: {self.right}")
        if result == self.right:
            return 0
        elif result < self.right:
            return -1
        else:
            return 1


def createEquations(equations=None):
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
    if equations is not None:
        rawEquations = equations

    rawEquations = [x.strip() for x in rawEquations.splitlines() if x.strip() != ""]
    equations = {}
    for e in rawEquations:
        temp = Equation(e)
        for pos in temp.left:
            index = convertPosToIndex(pos)
            if index in equations:
                equations[index].append(temp)
            else:
                equations[index] = [temp]
    pprint(equations)
    return equations


# ========================================
# Main
# ========================================
def testEquations():
    e = """
    A1 + A2 = 3
    A1 + A3 = 4
    A1 + A9 = 10
    A1 + A2 + A3 + A4 + A5 + A6 + A7 + A8 + A9 = 45
    """
    equations = createEquations(e)
    puzzle = "123456789....63....9....23..76.3...2..2..4...........1...9.7.....1.267....8....64"
    for index, equationList in equations.items():
        for equation in equationList:
            result = equation.solve(puzzle)
            assert result == 0


if __name__ == "__main__":
    filename = "./testpuzzle.txt"
    lines = []
    with open(filename, 'r') as handle:
        for line in handle:
            lines.append(line.strip())
    lines.pop(0)

    testEquations()

    e = createEquations()
    puzzle = "...2....1.12............2..........2.2...........2..........12.1....2...2..1....."
    # puzzle = "..7....8.....63....9....23..76.3...2..2..4...........1...9.7.....1.267....8....64"
    # output = "317295486284763519695418237176539842832174695459682371563947128941826753728351964"
    solve(puzzle, e)

    # calculate flag
    solution = "345267891612389457789415236431576982528931674967824315856743129173692548294158763"
    topRow = solution[:9]
    botRow = solution[-9:]
    leftCol, rightCol = "", ""
    for index in range(81):
        if index % 9 == 0 and 0 < index < 72:
            leftCol += solution[index]
        if index % 9 == 8 and 8 < index < 80:
            rightCol += solution[index]
    flag = topRow + rightCol + botRow[::-1] + leftCol[::-1]
    print(f"{topRow} {leftCol} {rightCol} {botRow}")
    print(f"flag: AOTW{{{flag}}}")
    print(f"flag len: {len(flag)}")
