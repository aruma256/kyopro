N, P, Q, R, S = map(int, input().split())
A = list(map(int, input().split()))

P -= 1
Q -= 1
R -= 1
S -= 1

for d in range(0, Q-P+1):
    A[P+d], A[R+d] = A[R+d], A[P+d]

print(*A)
