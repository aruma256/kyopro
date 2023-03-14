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
    H, W = mis()
    A = [lmis() for _ in range(H)]
    def dfs(pos: tuple, s: set):
        if pos == (H-1, W-1):
            return 1
        h, w = pos
        ret = 0
        if h < H-1:
            na = A[h+1][w]
            if na not in s:
                s.add(na)
                ret += dfs((h+1, w), s)
                s.remove(na)
        if w < W-1:
            na = A[h][w+1]
            if na not in s:
                s.add(na)
                ret += dfs((h, w+1), s)
                s.remove(na)
        return ret
    print(dfs((0, 0), {A[0][0]}))

main()
