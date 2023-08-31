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
    XYZ = [lmis() for _ in range(N)]
    dp = [INF] * (10**5 + 1)
    dp[0] = 0
    for x, y, z in XYZ:
        dpn = dp.copy()
        if x > y:
            for score in range(10**5 + 1):
                if dp[score] != INF:
                    dpn[score + z] = min(dpn[score + z], dp[score])
        else:
            min_required_score = (x + y)//2 + 1
            cost = min_required_score - x
            for score in range(10**5 + 1):
                if dp[score] != INF:
                    dpn[score + z] = min(dpn[score + z], dp[score] + cost)
        dp = dpn
    z_sum = sum(z for _, _, z in XYZ)
    z_required = z_sum//2 + 1
    print(min(dp[z_required:]))


main()
