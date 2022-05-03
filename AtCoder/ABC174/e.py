N, K = map(int, input().split())
A = list(map(int, input().split()))

def nibutan(f, ok, ng):
    while abs(ok - ng) > 1:
        mid = (ok + ng) // 2
        if f(mid):
            ok = mid
        else:
            ng = mid
    return ok

def check(target_length):
    count = 0
    for a in A:
        count += (a - 1) // target_length
    return count <= K

def main():
    ans = nibutan(check, max(A), 0)
    print(ans)

main()
