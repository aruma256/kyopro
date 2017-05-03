def combination(n, r):
    r = min(r, n - r)
    c = 1
    for i in range(1, r + 1):
        c *= n - r + i
        c //= i
    return c


def factorial_mod(x, m):
    a = 1
    for i in range(2, x + 1):
        a *= i
        a %= m
    return a


class UnionFind():
    def __init__(self, N):
        self.N = N
        self.root = list(range(N))
    def get_root(self, a):
        r = self.root[a]
        if r != a:
            r = self.get_root(r)
            self.root[a] = r
        return r
    def connect(self, a, b):
        if a == b:
            raise RuntimeError(a, b)
        self.root[self.get_root(a)] = self.get_root(b)
    def count_union(self):
        t = 0
        for i in range(self.N):
            if i == self.get_root(i):
                t += 1
        return t

