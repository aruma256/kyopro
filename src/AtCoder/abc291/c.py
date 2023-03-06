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
    N = ii()
    S = input()
    reached = {(0, 0)}
    cx = 0
    cy = 0
    for c in S:
        if c=='R':
            cx += 1
        elif c=='L':
            cx -= 1
        elif c=='U':
            cy += 1
        else:
            cy -= 1
        newpos = (cx, cy)
        if newpos in reached:
            print('Yes')
            return
        else:
            reached.add(newpos)
    print('No')

main()
