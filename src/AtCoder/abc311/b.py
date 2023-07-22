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
    N, D = mis()
    S = [input() for _ in range(N)]
    max_cont = 0
    cont = 0
    for day_i in range(D):
        if all(S[person_i][day_i]=='o' for person_i in range(N)):
            cont += 1
            max_cont = max(max_cont, cont)
        else:
            cont = 0
    print(max_cont)


main()
