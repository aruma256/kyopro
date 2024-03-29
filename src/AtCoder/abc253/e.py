import sys

import numpy as np
from numba import njit

@njit(cache=True)
def solve(N, M, K):
    dp = np.ones(M, dtype=np.int64)
    ndp = np.empty_like(dp)

    for _ in range(N-1):
        cs = dp.cumsum()
        for i in range(M):
            ndp[i] = (cs[-1] - cs[min(i+K-1, M-1)] + (cs[i-K] if i-K>=0 else 0)) % 998244353
        dp, ndp = ndp, dp

    ans = 0
    for val in dp:
        ans += val
        ans %= 998244353

    return ans

def main():
    N, M, K = map(int, input().split())
    if K == 0:
        print(pow(M, N, 998244353))
    else:
        print(solve(N, M, K))

if sys.argv[-1] == 'ONLINE_JUDGE':
    solve(100, 1000, 500)
else:
    main()
