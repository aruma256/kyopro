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

