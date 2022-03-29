N, M = map(int, input().split())
A = list(map(int, input().split()))
C = list(map(int, input().split()))

A.reverse()
C.reverse()
ans = []

while len(C) >= len(A):
    quotient = C[0] // A[0]
    ans.append(quotient)
    for idx, a in enumerate(A):
        C[idx] -= a * quotient
    C.pop(0)

print(*reversed(ans))
