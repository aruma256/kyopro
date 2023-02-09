N = int(input())
S = input()
atcoder_idx = {c: idx+1 for idx, c in enumerate("atcoder")}
MOD1097 = 1000000007

def main():
    dp = [0] * 8
    dp[0] = 1
    for c in S:
        if c in atcoder_idx:
            dpn = dp.copy()
            idx = atcoder_idx[c]
            dpn[idx] = (dpn[idx] + dp[idx-1]) % MOD1097
            dp = dpn
    print(dp[-1])

main()
