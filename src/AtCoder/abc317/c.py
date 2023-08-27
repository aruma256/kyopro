import sys
sys.setrecursionlimit(1000000000)
ii = lambda: int(input())
mis = lambda: map(int, input().split())
m0s = lambda: map(lambda x: int(x)-1, input().split())
lmis = lambda: list(mis())
lm0s = lambda: list(m0s())
INF = float('inf')
N1097 = 10**9 + 7
Yes = 'Yes'
No = 'No'


import itertools
def main():
    N, M = mis()
    w = [[None] * N for _ in range(N)]
    for _ in range(M):
        a, b, c = mis()
        a -= 1
        b -= 1
        w[a][b] = c
        w[b][a] = c
    #
    max_dist = 0
    for perm in itertools.permutations(range(N)):
        dist = 0
        for _from, _to in itertools.pairwise(perm):
            if w[_from][_to] is None:
                break
            dist += w[_from][_to]
        max_dist = max(max_dist, dist)
    print(max_dist)


main()
