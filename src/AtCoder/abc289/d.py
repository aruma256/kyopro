def main():
    N = int(input())
    A = list(map(int, input().split()))
    M = int(input())
    B = set(map(int, input().split()))
    X = int(input())
    #
    dp = [False] * 300000
    dp[0] = True
    for i in range(X+1):
        if dp[i]:
            for a in A:
                ni = i + a
                if ni not in B:
                    dp[ni] = True
    if dp[X]:
        print('Yes')
    else:
        print('No')

main()
