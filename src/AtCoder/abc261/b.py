import itertools

N = int(input())
A = [input() for _ in range(N)]

for i, j in itertools.combinations(range(N), 2):
    results = {A[i][j], A[j][i]}
    if results == {'D'}:
        continue
    elif results == {'W', 'L'}:
        continue
    else:
        print('incorrect')
        exit()

print('correct')
