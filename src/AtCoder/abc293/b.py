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
    A = lm0s()
    called = [False] * N
    for i, a in enumerate(A):
        if not called[i]:
            called[a] = True
    anslist = list(i+1 for i in range(N) if not called[i])
    print(len(anslist))
    print(*anslist)


main()
