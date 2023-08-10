n = int(input())
li = list(map(int, input().split()))
x = int(input())
count = 0

while li:
    tmp = li.pop(0)
    if x-tmp in li:
        count += 1

print(count)