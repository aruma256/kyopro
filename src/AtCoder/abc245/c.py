N, K = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

available_numbers = {A.pop(), B.pop()}
while A:
    tmp = set()
    a, b = A.pop(), B.pop()
    for n in available_numbers:
        if abs(a - n) <= K:
            tmp.add(a)
        if abs(b - n) <= K:
            tmp.add(b)
    available_numbers = tmp

print('Yes' if available_numbers else 'No')
