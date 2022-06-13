import itertools

X, A, D, N = map(int, input().split())
E = A + D * (N-1)

if A > E:
    A, E, = E, A
    D *= -1

if D and A <= X <= E:
    r = range(A, E+D, D)
    for i in itertools.count():
        if X+i in r or X-i in r:
            print(i)
            break
else:
    print(min(abs(A-X), abs(E-X)))
