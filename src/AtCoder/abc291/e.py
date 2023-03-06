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
    XY = [tuple(m0s()) for _ in range(M)]
    #
    if M+1 < N:
        print('No')
        return
    #
    w = [set() for _ in range(N)]
    rev_w = [set() for _ in range(N)]
    for x, y in XY:
        w[x].add(y)
        rev_w[y].add(x)
    #
    start = None
    for i in range(N):
        if w[i] and not rev_w[i]:
            if start is None:
                start = i
            else:
                print('No')
                return
    #
    end = None
    for i in range(N):
        if not w[i] and rev_w[i]:
            if end is None:
                end = i
            else:
                print('No')
                return
    #
    depthList = [INF] * N

    def dfsDepthMax(p):
        if depthList[p] != INF:
            return depthList[p]
        if p==end:
            depthList[p] = 0
        else:
            depthList[p] = max(dfsDepthMax(np) for np in w[p]) + 1
        return depthList[p]

    dfsDepthMax(start)
    print('Yes')
    print(*(N-val for val in depthList))

main()
