def solve():
    N, M = map(int, input().split())
    C = list(map(int, input().split()))
    d = {i: [] for i in range(N)}
    for _ in range(M):
        u, v = map(int, input().split())
        u -= 1
        v -= 1
        d[u].append(v)
        d[v].append(u)
    #
    reached = {(0, N-1)}
    q = [(0, N-1)]
    nq = []
    gen = 0
    while q:
        gen += 1
        while q:
            ta, ao = q.pop()
            for nta in d[ta]:
                for nao in d[ao]:
                    if C[nta] == C[nao]:
                        continue
                    if (nta, nao) in reached:
                        continue
                    nq.append((nta, nao))
                    reached.add((nta, nao))
        if (N-1, 0) in reached:
            # print("ANS")
            print(gen)
            return
        q, nq = nq, q
    # print("ANS")
    print(-1)

def main():
    for _ in range(int(input())):
        solve()

main()

