import bisect

def main():
    N = int(input())
    A = list(map(int, input().split()))
    A.append(-10000000000)
    A.append(10000000000)
    A.sort()
    for _ in range(int(input())):
        b = int(input())
        idx = bisect.bisect(A, b)
        print(min(abs(b-A[idx]), abs(b-A[idx-1])))

main()
