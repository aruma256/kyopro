N, K = map(int, input().split())

SS = [input() for _ in range(N)]
SS = SS[:K]
SS.sort()
for s in SS:
    print(s)
