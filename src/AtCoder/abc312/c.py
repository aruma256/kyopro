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
    N, M = mis()
    A = lmis()
    B = lmis()
    event_map = {}
    for a in A:
        if a not in event_map:
            event_map[a] = [0, 0]
        event_map[a][0] += 1
    for b in B:
        if (b+1) not in event_map:
            event_map[b+1] = [0, 0]
        event_map[b+1][1] += 1
    events = [(price, diff) for price, diff in event_map.items()]
    events.sort(reverse=True)
    #
    seller = 0
    buyer = M
    while events:
        price, (seller_diff, buyer_diff) = events.pop()
        seller += seller_diff
        buyer -= buyer_diff
        if seller >= buyer:
            print(price)
            return


main()
