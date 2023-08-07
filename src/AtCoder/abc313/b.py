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


def main():
    N, M = mis()
    d = [[] for _ in range(N)]
    for _ in range(M):
        a, b = m0s()
        d[b].append(a)
    #
    empty_count = 0
    ans = None
    for i in range(N):
        if len(d[i]) == 0:
            empty_count += 1
            ans = i
    #
    if empty_count > 1:
        print(-1)
    else:
        print(ans + 1)


main()
