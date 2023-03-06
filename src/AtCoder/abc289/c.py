import itertools

def main():
    N, M = map(int, input().split())
    CS = []
    for _ in range(M):
        input()
        CS.append(set(map(int, input().split())))

    ans = 0
    for r in range(1, M+1):
        for cs in itertools.combinations(CS, r):
            s = set()
            for c in cs:
                s |= c 
            if len(s) == N:
                ans += 1
    print(ans)


main()
