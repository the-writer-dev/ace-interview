class UnionFind:
    # initially each node is its parent and rank is 1
    def __init__(self, N):
        self.parents = [n for n in range(N)]
        self.ranks = [1 for _ in range(N)]

    # path compression
    # complexity: O(log n)
    def find(self, u):
        while u != self.parents[u]:
            self.parents[u] = self.parents[self.parents[u]]
            u = self.parents[u]
        return u

    # union by rank
    # complex: O(log n)
    def union(self, u, v):
        if self.ranks[u] < self.ranks[v]:
            self.parents[u] = v
        elif self.ranks[u] > self.ranks[v]:
            self.parents[v] = u
        else:
            self.parents[v] = u
            self.ranks[u] += 1
