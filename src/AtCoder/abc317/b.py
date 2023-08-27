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
    A = lmis()
    mi, ma = min(A), max(A)
    A = set(A)
    for i in range(mi, ma+1):
        if i not in A:
            print(i)
            return


main()
