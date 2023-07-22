import sys
sys.setrecursionlimit(1000000000)
ii = lambda: int(input())
mis = lambda: map(int, input().split())
m0s = lambda: map(lambda x: int(x)-1, input().split())
lmis = lambda: list(mis())
lm0s = lambda: list(m0s())
INF = float('inf')
N1097 = 10**9 + 7
Yes = 'Yes'
No = 'No'


def main():
    H, W = mis()
    S = [input() for _ in range(H)]
    stopped = [[False]*W for _ in range(H)]
    visited = [[False]*W for _ in range(H)]
    q = [(1, 1)]
    while q:
        h, w = q.pop()
        if stopped[h][w]:
            continue
        stopped[h][w] = True
        visited[h][w] = True
        for dh, dw in ((-1, 0), (1, 0), (0, -1), (0, 1)):
            nh, nw = h, w
            while S[nh+dh][nw+dw] == '.':
                nh += dh
                nw += dw
                # print(nh, nw)
                visited[nh][nw] = True
            if not stopped[nh][nw]:
                q.append((nh, nw))
    # visitedを数え上げる
    ans = 0
    for h in range(H):
        for w in range(W):
            if visited[h][w]:
                ans += 1
    print(ans)



main()
