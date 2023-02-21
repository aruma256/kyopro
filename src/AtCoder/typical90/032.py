import sys
sys.setrecursionlimit(1000000000)
ii = lambda: int(input())
mis = lambda: map(int, input().split())
m0s = lambda: map(lambda x: int(x)-1, input().split())
lmis = lambda: list(mis())
lm0s = lambda: list(m0s())
INF = float('inf')
N1097 = 10**9 + 7

import itertools

def main():
    N = ii()
    A = list(lmis() for _ in range(N))
    M = ii()
    XY = set()
    for _ in range(M):
        x, y = m0s()
        XY.add((x, y))
        XY.add((y, x))
    #
    ans = INF
    for runners in itertools.permutations(range(N)):
        if any((runners[i], runners[i+1]) in XY for i in range(N-1)):
            continue
        score = sum(A[runner][i] for i, runner in enumerate(runners))
        ans = min(ans, score)

    if ans != INF:
        print(ans)
    else:
        print(-1)

main()
