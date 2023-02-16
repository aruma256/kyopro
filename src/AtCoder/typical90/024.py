N, K = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

def main():
    s = sum(abs(a-b) for a, b in zip(A, B))
    if s > K:
        print('No')
        return
    if (K - s) % 2 == 0:
        print('Yes')
    else:
        print('No')

main()
