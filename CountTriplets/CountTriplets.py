# Count Triplets
# https://www.hackerrank.com/challenges/count-triplets-1/problem


def countTriplets(arr, r):
    # [1, 1, 1, 27, 3, 3, 9, 3, 27, 9, 1, 3, 27], r = 3
    # loop through each value in arr
    # assume value is b, calculate a and c. e.g. b = 3, a = 1, c = 9
    # if a is in pastMap (value already seen), add 'c' to futureMap with 'a's current value
    #   if futureMap[c] already exists, add 'a's current value to futureMap[c]
    #   we increment futureMap[c] because this represents how many times 'a' has occured in the past
    # pastMap: {1: 3}. futureMap: {9: [3]}
    # check if current value b is in the futureMap.
    #   if it is, increment count by futureMap[b] * pastMap[b // r]
    # Add b to pastMap
    futureMap = {}
    pastMap = {}
    count = 0
    for b in arr:
        a = b // r
        c = b * r
        # check futureMap before updating it
        if b in futureMap:
            count += futureMap[b]
        # update futureMap
        if b % r == 0 and a in pastMap:
            futureMap[c] = futureMap.get(c, 0) + pastMap[a]
        pastMap[b] = pastMap.get(b, 0) + 1
    return count


# main
# Read a file
fileName = "./CountTripletsTest.txt"
lines = []
with open(fileName, 'r') as file_handle:
    for line in file_handle:
        lines.append(line)
r = int((lines[0].split())[1])
arr = [int(x) for x in lines[1].split()]
result = countTriplets(arr, r)
expected = int(lines[2])
if result == expected:
    print(f"SUCCESS: {result}")
else:
    print(f"TEST FAILED: {result}, expected: {expected}")
