import sys
sys.setrecursionlimit(1000000000)
ii = lambda: int(input())
mis = lambda: map(int, input().split())
m0s = lambda: map(lambda x: int(x)-1, input().split())
lmis = lambda: list(mis())
lm0s = lambda: list(m0s())
INF = float('inf')
N1097 = 10**9 + 7

import math

def solve():
    N, D, K = mis()
    K -= 1
    D %= N
    gcd = math.gcd(D, N)
    if gcd==1:
        return D*K % N
    cycle_len = N//gcd
    cycle_count = K//cycle_len
    K -= cycle_count*cycle_len
    return (D*K + cycle_count) % N

def main():
    ans = [solve() for _ in range(ii())]
    print(*ans, sep="\n")

main()
