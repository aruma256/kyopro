from itertools import count
import math

def find(n: int):
    for i in count(2):
        if n%i == 0:
            if n%(i**2) == 0:
                p = i
                q = n//(i**2)
            else:
                p = int(math.sqrt(n//i))
                q = i
            return p, q

def main():
    T = int(input())
    for _ in range(T):
        n = int(input())
        print(*find(n))

main()
