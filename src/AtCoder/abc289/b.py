N, M = map(int, input().split())
A = set(map(int, input().split()))

s = []
ans = []

for i in range(1, N+1):
    if i in A:
        s.append(i)
    else:
        ans.append(i)
        while s:
            ans.append(s.pop())

print(*ans)
