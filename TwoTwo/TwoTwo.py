import math 

TESTCASE1 = True

powersTwoMap = {}
lastTwoDigits = {}
lastThreeDigits = {}
lastFourDigits = {}
def buildPowersMap():
    # build powersTwoMap
    x = 800
    temp = 1
    for i in range(1, x + 1):
        temp *= 2    
        powersTwoMap[temp] = i
        # print(f"{str(temp)[:50]} {i} {len(str(temp))}")

    # build maps
    for value, _ in powersTwoMap.items():
        # print(f"{str(value)[-2:]} {power}")        
        lastTwoDigits[value % 100] = True
        lastThreeDigits[value % 1000] = True
        lastFourDigits[value % 10000] = True
    # print(lastFourDigits)    

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
    for i in range(len(a) - 1, -1, -1):
        if int(a[i]) % 2 != 0 or int(a[i]) == 0:
            continue        
        maxGroupLength = i + 2 if (i + 2) < 241 else 241      
        for groupLength in range(1, maxGroupLength):
            if groupLength > 1 and int(a[i - 1: i + 1]) not in lastTwoDigits:
                break
            if groupLength > 2 and int(a[i - 2: i + 1]) not in lastThreeDigits:
                break
            if groupLength > 3 and int(a[i - 3: i + 1]) not in lastFourDigits:
                break
            group = a[i - groupLength + 1: i + 1]
            # print(f"group: ..{group[-50:]} {groupLength} {i}")
            if isPowerOfTwo(strength(group)):                
                twoCount += 1
    return twoCount
    
# main
testCases = []

if TESTCASE1:
    testCases = [
        ("2222222", 7),    
        ("24256", 4),
        ("65536", 1),
        ("023223", 4),
        ("33579", 0),
        ("2121212121212121", 8)
    ]

if not TESTCASE1:
    testCases = []
    filename = "./TwoTwo1.txt"
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
    print(f"result: {result}")
