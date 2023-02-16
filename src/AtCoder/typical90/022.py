import math

A, B, C = map(int, input().split())
l = math.gcd(math.gcd(A, B), C)
print(A//l - 1 + B//l - 1 + C//l - 1)
