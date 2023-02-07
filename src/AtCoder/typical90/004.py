import numpy as np

def main():
    H, W = map(int, input().split())
    A = np.array([list(map(int, input().split())) for _ in range(H)], dtype=np.int64)
    B = -A
    hsum = A.sum(axis=0)
    wsum = A.sum(axis=1)
    for w in range(W):
        B[:,w] += hsum[w]
    for h in range(H):
        B[h,:] += wsum[h]
    for line in B:
        print(*line)

main()
