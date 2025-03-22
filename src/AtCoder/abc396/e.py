from collections import deque
import itertools

def main():
    N, M = map(int, input().split())
    XYZ = []
    max_z = 0
    for _ in range(M):
        x, y, z = map(int, input().split())
        XYZ.append((x - 1, y - 1, z))
        max_z = max(max_z, z)

    w = [[] for _ in range(N)]
    for x, y, z in XYZ:
        w[x].append((y, z))
        w[y].append((x, z))

    ans = [0] * N
    b = 1
    while b <= max_z:
        vals = [None] * N
        for a_i in range(N):
            if vals[a_i] is not None:
                continue

            # bfs
            zeros = set()
            non_zeros = set()
            q = deque()
            q.append(a_i)
            vals[a_i] = 0
            zeros.add(a_i)
            while q:
                i = q.popleft()
                for to, z in w[i]:
                    s = bool(z & b)
                    if vals[to] is not None:
                        if vals[i] ^ s != vals[to]:
                            print(-1)
                            return
                        continue
                    vals[to] = vals[i] ^ s
                    q.append(to)
                    if vals[to] == 0:
                        zeros.add(to)
                    else:
                        non_zeros.add(to)
            if len(zeros) < len(non_zeros):
                for i in itertools.chain(zeros, non_zeros):
                    vals[i] ^= 1
        for a_i in range(N):
            if vals[a_i]:
                ans[a_i] |= b

        b <<= 1

    print(*ans)


main()
