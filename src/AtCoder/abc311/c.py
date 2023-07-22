import sys
sys.setrecursionlimit(1000000000)
ii = lambda: int(input())
mis = lambda: map(int, input().split())
m0s = lambda: map(lambda x: int(x)-1, input().split())
lmis = lambda: list(mis())
lm0s = lambda: list(m0s())
INF = float('inf')
N1097 = 10**9 + 7
Yes = 'Yes'
No = 'No'


class dsu():
    n=1
    parent_or_size=[-1 for i in range(n)]
    def __init__(self,N):
        self.n=N
        self.parent_or_size=[-1 for i in range(N)]
    def merge(self,a,b):
        assert 0<=a<self.n, "0<=a<n,a={0},n={1}".format(a,self.n)
        assert 0<=b<self.n, "0<=b<n,b={0},n={1}".format(b,self.n)
        x=self.leader(a)
        y=self.leader(b)
        if x==y:
            return x
        if (-self.parent_or_size[x]<-self.parent_or_size[y]):
            x,y=y,x
        self.parent_or_size[x]+=self.parent_or_size[y]
        self.parent_or_size[y]=x
        return x
    def same(self,a,b):
        assert 0<=a<self.n, "0<=a<n,a={0},n={1}".format(a,self.n)
        assert 0<=b<self.n, "0<=b<n,b={0},n={1}".format(b,self.n)
        return self.leader(a)==self.leader(b)
    def leader(self,a):
        assert 0<=a<self.n, "0<=a<n,a={0},n={1}".format(a,self.n)
        if (self.parent_or_size[a]<0):
            return a
        self.parent_or_size[a]=self.leader(self.parent_or_size[a])
        return self.parent_or_size[a]
    def size(self,a):
        assert 0<=a<self.n, "0<=a<n,a={0},n={1}".format(a,self.n)
        return -self.parent_or_size[self.leader(a)]
    def groups(self):
        leader_buf=[0 for i in range(self.n)]
        group_size=[0 for i in range(self.n)]
        for i in range(self.n):
            leader_buf[i]=self.leader(i)
            group_size[leader_buf[i]]+=1
        result=[[] for i in range(self.n)]
        for i in range(self.n):
            result[leader_buf[i]].append(i)
        result2=[]
        for i in range(self.n):
            if len(result[i])>0:
                result2.append(result[i])
        return result2


def main():
    N = ii()
    A = lm0s()
    uf = dsu(N)
    for i, a in enumerate(A):
        if uf.leader(i) == uf.leader(a):
            # 閉路が存在する
            # それを出力する
            ans = [i]
            next_i = A[i]
            while next_i != i:
                ans.append(next_i)
                next_i = A[next_i]
            print(len(ans))
            print(*[a+1 for a in ans])
            return
        else:
            uf.merge(i, a)


main()
