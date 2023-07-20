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
    products = []
    for _ in range(N):
        p, _, *f = lmis()
        products.append((p, set(f)))
    import itertools
    for a, b in itertools.permutations(products, 2):
        if a[0] >= b[0]:
            if b[1] >= a[1]:
                if a[0] > b[0] or b[1] - a[1]:
                    print(Yes)
                    return
    print(No)


main()
