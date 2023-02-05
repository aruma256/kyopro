N, L = map(int, input().split())
K = int(input())
A = list(map(int, input().split()))

def meg(f, ok, ng):
    while abs(ok-ng)>1:
        mid = (ok+ng)//2
        if f(mid):
            ok=mid
        else:
            ng=mid
    return ok

def check(target_min_length):
    # K回以上切るとき、最短ピース(スコア)を target_min_length 以上にできるか
    # K+1回切っても s を達成可能 → K回切ったときに s を達成可能
    left = 0
    cut_count = 0
    for a in A:
        length = a - left
        if length >= target_min_length and L - a >= target_min_length:
            left = a
            cut_count += 1
    return cut_count >= K

def main():
    print(meg(check, 0, L))

main()
