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


# A [cm]
# B [cm/s]
# A/B [s]


def meg(f, ok, ng):
    while abs(ok-ng)>1:
        mid = (ok+ng)//2
        if f(mid):
            ok=mid
        else:
            ng=mid
    return ok


def main():
    N = ii()
    AB = []
    total_length = 0
    total_seconds = 0
    for _ in range(N):
        a, b = mis()
        AB.append((a, b, a/b))
        total_length += a
        total_seconds += a/b
    #
    target_seconds = total_seconds / 2
    current_pos = total_length
    now = 0
    while now + AB[-1][-1] < target_seconds:
        a, b, s = AB.pop()
        now += s
        current_pos -= a
    #
    a, b, s = AB.pop()
    current_pos -= (target_seconds - now) * b
    print(current_pos)

main()
