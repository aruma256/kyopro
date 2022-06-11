from numba import njit

@njit
def solve(N):
    S = [n**2 for n in range(1, N+1)]
    ans = 0
    for i in range(1, N+1):
        for s in S:
            if s == 1:
                continue
            if i < s:
                break
            while i%s == 0:
                i //= s
        for s in S:
            j = i * s
            if j <= N:
                ans += 1
            else:
                break
    return ans

def main():
    print(solve(int(input())))

main()
