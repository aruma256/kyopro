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
    N, M = mis()
    C = input().split()
    D = input().split()
    P0, *P = lmis()
    m = {d: p for d, p in zip(D, P)}
    ans = 0
    for c in C:
        if c in m:
            ans += m[c]
        else:
            ans += P0
    print(ans)



if __name__ == "__main__":
    main()
