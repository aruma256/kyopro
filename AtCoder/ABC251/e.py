N = int(input())
A = list(map(int, input().split()))

def calc(A):
    p = A[0]
    s = 10**11

    for a in A[1:]:
        p, s = min(p, s) + a, p

    return min(p, s)

def main():
    print(min(calc(A), calc(A[::-1])))

main()
