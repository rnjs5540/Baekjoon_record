import sys

def find(a: int) -> int:
    if parent[a] < 0:   # 루트
        return a

    tmp = a
    while parent[tmp] >= 0:
        tmp = parent[tmp]
    ancestor_a = tmp

    tmp = a
    while parent[a] >= 0:
        tmp = parent[a]
        parent[a] = ancestor_a
        a = tmp

    return ancestor_a

def union(ancestor_a: int, ancestor_b: int):
    if parent[ancestor_a] > parent[ancestor_b]:
        parent[ancestor_a] = ancestor_b
    else:
        parent[ancestor_b] = ancestor_a
    if parent[ancestor_a] == parent[ancestor_b]:
        parent[ancestor_a] -= 1


n, m = map(int, sys.stdin.readline().split())
parent = [-1 for _ in range(n)] # 음수는 루트의 노드레벨

ans = 0
for turn in range(1, m+1):
    s, e = map(int, sys.stdin.readline().split())
    ancestor_s = find(s)
    ancestor_e = find(e)
    if ancestor_s == ancestor_e:
        ans = turn
        break
    union(ancestor_s, ancestor_e)

print(ans)