N = int(input())
w = [set() for _ in range(N)]
for _ in range(N-1):
    a, b = map(int, input().split())
    a -= 1
    b -= 1
    w[a].add(b)
    w[b].add(a)

def calc_farthest_point(start):
    depth = 0
    reached = [False] * N
    reached[start] = True
    q = {start}
    nq = set()
    far_id = None
    while True:
        while q:
            far_id = p = q.pop()
            for c in w[p]:
                if not reached[c]:
                    nq.add(c)
                    reached[c] = True
        q, nq = nq, q
        nq.clear()
        if q:
            depth += 1
            continue
        else:
            break
    return far_id, depth

def main():
    farthest, _ = calc_farthest_point(0)
    _, length = calc_farthest_point(farthest)
    print(length + 1)

main()
