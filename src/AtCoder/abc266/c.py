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


def cross(x, y):
    return x[0]*y[1] - x[1]*y[0]

def main():
    import math
    ps = [lmis() for _ in range(4)]
    for i in range(4):
        a, b, c = ps[i], ps[(i+1)%4], ps[(i+2)%4]
        vab = (b[0]-a[0], b[1]-a[1])
        vbc = (c[0]-b[0], c[1]-b[1])
        if cross(vab, vbc) < 0:
            print(No)
            return
    print(Yes)

main()
