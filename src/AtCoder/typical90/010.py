import itertools

N = int(input())
c1 = [0] * N
c2 = [0] * N
for i in range(N):
    c, p = map(int, input().split())
    (c1 if c==1 else c2)[i] = p

cs1 = [0] + list(itertools.accumulate(c1))
cs2 = [0] + list(itertools.accumulate(c2))

def main():
    Q = int(input())
    for _ in range(Q):
        l, r = map(int, input().split())
        l -= 1
        print(cs1[r]-cs1[l], cs2[r]-cs2[l])

main()
