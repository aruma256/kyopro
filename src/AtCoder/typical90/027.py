N = int(input())
s = set()

for i in range(1, N+1):
    c = input()
    if c not in s:
        s.add(c)
        print(i)
