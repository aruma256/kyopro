H, W = map(int, input().split())

# https://github.com/shakayami/ACL-for-python/blob/master/dsu.py
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


def rc_to_idx(r, c):
    return r*W + c

def main():
    uf = dsu((H+1)*(W+1))
    Q = int(input())
    RED = [False] * (rc_to_idx(H, W) + 1)
    for _ in range(Q):
        q = list(map(int, input().split()))
        if q[0] == 1:
            _, r, c = q
            RED[rc_to_idx(r, c)] = True
            for nr, nc in ((r+1, c), (r-1, c), (r, c+1), (r, c-1)):
                if 1 <= nr <= H and 1 <= nc <= W and RED[rc_to_idx(nr, nc)]:
                    uf.merge(rc_to_idx(nr, nc), rc_to_idx(r, c))
        else:
            _, ar, ac, br, bc = q
            if RED[rc_to_idx(ar, ac)] and uf.same(rc_to_idx(ar, ac), rc_to_idx(br, bc)):
                print('Yes')
            else:
                print('No')

main()
