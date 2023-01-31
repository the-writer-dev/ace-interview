# link:
import union_find


def minCostConnectPoints(self, points: List[List[int]]) -> int:
    def manhattanDist(p1, p2):
        return abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])

    edges = []
    n = len(points)
    for i in range(n):
        for j in range(i + 1, n):
            edges.append([manhattanDist(points[i], points[j]), i, j])

    edges.sort()  # Sort increasing order by dist
    uf = union_find.UnionFind(n)
    ans = 0
    for d, u, v in edges:
        if uf.union(u, v):
            ans += d
            n -= 1
        if n == 1:
            break  # a bit optimize when we found enough n-1 edges!
    return ans
