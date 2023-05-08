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
    S = input()
    ss = []
    for i in range(len(S)):
        ss.append(S[i:] + S[:i])
    ss.sort()
    print(ss[0])
    print(ss[-1])

main()
