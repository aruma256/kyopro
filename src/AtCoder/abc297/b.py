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
    S = input()
    b1 = S.index("B")
    b2 = S.index("B", b1+1)
    r1 = S.index("R")
    r2 = S.index("R", r1+1)
    if (b1&1) != (b2&1) and S.index("K") in range(r1, r2):
        print(Yes)
    else:
        print(No)

main()
