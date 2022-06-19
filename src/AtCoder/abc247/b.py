from itertools import chain
from collections import Counter

def main():
    N = int(input())

    ST = [input().split() for _ in range(N)]

    C = Counter()
    for s, t in ST:
        C[s] += 1
        if s != t:
            C[t] += 1

    for s, t in ST:
        if C[s] > 1 < C[t]:
            print('No')
            return
    
    print('Yes')

main()
