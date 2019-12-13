# Merge Sort
def merge(a, b):
    aIndex, bIndex = 0, 0
    merged = []
    while aIndex < len(a) and bIndex < len(b):
        if a[aIndex] <= b[bIndex]:
            merged.append(a[aIndex])
            aIndex += 1
        else:
            merged.append(b[bIndex])
            bIndex += 1
    merged.extend(a[aIndex:])
    merged.extend(b[bIndex:])
    return merged


def mergeSort(arr):
    n = len(arr)
    if n == 1:
        return arr
    a = mergeSort(arr[:n//2])
    b = mergeSort(arr[n//2:])
    return merge(a, b)


if __name__ == "__main__":
    myArray = [2, 3, 1, 9, 100, 4, 5, 3, 3, 99, 50, 49, 41]
    newArray = mergeSort(myArray)
    print(f"unsorted: {myArray}")
    print(f"sorted: {newArray}")

    # Test with input file
    filename = "./MergeSort_input.txt"
    lines = []
    with open(filename, 'r') as handle:
        for line in handle:
            lines.append(line)
    t = int(lines.pop(0))
    for i in range(t):
        n = lines[2*i]
        array = [int(x) for x in lines[2*i+1].split()]
        mergeSort(array)
