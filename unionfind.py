class unionfind:
    def __init__(self):
        self.parent = {}
        self.rank = {}
        self.count = 0

    def add(self,p):
        self.parent[p] = p
        self.rank[p] = 1
        self.count+=1

    def root(self,i):
        while i != self.parent[i]:
            self.parent[i] = self.parent[self.parent[i]] # path compression
            i = self.id[i]
        return i

    def union(self, p,q):
        i,j = self.root(p), self.root(q)
        if i == j:
            return
        if self.rank[i] > self.rank[j]:
            i,j = j,i
            self.parent[i] = j
            self.rank[j] += self.rank[i]
            self.count -=1
