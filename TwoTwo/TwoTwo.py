import timeit
import json

DEBUG = False
TESTNUMBER = 1

class Trie:
    root = {} # character : node

    def __repr__(self):
        return f"{(self.root)}"

    def __str__(self):
        return f"{(self.root)}"

    def add(self, word):    
        current = self.root
        for char in word:
            if char not in current:
                current[char] = {}
            current = current[char]
        current["*"] = True

    def search(self, word):
        current = self.root
        for char in word:
            if char not in current:
                return False
            current = current[char]
        if '*' in current:
            return True
        else:
            return False

powersTrie = Trie()
def buildPowersMap():
    # build powersTwoMap
    x = 800
    temp = 1
    powersTrie.add(str(temp))
    for i in range(1, x + 1):
        temp *= 2
        powersTrie.add(str(temp))
        if DEBUG:
            print(f"{str(temp)[:50]}.. {i} {len(str(temp))}")
    # print(json.dumps(powersTrie.root, sort_keys=True, indent=1))

# https://www.hackerrank.com/challenges/two-two/problem
# Output the total number of strengths of the form 2^x such that 0 <= x <= 800.
def twotwo(a):
    count = 0    
    for i in range(len(a)):
        current = powersTrie.root
        substring = a[i:]               
        for char in substring:            
            # if DEBUG:
            #     print(f"{char} {substring}")
            if not char in current:
                break
            current = current[char]
            if "*" in current:
                count += 1           
    return count
    
# main
testCases = []

if TESTNUMBER == 0:
    testCases = [
        ("2222222", 7),    
        ("24256", 4),
        ("65536", 1),
        ("023223", 4),
        ("33579", 0),
        ("2121212121212121024", 19)
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
totalTime = 0
for t in testCases:
    start = timeit.default_timer()
    result = twotwo(t[0])
    stop = timeit.default_timer()
    if result == t[1]:
        print(f"SUCCESS: {result}")
    else: 
        print(f"FAIL: {result}. Expected {t[1]}")
    totalTime += stop - start
print(f"avg time: {totalTime / len(testCases)}")
print(f"total time: {totalTime}")
