from itertools import combinations
n = int(input())
arr = [[0 for col in range(n)] for row in range(n)]
total = 0
arr = [list(map(int, input().split())) for _ in range(n)]

def notInComb(x):
    return x not in comb


minDiff = 9999
combs = list(combinations(range(n), int(n/2)))
for comb in combs:
    sum = 0
    for i in comb:
        for j in comb:
            sum += arr[i][j]

    notComb = list(filter(notInComb, range(n)))
    sum2 = 0
    for i in notComb:
        for j in notComb:
            sum2 += arr[i][j]

    if abs(sum - sum2) < minDiff:
        minDiff = abs(sum - sum2)

print(minDiff)




# 전체 합의 반에 가까운거 고르면 됨