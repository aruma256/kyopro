from collections import Counter

N = int(input())
A = list(map(int, input().split()))
d = Counter(A)

dp = [0] * 4
dp[0] = 1
ndp = [0] * 4

while d:
    a, n = d.popitem()
    for i in range(0, 4):
        ndp[i] = dp[i]
    for i in (0, 1, 2):
        ndp[i+1] += dp[i] * n
    dp, ndp = ndp, dp

print(dp[3])
