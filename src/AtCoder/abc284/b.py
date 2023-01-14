T = int(input())
for _ in range(T):
    N = int(input())
    A = list(map(int, input().split()))
    print(sum(a&1 for a in A))
