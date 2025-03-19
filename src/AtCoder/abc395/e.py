import heapq

INF = 10**18

def main():
    N, M, X = map(int, input().split())
    N2 = N*2
    w: list[set[tuple[int, int]]] = [set() for _ in range(N2)]

    # 反転世界へ渡るコスト = X
    for i in range(N):
        w[i].add((i+N, X))
        w[i+N].add((i, X))

    # 辺を受け取る
    for _ in range(M):
        u, v = map(int, input().split())
        u -= 1
        v -= 1
        w[u].add((v, 1))
        w[v+N].add((u+N, 1)) # 反転世界では逆向きに辺がある

    # ダイクストラ法
    scores = [INF] * N2
    scores[0] = 0
    q = []
    heapq.heappush(q, (0, 0))
    while q:
        score, node = heapq.heappop(q)
        if score > scores[node]:
            continue
        for to, cost in w[node]:
            if scores[to] > score + cost:
                scores[to] = score + cost
                heapq.heappush(q, (score + cost, to))

    print(min(scores[N - 1], scores[N2 - 1]))


main()
