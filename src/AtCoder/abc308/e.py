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


class CumSum():
    def __init__(self, A):
        self.S = [0] * (len(A) + 1)
        for i, a in enumerate(A):
            self.S[i+1] = self.S[i] + a

    def sum(self, l, r):
        return self.S[r] - self.S[l]


def main():
    N = ii()
    A = lmis()
    S = input()
    cs = {
        "M": [CumSum([a==n and c=="M" for a, c in zip(A, S)]) for n in range(3)],
        "E": [CumSum([a==n and c=="E" for a, c in zip(A, S)]) for n in range(3)],
        "X": [CumSum([a==n and c=="X" for a, c in zip(A, S)]) for n in range(3)],
    }
    import itertools

    def calc_mex(m, e, x):
        for i in itertools.count():
            if i not in (m, e, x):
                return i

    ans = 0
    for i in range(1, N-1):
        if S[i] != "E":
            continue
        e = A[i]
        for m, x in itertools.product(range(3), repeat=2):
            ans += calc_mex(m, e, x) * cs["M"][m].sum(0, i) * cs["X"][x].sum(i+1, N)

    print(ans)


main()
