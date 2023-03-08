from numba import njit

N = int(input())
A = list(map(lambda x: -int(x), input().split()))
S = [input() for _ in range(N)]
INF = N*10
Q = int(input())
UV = [tuple(map(lambda x: int(x)-1, input().split())) for _ in range(Q)]

@njit
def main():
    dist = [[(INF, INF)]*N for _ in range(N)]
    for i in range(N):
        dist[i][i] = (0, 0)
    for i in range(N):
        for j in range(N):
            if S[i][j] == 'Y':
                dist[i][j] = (1, A[j])
    # fw
    for k in range(N):
        for i in range(N):
            if k==i:
                continue
            for j in range(N):
                new_dist = (dist[i][k][0]+dist[k][j][0], dist[i][k][1]+dist[k][j][1])
                if dist[i][j] > new_dist:
                    dist[i][j] = new_dist
    #
    for u, v in UV:
        if dist[u][v][0] == INF:
            print('Impossible')
        else:
            print(dist[u][v][0], -(dist[u][v][1]+A[u]))

main()
