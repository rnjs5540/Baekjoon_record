import sys
#sys.setrecursionlimit(10**6)

def find_ancestor(a):
    if parent[a] > -1:
        ancestor_a = find_ancestor(parent[a])
        parent[a] = ancestor_a
        return ancestor_a
    return a

n, m = map(int, sys.stdin.readline().split())
parent = [-1 for _ in range(n+1)]
node_level = [1 for _ in range(n+1)]
for i in range(m):
    opt, a, b = map(int, sys.stdin.readline().split())
    ancestor_a = find_ancestor(a)
    ancestor_b = find_ancestor(b)
    if opt == 0:
        if ancestor_a == ancestor_b:
            continue
        
        if node_level[ancestor_a] < node_level[ancestor_b]:
            parent[ancestor_a] = ancestor_b
        else:
            parent[ancestor_b] = ancestor_a
            
            if node_level[ancestor_a] == node_level[ancestor_b]:
                node_level[ancestor_a] += 1
    else:
        if ancestor_a == ancestor_b:
            print('YES')
        else:
            print('NO')
