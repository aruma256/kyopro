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


import heapq

def main():
    N, K = mis()
    A = lmis()
    A.sort()
    q = [0]
    count = 0
    checker = set()
    while True:
        p = heapq.heappop(q)
        if count == K:
            print(p)
            return
        count += 1
        for a in A:
            np = p + a
            if np not in checker:
                checker.add(np)
                heapq.heappush(q, p+a)


main()
