goal = input()
brokenCount = int(input())

BrokenArr = []
if brokenCount > 0:
    brokenNums = input()
    for brokenNum in brokenNums.split():
        BrokenArr.append(brokenNum)

minDiff = abs(int(goal) - 100)
for num in range(1000001):
    num = str(num)
    isPossible = True
    for digit in num:
        if digit in BrokenArr:
            isPossible = False
            break
    if isPossible:
        diff = abs(int(goal) - int(num)) + len(num)
        minDiff = min(minDiff, diff)

print(minDiff)
