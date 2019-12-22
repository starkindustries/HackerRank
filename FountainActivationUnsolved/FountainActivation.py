
# def fountainActivation(locations):
#     # cover all ranges from 1 to location length
#     # 1-3, 2-5, 4, 5 etc. ranges can overlap
#     rangeMap = {}
#     #rangeList = []
#     for i in range(len(locations)):
#         fountainRange = [max(i+1 - locations[i], 1), min(i+1 + locations[i], len(locations))]
#         #rangeLength = fountainRange[1] - fountainRange[0]
#         if fountainRange[0] in rangeMap:
#             rangeMap[fountainRange[0]].append(fountainRange[1])
#         else:
#             rangeMap[fountainRange[0]] = [fountainRange[1]]

#     # print(rangeMap)
#     count = 0
#     left = 1
#     while left < len(locations):
#         if left in rangeMap:
#             maxRange = max(rangeMap[left])
#             left = maxRange + 1
#             count += 1
#         else:
#             left -= 1
#     return count

# store left of range in map as key

# greedy algorithm
# iterate. assign most powerful fountain that covers the most in the range. remove fountain
# then for the remaining garden, assign fountains that cover the most range for their sub ranges.
# heapq._heapify_max(rangeList)
# gardenNeedsWater = [[1, len(locations)]]
# while len(gardenNeedsWater) > 0:
#     maxRange = heapq._heappop_max(rangeList)
#     fountRange = rangeMap[maxRange]

#     for gardenRange in gardenNeedsWater:
#         # does this range cover the needs of the garden?
#         if fountRange[0] >= gardenRange[0] and gardenRange[1] <= gardenNeedsWater[1]:
#             # yes it does! remove this range from garden

# return
# print(rangeList)
# heapq._heapify_max(rangeList)
# maxRange = heapq._heappop_max(rangeList)
# print(f"maxRange: {maxRange}")
# temp = rangeMap[maxRange]
# print(f"temp: {temp}")


def numFountains(fountains):
    print(f"fountains: {fountains}")
    n = len(fountains)
    # extents[leftIndex] = index_after_fountain_ends
    # extents stores the index AFTER the fountain ends,
    # where i is the index where the fountain starts
    extents = [0] * n
    for i in range(n):
        left = max(i - fountains[i], 0)
        right = min(i + fountains[i] + 1, n)
        extents[left] = max(extents[left], right)
        print(f"f{i}: left {left}, right {right}, extents[left] {extents[left]}")
    print(f"extents {extents}")

    # loop through the extents array
    # starting with the first index, iterate to the index
    # after the fountain ends. if we reach this value without
    # covering all fountains, increment fountain count.
    # along the way gather the max fountain value,
    # which says that a particular fountain covers the area
    # from i to extents[i]. if value of extents[i] > n then
    # you're done!
    num_fountains = 1
    right = extents[0]
    next_right = 0
    for i in range(n):
        next_right = max(next_right, extents[i])
        print(f"nextRight: {next_right}, extents[{i}]: {extents[i]}")
        if i == right:
            num_fountains += 1
            right = next_right
    print(f"num fountains: {num_fountains}")
    return num_fountains


if __name__ == "__main__":
    f1 = [91, 59, 85, 60, 57, 72, 12, 3, 27, 16, 58, 41, 94, 77, 64, 97, 20, 32, 37, 7, 2, 57, 94, 35, 70, 38, 60, 97, 100, 5, 76, 38, 8, 16, 61, 45, 77, 6, 89, 86, 31, 88, 48, 13, 93, 75, 38, 93, 25,
          80, 99, 98, 78, 30, 42, 57, 17, 96, 95, 25, 12, 94, 57, 81, 35, 5, 74, 89, 45, 18, 69, 67, 67, 11, 96, 23, 59, 97, 73, 26, 68, 77, 50, 19, 17, 79, 54, 76, 64, 69, 98, 9, 42, 48, 61, 70, 19, 49, 79, 80]
    # assert(numFountains(f1) == 1)
    assert(numFountains([1, 2, 1]) == 1)
    assert(numFountains([2, 0, 0, 0]) == 2)
    assert(numFountains([0, 0, 0, 3, 0, 0, 2, 0, 0]) == 2)
    assert(numFountains([3, 0, 2, 0, 1, 0]) == 2)
    assert(numFountains([3, 0, 1, 0, 1, 0]) == 2)
    assert(numFountains([3, 0, 1, 0, 0, 1]) == 2)
    assert(numFountains([2, 0, 2, 0, 1, 0]) == 2)
    assert(numFountains([2, 0, 0, 0, 0]) == 3)
    assert(numFountains([0, 0, 0, 0, 0]) == 5)
    assert(numFountains([1, 2, 1]) == 1)
    assert(numFountains([0, 1, 0]) == 1)
