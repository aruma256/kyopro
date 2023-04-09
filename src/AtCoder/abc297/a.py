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
    N, D = mis()
    T = lmis()
    for i in range(N-1):
        if T[i+1]-T[i] <= D:
            print(T[i+1])
            return
    print(-1)

main()
