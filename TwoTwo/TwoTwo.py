import math 

# https://www.hackerrank.com/challenges/two-two/problem
def strength(subString):
    if int(subString[0]) == 0:
        return 0
    return int(subString)

def isPowerOfTwo(n):    
    return math.log2(n).is_integer()    

def twotwo(a):
    twoCount = 0
    groupMap = {}
    # loop through all groups of i-j or build a groups
    # loop through all possible group lengths from 1 to len(a)
    for i in range(1, len(a) + 1):
        # loop through all groups of length i
        for j in range(0, len(a) - i + 1):
            # this is a group
            group = a[j:j + i]
            groupMap[group] = groupMap.get(group, 0) + 1
            # print(f"{j} {j + i} {group}")    
    print("DONE")
    return 5
    # for each group, find the group's strength
    for group, count in groupMap.items():
        # determine if strength is a power of 2
        if isPowerOfTwo(strength(group)):
            # if is power of 2, increment count
            twoCount += count
    return twoCount
    
# main
"""
testCases = [
    ("2222222", 7),    
    ("24256", 4),
    ("65536", 1),
    ("023223", 4),
    ("33579", 0),
]
"""

testCases = []
filename = "./TwoTwo1.txt"
lines = []
with open(filename, 'r') as fileHandle:
    for line in fileHandle:
        lines.append(line)
n = int(lines.pop(0))
for i in range(n):
    testCases.append((lines[i], int(lines[n + i + 1])))

for t in testCases:
    result = twotwo(t[0])
    print(f"result: {result}")


# up to len 10^5 = 100,000
"""
x = 332193
powersOfTwo = [2]
for i in range(1, x + 1):
    temp = powersOfTwo[i - 1]
    powersOfTwo.append(2 * temp)
    isPow2 = isPowerOfTwo(temp)
    print(f"{i} {str(temp)[:50]}.. {isPow2}")
print(f"{powersOfTwo}")
"""