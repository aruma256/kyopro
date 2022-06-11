import itertools

N, K = map(int, input().split())
A = list(map(int, input().split()))

P = [sorted(A[i::K]) for i in range(K)]

t = list(itertools.chain(*zip(*P)))
print('Yes' if t == sorted(t) else 'No')
