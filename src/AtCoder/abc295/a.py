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
    W = set(input().split())
    a = {"and", "not", "that", "the", "you"}
    print("Yes" if W&a else "No")


main()
