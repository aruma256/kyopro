import sys
sys.setrecursionlimit(1000000000)
ii = lambda: int(input())
mis = lambda: map(int, input().split())
m0s = lambda: map(lambda x: int(x)-1, input().split())
lmis = lambda: list(mis())
lm0s = lambda: list(m0s())
INF = float('inf')
N1097 = 10**9 + 7

A, X, M = mis()

def simple(A, X, M):
    return sum(A**i for i in range(X)) % M

def solve(A, X, M):
    if A==1:
        return X % M
    r = A
    # (r^x - 1)/(r - 1) % M
    # ( (r^x - 1)%(M*(r-1)) / (r-1) ) % M
    return (pow(r, X, M*(A-1))-1) // (r-1) % M

def main():
    if M==1:
        print(0)
        return
    # print(simple(A, X, M))
    print(solve(A, X, M))



main()
