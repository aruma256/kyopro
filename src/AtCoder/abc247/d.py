from collections import deque, namedtuple

dq = deque()

class BallGroup:
    def __init__(self, number, count) -> None:
        self.number = number
        self.count = count

for _ in range(int(input())):
    q = tuple(map(int, input().split()))
    if q[0] == 1:
        _, x, c = q
        dq.append(BallGroup(x, c))
    else:
        _, c = q
        t_ans = 0
        while c:
            bg = dq.popleft()
            d = min(c, bg.count)
            c -= d
            bg.count -= d
            t_ans += bg.number * d
            if bg.count:
                dq.appendleft(bg)
        print(t_ans)
