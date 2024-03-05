goal = input()
brokenCount = int(input())
BrokenArr = [] if brokenCount == 0 else list(input().split())

minDiff = abs(int(goal) - 100)
for num in range(1000001):
    num = str(num)
    isPossible = True
    for digit in num:
        if digit in BrokenArr:
            isPossible = False
            break
    if not isPossible: 
        continue
    diff = abs(int(goal) - int(num)) + len(num)
    minDiff = min(minDiff, diff)        

print(minDiff)
