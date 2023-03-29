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
    from collections import Counter
    S = list(map(int, input()))
    counter = Counter({0: 1})
    b = 0
    ans = 0
    for i, val in enumerate(S):
        b ^= (1<<val)
        ans += counter[b] # 組み合わせ数がどれだけ増えるか
        counter[b] += 1
    print(ans)

main()
