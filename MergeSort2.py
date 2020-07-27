def mergeSort(array):
    if len(array) < 2:
        return array
    # Write your code here.
    # split into individual arrays
    arrays = list(map(lambda x: [x], array))
    print(arrays)
    i = 0
    newArrays = []
    while len(arrays) > 1:        
        if i < len(arrays) - 1:
            c = merge(arrays[i], arrays[i+1])
            print(f"c: {c}")
            newArrays.append(c)
            i += 2
        if i == len(arrays) - 1: # merge left over element
            c = merge(arrays[i], newArrays[0])
            newArrays[0] = c
            i += 1
            print(f"odd merge: {newArrays}")
        if i == len(arrays):
            i = 0
            arrays = newArrays.copy()
            newArrays = []
        print(f"i: {i}")    
        print(f"arrays: {arrays}")
        print(f"newArrays: {newArrays}")
    return arrays[0]
            
def merge(a, b):    
    aIndex, bIndex, c = 0, 0, []
    while aIndex < len(a) and bIndex < len(b):
        if a[aIndex] <= b[bIndex]:
            c.append(a[aIndex])
            aIndex += 1
        else:
            c.append(b[bIndex])
            bIndex += 1
    if aIndex < len(a):
        c.extend(a[aIndex:])
    if bIndex < len(b):
        c.extend(b[bIndex:])
    return c
            
if __name__ == "__main__":
    array = [8, 5, 2, 9, 5, 6, 3]
    result = mergeSort(array)
    print(f"Result: {result}")