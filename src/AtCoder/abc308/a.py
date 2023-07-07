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
    S = lmis()
    if all(a <= b for a, b in zip(S, S[1:])):
        if all(100 <= a <= 675 for a in S):
            if all(a % 25 == 0 for a in S):
                print('Yes')
                return
    print('No')


if __name__ == "__main__":
    main()
