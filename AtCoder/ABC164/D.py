'''
[point 1]
1817181712114 の部分 "18171"について考える...

    181710000 / 10000 ≡ 0 (MOD 2019) ならば、2019の倍数
    181710000 ≡ 0 (MOD 2019) でよい

[point 2]
    181710000
    =
    181712114
    -
         2114

    なので、特定区間の値 は 累積和の差 から瞬時に求められる。
    さらに、181710000 ≡ 0 (MOD 2019) を考えると、

    0 ≡ 181712114 - 2114
    → 181712114 ≡ 2114

    となる。
    結局の所、MOD2019において合同な累積和のペアの数の数え上げ。
'''

from collections import defaultdict

def gen_10exp_mod(n, mod):
    a = 1
    yield a
    for _ in range(1, n):
        a = (a*10) % mod
        yield a

def main():
    MOD = 2019
    S = input()[::-1]
    # 桁ごとの実際の値を計算 (MOD)
    A = [int(s)*n % MOD for s, n in zip(S, gen_10exp_mod(len(S), MOD))]
    # 累積和を計算
    ACC = [0]
    for a in A:
        ACC.append((ACC[-1] + a) % MOD)
    # ペア数え上げ
    d = defaultdict(int)
    for acc in ACC:
        d[acc] += 1
    ans = sum(v*(v-1)//2 for v in d.values())
    print(ans)

main()
