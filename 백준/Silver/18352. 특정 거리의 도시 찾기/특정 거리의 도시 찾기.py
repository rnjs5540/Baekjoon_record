city_n, road_n, dist, start  = map(int, input().split())

dic = {}
for i in range(1, city_n + 1):
    dic[i] = []

for road in range(road_n):
    s, e = map(int, input().split())
    dic[s].append(e)

# bfs
visited = [start]
queue = [start]
for i in range(dist):
    tmpQueue = []
    while len(queue) > 0:
        popItem = queue.pop()
        for item in dic[popItem]:
            if item not in visited:
                tmpQueue.append(item)
                visited.append(item)
    queue = tmpQueue

if len(queue) == 0:
    print(-1)
for item in sorted(queue):
    print(item)