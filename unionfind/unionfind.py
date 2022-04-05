class UnionFind:
    def __init__(self, n):
        self._parents = [node for node in range(n)]
        self._ranks = [1 for _ in range(n)]

    def union(self, u, v):
        root_u, root_v = self.find(u), self.find(v)
        if root_u == root_v:
            return 

        if self._ranks[root_u] > self._ranks[root_v]:
            self._parents[root_v] = root_u
        elif self._ranks[root_u] < self._ranks[root_v]:
            self._parents[root_u] = root_v
        else:
            self._parents[root_u] = root_v
            self._ranks[root_v] += 1
    
    def find(self, u):
        while self._parents[u] != u:
            self._parents[u] = self._parents[self._parents[u]]
            u = self._parents[u]
        return u

unionfind = UnionFind(5)
print(unionfind._parents)

unionfind.union(0,1)
print(unionfind._parents)

print(unionfind.find(1))
print(unionfind.find(0))
