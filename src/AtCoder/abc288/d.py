def main():
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    while len(A) % K != 0:
        A.append(0)
    #
    CA = [[0]*K]
    try:
        for lvl in range(N//K + 1):
            CA.append(list(CA[-1][k]+A[lvl*K+k] for k in range(K)))
    except:
        pass

    # from pprint import pprint
    # pprint(CA)

    #
    lr = [tuple(map(int, input().split())) for _ in range(int(input()))]

    #
    for l, r in lr:
        l -= 1
        r -= 1
        diffs = set()
        for i in range(min(K, r-l+1)):
            s = l + i
            slvl = s // K
            e = r
            while e%K != s%K:
                e -= 1
            elvl = e // K + 1
            k = s%K
            # print(f"s {s}, e {e}, slvl {slvl}, elvl {elvl}, k {k}")
            diffs.add(CA[elvl][k] - CA[slvl][k])
        if len(diffs)==1:
            print('Yes')
        else:
            print('No')
        # print(diffs)

main()
