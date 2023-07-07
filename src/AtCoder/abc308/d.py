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
    SS = [input() for _ in range(H)]
    snuke_to_num = {
        's': 0,
        'n': 1,
        'u': 2,
        'k': 3,
        'e': 4,
    }
    m = [[snuke_to_num.get(c, -1) for c in S] for S in SS]
    if m[0][0] == -1:
        print(No)
        return
    #
    reached = {(0, 0)}
    def dfs(h, w):
        n = m[h][w]
        nn = (n + 1) % 5
        for dh, dw in ((1, 0), (0, 1), (-1, 0), (0, -1)):
            nh, nw = h + dh, w + dw
            if nh in range(0, H) and nw in range(0, W):
                if m[nh][nw] == nn and (nh, nw) not in reached:
                    reached.add((nh, nw))
                    dfs(nh, nw)

    dfs(0, 0)

    if (H-1, W-1) in reached:
        print(Yes)
    else:
        print(No)


if __name__ == "__main__":
    main()
