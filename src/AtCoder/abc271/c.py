from collections import deque

N = int(input())
A = list(set(map(int, input().split()))) # 重複排除済みリスト
A.sort()
A = deque(A)

# 所持金の初期値 = 売却した冊数 = 最初に持っていた冊数 - 現在持っている冊数
wallet = N - len(A)

c = 0 # ここまで読んだ
while True:
    if A and A[0] == c + 1:
        c = A.popleft()
    elif wallet >= 2:
        wallet -= 2
        c += 1
    elif A:
        A.pop()
        wallet += 1
    else:
        break

print(c)
