import math 

TESTNUMBER = 1

powersTwoMap = { 1 : 0 }
def buildPowersMap():
    # build powersTwoMap
    x = 800
    temp = 1
    for i in range(1, x + 1):
        temp *= 2    
        powersTwoMap[temp] = i
        # print(f"{str(temp)[:50]} {i} {len(str(temp))}")

# https://www.hackerrank.com/challenges/two-two/problem
def strength(subString):
    if int(subString[0]) == 0:
        return 0
    return int(subString)

def isPowerOfTwo(n):    
    return (n in powersTwoMap)

# Output the total number of strengths of the form 2^x such that 0 <= x <= 800.
maxLen = 241
def twotwo(a):
    twoCount = 0
    for value in powersTwoMap.keys():
        if str(value) in a:
            twoCount += a.count(str(value))
    return twoCount
    
# main
testCases = []

if TESTNUMBER == 0:
    testCases = [
        ("2222222", 7),    
        ("24256", 4),
        ("65536", 1),
        ("023223", 4),
        ("33579", 0),
        ("2121212121212121", 8)
    ]

if TESTNUMBER > 0:
    testCases = []
    filename = "./TwoTwo1.txt"
    if TESTNUMBER == 2:
        filename = "./TwoTwo2.txt"
    lines = []
    with open(filename, 'r') as fileHandle:
        for line in fileHandle:
            lines.append(line.strip())    
    n = int(lines.pop(0))
    for i in range(n):
        testCases.append((lines[i], int(lines[n + i + 1])))

buildPowersMap()
for t in testCases:
    result = twotwo(t[0])
    if result == t[1]:
        print(f"SUCCESS: {result}")
    else: 
        print(f"FAIL: {result}. Expected {t[1]}")
