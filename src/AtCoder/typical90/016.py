from numba import njit

@njit
def solve(N, A, B, C):
    ans = 10**10
    for a in range(0, 10000):
        for b in range(0, 10000-a):
            d = N - a*A - b*B
            if d < 0:
                break
            if d % C == 0:
                c = d//C
                ans = min(ans, a+b+c)
    return ans  

def main():
    N = int(input())
    A, B, C = map(int, input().split())
    print(solve(N, A, B, C))

main()
