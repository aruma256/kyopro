from datetime import time

A, B, C, D = map(int, input().split())
if time(A, B, 0) < time(C, D, 1):
    print('Takahashi')
else:
    print('Aoki')
