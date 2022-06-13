N = int(input())

best_i = -1
best_score = -1
al = set()

for i in range(N):
    p, score = input().split()
    score = int(score)
    if p not in al:
        if score > best_score:
            best_score = score
            best_i = i
    al.add(p)

print(best_i + 1)
