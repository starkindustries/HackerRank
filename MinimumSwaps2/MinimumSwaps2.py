# https://www.hackerrank.com/challenges/minimum-swaps-2/problem

def minimumSwaps(arr):
    i, count = 0, 0
    print(arr)
    while i < len(arr):
        if not arr[i] == i + 1:            
            swapIndex = arr[i] - 1
            arr[i], arr[swapIndex] = arr[swapIndex], arr[i]                        
            count += 1
            i -= 1
            print(arr)
        i += 1
    return count

# inputString = "2 31 1 38 29 5 44 6 12 18 39 9 48 49 13 11 7 27 14 33 50 21 46 23 15 26 8 47 40 3 32 22 34 42 16 41 24 10 4 28 36 30 37 35 20 17 45 43 25 19"
# n = [int(x) for x in inputString.split()]
n = [7, 1, 3, 2, 4, 5, 6]
temp = minimumSwaps(n)
print(temp)