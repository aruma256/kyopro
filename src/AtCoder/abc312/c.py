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
    events = []
    for a in A:
        events.append((a, 1, 0))
    for b in B:
        events.append((b+1, 0, -1))
    events.sort()
    #
    seller = 0
    buyer = M
    for event in events:
        price, seller_diff, buyer_diff = event
        seller += seller_diff
        buyer += buyer_diff
        if seller >= buyer:
            print(price)
            return


main()
