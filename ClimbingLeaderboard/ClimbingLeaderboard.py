import timeit

# hackerrank.com/challenges/climbing-the-leaderboard

# Complete the climbingLeaderboard function below.
def climbingLeaderboard(scores, alice):
    scoreMap = {}
    rank = []
    currentRank = 1
    for score in scores:
        if not score in scoreMap:
            scoreMap[score] = currentRank
            currentRank += 1
    # print(scoreMap)
    print("CHECKPOINT 1")

    scoreKeys = list(scoreMap.keys())
    
    for aliceScore in alice:
        if aliceScore in scoreMap:
            rank.append(scoreMap[aliceScore])
        elif scores[len(scores)-1] > aliceScore:
            # if alice scored lowest
            rank.append(currentRank)
        elif scores[0] < aliceScore:
            # if alice scored highest
            rank.append(1)
        else:
            # binary search scores to find score less than alice's            
            # print(scoreKeys)
            left = 0
            right = len(scoreKeys) - 1
            m = 0
            while left <= right:
                m = (left + right) // 2
                if scoreKeys[m] < aliceScore:
                    # because scores in descending order
                    right = m - 1
                else:
                    left = m + 1            
            key = ""            
            if scoreKeys[m] < aliceScore:
                key = scoreKeys[m]
                # print(f"{scoreKeys[m]} {aliceScore}")
            else:
                key = scoreKeys[m + 1]
                # print(f"{scoreKeys[m+1]} {aliceScore}")
            rank.append(scoreMap[key])
    return rank

# main
filename = "ClimbInput.txt"
lines = []
with open(filename, 'r') as handle:
    for line in handle:
        lines.append(line)

n = int(lines[0]) # number of players
scores = [int(x) for x in lines[1].split()]
m = int(lines[2]) # number of games alice played
alice = [int(x) for x in lines[3].split()]

start = timeit.default_timer()
result = climbingLeaderboard(scores, alice)
stop = timeit.default_timer()
print(f"time: {stop - start}")
# print(result)
"""
filename = "ClimbOutput.txt"
output = []
with open(filename, 'r') as handle:
    for line in handle:
        output.append(int(line))
"""