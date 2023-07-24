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
    import itertools
    N = ii()
    XY = [lmis() for _ in range(N)]
    max_length = 0
    for (ax, ay), (bx, by) in itertools.combinations(XY, 2):
        # 2点間の長さを求める
        length = ((ax - bx)**2 + (ay - by)**2)**0.5
        max_length = max(max_length, length)
    print(max_length)


main()
