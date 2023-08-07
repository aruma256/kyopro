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
    N = ii()
    A = lmis()
    A.sort()
    #
    def calc(target_low):
        plus_diff = 0
        minus_diff = 0
        target_high = target_low + 1
        for a in A:
            if a < target_low:
                plus_diff += abs(target_low - a)
            elif target_high < a:
                minus_diff += abs(target_high - a)
        return max(plus_diff, minus_diff)
    #
    avr = sum(A) / N
    avr_low = int(avr)
    print(min(calc(i) for i in range(avr_low-2, avr_low+3)))


main()
