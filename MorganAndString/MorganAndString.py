
def morganAndString(a, b):
    result = ""
    while True:           
        if len(a) == 1 or len(b) == 1:
            if (result + a + b) < (result + b + a):
                return result + a + b
            else:
                return result + b + a
        # Make the two strings the same length by filling the smaller string with trailing 'Z's
        # This is to count for edge cases like: a = AZZ, b = AZZA
        tempA = a + "Z" * (len(b) - len(a)) if len(a) < len(b) else a
        tempB = b + "Z" * (len(a) - len(b)) if len(b) < len(a) else b        
        if tempA <= tempB:
            c = a[0]
            while a[0] == c and len(a) > 1:                
                result += c
                a = a[1:]
        else: # b < a
            c = b[0]
            while b[0] == c and len(b) > 1:                
                result += c
                b = b[1:]
        

if __name__ == "__main__":
    fileName = "./MorganAndString7.txt"
    lines = []
    with open(fileName, 'r') as file_handle:
        for line in file_handle:        
            lines.append(line)
    n = int(lines[0])
    for i in range(n):
        a = lines[2*i+1].strip()
        b = lines[2*i+2].strip()
        result = morganAndString(a, b)
        expected = lines[len(lines) - n + i].strip()
        if result == expected:
            print("SUCCESS!")
        else:
            print("FAIL")
            print(f"a, b: {a} {b}")
            print(f"R, E: {result} {expected }")
            printLimit = 100
            j = 0
            while j < len(result) or j < len(expected):
                if not result[j] == expected[j]:
                    print(f"diff: {j} {result[j]} {expected[j]}")
                    printLimit -= 1
                    if printLimit < 0:
                        break
                j += 1
                