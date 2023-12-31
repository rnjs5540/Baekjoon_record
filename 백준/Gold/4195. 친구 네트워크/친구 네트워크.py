import sys

def find(name: str) -> str:
    if isinstance(parent[name], int):
        return name
    parent[name] = find(parent[name])
    return parent[name]

def union(name1:str, name2:str):
    ancestor1 = find(name1)
    ancestor2 = find(name2)

    if ancestor1 == ancestor2:
        return
    
    node_level1 = parent[ancestor1]
    node_level2 = parent[ancestor2]
    if node_level1 < node_level2:
        parent[ancestor1] = ancestor2
    else:
        parent[ancestor2] = ancestor1
    if node_level1 == node_level2:
        parent[ancestor1] += 1
    
    relation_num[ancestor1] += relation_num[ancestor2]
    relation_num[ancestor2] = relation_num[ancestor1]


test_case = int(sys.stdin.readline())
for i in range(test_case):
    parent = {}  # name : parent
    relation_num = {} # name : relation_num
    
    n = int(sys.stdin.readline())
    for i in range(n):
        name1, name2 = sys.stdin.readline().split()

        if name1 not in parent:
            parent[name1] = 1
            relation_num[name1] = 1
        if name2 not in parent:
            parent[name2] = 1
            relation_num[name2] = 1

        union(name1, name2)

        print(relation_num[find(name1)])
