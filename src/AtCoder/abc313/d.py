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


def ask(query):
    print('? ' + ' '.join(str(v+1) for v in query))
    res = ii()
    if res == -1:
        import time
        time.sleep(10)
    return res


def main():
    N, K = mis()
    # K+1 区間内を特定する
    res = []
    for i in range(K+1):
        query = list(range(0, i)) + list(range(i+1, K+1))
        res.append(ask(query))
    range_sum = sum(res) & 1
    ans = [res[i]^range_sum for i in range(K+1)]
    # 残りの区間を特定する
    base = sum(res[:K-1]) & 1
    query = list(range(K))
    for i in range(K+1, N):
        query[-1] = i
        ans.append(ask(query)^base)
    print('! ' + ' '.join(str(v) for v in ans))


main()
