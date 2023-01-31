from collections import deque
from collections import defaultdict


class Graph:
    def __init__(self):
        self.graph = defaultdict(list)

    def addEdge(self, u, v):
        self.graph[u].append(v)

    def bfs(self, s):
        visited = [False] * (max(self.graph) + 1)
        q = deque([s])
        visited[s] = True

        while q:
            c = q.popleft()
            print(c)
            for v in self.graph[s]:
                if visited[v] == False:
                    q.append(v)
                    visited[v] = True


g = Graph()
g.addEdge(0, 1)
g.addEdge(0, 2)
g.addEdge(0, 3)
g.addEdge(1, 0)
g.addEdge(2, 0)
g.addEdge(2, 3)
g.addEdge(3, 0)
g.addEdge(3, 2)

g.bfs(0)
