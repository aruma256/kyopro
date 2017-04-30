def combination(n, r):
    r = min(r, n - r)
    c = 1
    for i in range(1, r + 1):
        c *= n - r + i
        c //= i
    return c

