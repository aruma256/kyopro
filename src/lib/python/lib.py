import sys
sys.setrecursionlimit(1000000000)
import math
from math import gcd
def lcm(a, b): return a * b // gcd(a, b)
from itertools import count, permutations, combinations, chain, product
from functools import lru_cache
from collections import deque, defaultdict, OrderedDict
from operator import itemgetter
from pprint import pprint
import heapq
ii = lambda: int(input())
mis = lambda: map(int, input().split())
lmis = lambda: list(mis())
INF = float('inf')
N1097 = 10**9 + 7

def meg(f, ok, ng):
    while abs(ok-ng)>1:
        mid = (ok+ng)//2
        if f(mid):
            ok=mid
        else:
            ng=mid
    return ok

def get_inv(n, modp):
    return pow(n, modp-2, modp)

def factorials_list(n, modp):    # 10**6
    fs = [1]
    for i in range(1, n+1):
        fs.append(fs[-1] * i % modp)
    return fs

def invs_list(n, fs, modp):     # 10**6
    invs = [get_inv(fs[-1], modp)]
    for i in range(n, 1-1, -1):
        invs.append(invs[-1] * i % modp)
    invs.reverse()
    return invs

def comb(n, k, modp):
    num = 1
    for i in range(n, n-k, -1):
        num = num * i % modp
    den = 1
    for i in range(2, k+1):
        den = den * i % modp
    return num * get_inv(den, modp) % modp

def comb_from_list(n, k, modp, fs, invs):
    return fs[n] * invs[n-k] * invs[k] % modp
