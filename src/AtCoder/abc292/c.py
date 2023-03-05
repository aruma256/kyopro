import sys
sys.setrecursionlimit(1000000000)
ii = lambda: int(input())
mis = lambda: map(int, input().split())
m0s = lambda: map(lambda x: int(x)-1, input().split())
lmis = lambda: list(mis())
lm0s = lambda: list(m0s())
INF = float('inf')
N1097 = 10**9 + 7


def solve(N: int):
    c = [0] * (N+1)
    ans = 0
    for x in range(1, N):
        ab_patterns = 0
        for a in range(1, int(x**0.5) + 1):
            if x%a == 0:
                b = x // a
                ab_patterns += 1
                if a != b:
                    ab_patterns += 1
        y = N - x
        cd_patterns = 0
        for c in range(1, int(y**0.5) + 1):
            if y%c == 0:
                d = y // c
                cd_patterns += 1
                if c != d:
                    cd_patterns += 1
        ans += ab_patterns * cd_patterns
    print(ans)

def main():
    solve(ii())

main()
