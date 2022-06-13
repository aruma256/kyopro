N, W = map(int, input().split())
A = list(map(int, input().split()))

import itertools

group = set()

for i in range(1, 3+1):
    for val in map(sum, itertools.combinations(A, i)):
        if val <= W:
            group.add(val)

print(len(group))
