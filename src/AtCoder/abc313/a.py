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
    N = ii()
    P = lmis()
    if P[0] == max(P) and P.count(max(P)) == 1:
        print(0)
    else:
        print(max(P) - P[0] + 1)


main()
