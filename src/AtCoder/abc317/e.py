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
    A = [list(input()) for _ in range(H)]
    for row_i, row in enumerate(A):
        for col_i, cell in enumerate(row):
            if cell == 'S':
                start = (row_i, col_i)
            elif cell == 'G':
                goal = (row_i, col_i)
    B = [row[:] for row in A]
    for row_i, row in enumerate(A):
        for col_i, cell in enumerate(row):
            if cell == 'v':
                B[row_i][col_i] = '#'
                for target_row_i in range(row_i+1, H):
                    if A[target_row_i][col_i] == '.':
                        B[target_row_i][col_i] = '#'
                    else:
                        break
            elif cell == '^':
                B[row_i][col_i] = '#'
                for target_row_i in range(row_i-1, -1, -1):
                    if A[target_row_i][col_i] == '.':
                        B[target_row_i][col_i] = '#'
                    else:
                        break
            elif cell == '>':
                B[row_i][col_i] = '#'
                for target_col_i in range(col_i+1, W):
                    if A[row_i][target_col_i] == '.':
                        B[row_i][target_col_i] = '#'
                    else:
                        break
            elif cell == '<':
                B[row_i][col_i] = '#'
                for target_col_i in range(col_i-1, -1, -1):
                    if A[row_i][target_col_i] == '.':
                        B[row_i][target_col_i] = '#'
                    else:
                        break
            elif cell == 'G':
                B[row_i][col_i] = '.'
    del A
    # bfs
    from collections import deque
    q = deque()
    q.append((start, 0))
    visited = [[False]*W for _ in range(H)]
    visited[start[0]][start[1]] = True
    while q:
        now, depth = q.popleft()
        if now == goal:
            print(depth)
            return
        now_row, now_col = now
        for d_row, d_col in ((1, 0), (-1, 0), (0, 1), (0, -1)):
            next_row = now_row + d_row
            next_col = now_col + d_col
            if 0 <= next_row < H and 0 <= next_col < W and not visited[next_row][next_col] and B[next_row][next_col] == '.':
                visited[next_row][next_col] = True
                q.append(((next_row, next_col), depth+1))
        # print(q)
    print(-1)
    # from pprint import pprint
    # pprint(B)


main()
