from itertools import permutations

N, M = map(int, input().split())
arr = list(map(int, input().split()))

for permu in sorted(set(permutations(arr, M))):
    for p in permu:
        print(p, end=' ')
    print()
