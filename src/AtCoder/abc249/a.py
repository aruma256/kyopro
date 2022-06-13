A, B, C, D, E, F, X = map(int, input().split())

def action(jog, speed, rest):
    pos = 0
    while True:
        for _ in range(jog):
            pos += speed
            yield pos
        for _ in range(rest):
            yield pos

takahashi = action(A, B, C)
aoki = action(D, E, F)

for _ in range(X):
    t = next(takahashi)
    a = next(aoki)

if t > a:
    print('Takahashi')
elif t < a:
    print('Aoki')
else:
    print('Draw')
