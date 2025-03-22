# tags: binary search

def main():
    N, X = map(int, input().split())
    us = []
    ds = []
    for _ in range(N):
        u, d = map(int, input().split())
        us.append(u)
        ds.append(d)

    # 最適な H を二分探索で求める
    def check(h):
        u_longest = us[0]
        u_shortest = 0
        for u, d in zip(us, ds):
            if u + d < h:
                return False

            diff = (u + d) - h

            tmp_u_longest = u if diff <= d else u - (diff - d)
            tmp_u_shortest = max(u - diff, 0)
            u_longest = min(u_longest + X, tmp_u_longest)
            u_shortest = max(u_shortest - X, tmp_u_shortest)

            if u_longest < u_shortest:
                return False

        return True

    ok = 0
    ng = sum(us) + sum(ds) + 1
    while abs(ok - ng) > 1:
        mid = (ok + ng) // 2
        if check(mid):
            ok = mid
        else:
            ng = mid

    ok_h = ok
    cost = sum(us) + sum(ds) - ok_h * N
    print(cost)

main()
