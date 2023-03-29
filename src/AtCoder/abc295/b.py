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
    import itertools
    R, C = mis()
    B = [input() for _ in range(R)]
    ans = [list(line) for line in B]
    for r, line in enumerate(B):
        for c, val in enumerate(line):
            if val == ".":
                pass
            elif val == "#":
                pass
            else:
                p = int(val)
                for ri in range(R):
                    for ci in range(C):
                        if abs(ri - r) + abs(ci - c) <= p:
                            ans[ri][ci] = "."
    for line in ans:
        print("".join(line))

main()
