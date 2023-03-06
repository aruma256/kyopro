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
    X = lmis()
    X.sort()
    for _ in range(N):
        X.pop()
    X.reverse()
    for _ in range(N):
        X.pop()
    print(sum(X)/(3*N))

main()
