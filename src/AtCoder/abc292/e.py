import sys
sys.setrecursionlimit(1000000000)
ii = lambda: int(input())
mis = lambda: map(int, input().split())
m0s = lambda: map(lambda x: int(x)-1, input().split())
lmis = lambda: list(mis())
lm0s = lambda: list(m0s())
INF = float('inf')
N1097 = 10**9 + 7


def main():
    N, M = mis()
    UV = [tuple(m0s()) for _ in range(M)]
    #
    w = [set() for _ in range(N)]
    for u, v in UV:
        w[u].add(v)
    #
    ans = 0
    for s in range(N):
        q = [s]
        reached = {s}
        depth = 0
        while q:
            depth += 1
            nq = []
            while q:
                p = q.pop()
                for np in w[p]:
                    if np not in reached:
                        nq.append(np)
                        reached.add(np)
                        if depth >= 2:
                            ans += 1
            q = nq
    print(ans)

main()
