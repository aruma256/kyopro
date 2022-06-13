'''
A = 500 とする。
このとき、X = 10^9 となるのは、 B = 499.9968... のとき。
→ AまたはB (の絶対値) が大きすぎると、Xが10^9に収まらない。

A, Bの探索範囲は -120~120で十分。
'''

from itertools import product

def main():
    X = int(input())
    for A, B in product(range(-150, 150), range(-150, 150)):
        if A**5 - B**5 == X:
            print(A, B)
            return

main()

'''
無限ループによる実装
Aを0, -1, 1, -2, 2, -3, 3 ... のように動かす

from itertools import count

def main():
    X = int(input())
    for i in count():
        for A in (-i, i):
            for B in range(-i, i+1):
                if A**5 - B**5 == X:
                    print(A, B)
                    return


main()
'''


