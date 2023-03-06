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
    N = ii()
    AB = [tuple(mis()) for _ in range(N)]
    #
    omo = 1
    ura = 1
    for i in range(1, N):
        ca, cb = AB[i]
        pa, pb = AB[i-1]
        nomo, nura = 0, 0
        if ca != pa:
            nomo += omo
        if ca != pb:
            nomo += ura
        if cb != pb:
            nura += ura
        if cb != pa:
            nura += omo
        omo, ura = nomo % 998244353, nura % 998244353
    print((omo + ura) % 998244353)

main()
