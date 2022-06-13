from collections import deque
from itertools import count

N = int(input())
SS = [list(map(int, input())) for _ in range(N)]

ans = 10**10

for n in range(10):
    d = deque(SS)
    for i in count():
        for _ in range(len(d)):
            f = d.popleft()
            if f[i%10] == n:
                break
            d.append(f)
        if not d:
            break
    ans = min(ans, i)

print(ans)
