N, X = map(int, input().split())

def main():
    AB = [tuple(map(int, input().split())) for _ in range(N)]
    dp = [False] * (X+1)
    dp[0] = True
    for price, count in AB:
        dpn = dp.copy()
        for x in range(X+1):
            if dp[x] is False:
                continue
            for mul in range(1, count+1):
                nx = x + price * mul
                if nx > X:
                    break
                dpn[nx] = True
        dp = dpn
    if dp[X]:
        print('Yes')
    else:
        print('No')

main()
