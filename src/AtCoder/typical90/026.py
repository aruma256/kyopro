def bfs_with_2_colors(w, initialPos=0):
    group0 = {initialPos}
    group1 = set()
    def reached(pos_id):
        return next_pos in group0 or next_pos in group1
    q = [initialPos]
    depth = 0
    while q:
        depth += 1
        next_q = []
        while q:
            pos = q.pop()
            for next_pos in w[pos]:
                if not reached(next_pos):
                    next_q.append(next_pos)
                    (group1 if depth&1 else group0).add(next_pos)
        q = next_q
    return depth, group0, group1

def main():
    N = int(input())
    w = [[] for _ in range(N)]
    for _ in range(N-1):
        a, b = map(int, input().split())
        a -= 1
        b -= 1
        w[a].append(b)
        w[b].append(a)
    #
    _, g0, g1 = bfs_with_2_colors(w)
    g = g0 if len(g0) >= len(g1) else g1
    while len(g) > N//2:
        g.pop()
    print(*(i+1 for i in g))

main()
