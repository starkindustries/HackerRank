
"""
# Recursive approach. It works but returns runtime error:
# maximum recursion depth exceeded
def morganAndString(a, b):        
    if a <= b:
        if len(a) == 1:
            return a[0] + b
        else:
            return a[0] + morganAndString(a[1:], b)
    elif b < a:
        if len(b) == 1:
            return b[0] + a
        else:
            return b[0] + morganAndString(a, b[1:])    
"""

def morganAndString(a, b):
    result = ""
    while True:        
        """
        if a[0] == "Z" or b[0] == "Z":
            print("Z!")
            print(f"a: {a[:30]}..")
            print(f"b: {b[:30]}..")            
        """
        if a <= b:
            if len(a) == 1:
                return result + a + b
            result += a[0]
            a = a[1:]
        else: # b < a
            if len(b) == 1:
                return result + b + a
            result += b[0]
            b = b[1:]
        

if __name__ == "__main__":
    fileName = "./MorganAndString4.txt"
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
            # print(f"R, E: {result} {expected }")
            printLimit = 100
            j = 0
            while j < len(result) or j < len(expected):
                if not result[j] == expected[j]:
                    print(f"diff: {j-1} {result[j-1]} {expected[j-1]}")
                    printLimit -= 1
                    if printLimit < 0:
                        break
                j += 1
                