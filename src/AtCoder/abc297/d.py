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

A, B = mis()

def simple():
    a, b = A, B
    count = 0
    while a != b:
        if a > b:
            a = a - b
        else:
            b = b - a
        count += 1
    return count


def solve():
    a, b = A, B
    count = 0
    while a != b:
        if a < b:
            a, b = b, a
        d = (a-b)//b
        if d:
            a -= b*d
            count += d
        else:
            a = a - b
            count += 1
    return count
    


def main():
    print(solve())



main()
