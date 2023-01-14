import sys
sys.setrecursionlimit(2**30)

def main():
    N, M = map(int, input().split())
    ps = [[] for _ in range(N)]
    for _ in range(M):
        u, v = map(int, input().split())
        u -= 1
        v -= 1
        ps[u].append(v)
        ps[v].append(u)
    #
    ans = 0
    s = set()
    def count(pos):
        nonlocal ans
        s.add(pos)
        ans += 1
        if ans >= 1000000:
            print(1000000)
            exit(0)
        for next_pos in ps[pos]:
            if next_pos not in s:
                count(next_pos)
        s.remove(pos)
    count(0)
    print(ans)

main()
