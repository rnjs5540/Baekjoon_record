n = int(input())
li = list(map(int, input().split()))
li.sort()

ans1 = 1000000000
ans2 = 1000000000

baseIndex = 0
for base in li:
    closestSum = 2000000002
    closestPartner = 0

    s = baseIndex + 1
    e = n - 1
    # base와 더했을때 가장 0에 가까운 수(closestPartner)
    while s <= e:
        mid = int((s+e) / 2)
        sumVal = base + li[mid]

        if abs(sumVal) < abs(closestSum):
            closestSum = sumVal
            closestPartner = li[mid]

        if sumVal == 0:
            break
        if sumVal > 0:
            e = mid - 1
        else:
            s = mid + 1

    if abs(ans1 + ans2) > abs(closestSum):
        ans1 = base
        ans2 = closestPartner

    baseIndex += 1

print(ans1, ans2)


'''
시간초과면 이해하겠는데
틀린건 어디서 틀렸는지 모르겠네..
내일 마저해야지
'''