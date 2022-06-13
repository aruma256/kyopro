from itertools import count

N = int(input())
A = set(map(int, input().split()))
for i in count():
    if i not in A:
        print(i)
        break
