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
    S = input()
    _set = set()
    for i, c in enumerate(S):
        _set.add(c)
        if len(_set) == 3:
            print(i+1)
            return


main()
