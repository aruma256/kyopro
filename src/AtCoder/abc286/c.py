from collections import deque

N, A, B = map(int, input().split())

S = input()

def main():
    dq = deque(S)

    ans = 10**20

    for i in range(N):
        score = i * A
        for j in range(0, N//2):
            if dq[j] != dq[N-1-j]:
                score += B
        ans = min(ans, score)
        dq.append(dq.popleft())

    print(ans)

main()
