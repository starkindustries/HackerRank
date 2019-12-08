def threeNumberSum(array, targetSum):
    # Write your code here.
    output = []
    # this map will detect duplicates
    outputMap = {}
    # create map of the integers
    # NOTE: integers are **distinct**
    arrayMap = {}
    for n in array:
        arrayMap[n] = True
    print(arrayMap)

    # loop through array
    for i in range(len(array) - 1):
        a = array[i]
        # loop through remaining array
        for j in range(i + 1, len(array)):
            b = array[j]
            # check if (target - a - b) exists
            c = targetSum - a - b
            print(f"{a} {b} {c}")
            if c in arrayMap and c != a and c != b:
                threeNums = sorted([a, b, c])
                threeNumString = f"{threeNums[0]}-{threeNums[1]}-{threeNums[2]}"
                if threeNumString not in outputMap:
                    output.append(threeNums)
                    outputMap[threeNumString] = True
    output.sort()
    return output


# main
# result = threeNumberSum([1, 2, 3, 4, 5, 6, 7, 8, 9, 15], 33)
result = threeNumberSum([12, 3, 1, 2, -6, 5, -8, 6], 0)
print(result)
