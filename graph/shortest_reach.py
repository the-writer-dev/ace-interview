# link: https://www.hackerrank.com/challenges/ctci-bfs-shortest-reach/problem

# idea
# build the graph
# use bfs to search through and calculate the distances at each node 
from collections import defaultdict

def shortest_reach(v, e, start):
    graph = defaultdict(dict)

    distances = [-1] * v
    for k, v in e:
        graph[k][v] = 1 
        graph[v][k] = 1

    

    # why this weird 'start-1'? - normaly elements in arr start with 0 but given nodes start with 1  
    distances[start-1] = 0
    q = [start]
    visited = {start}
    while q:
        level_size = len(q)
        for _ in range(level_size):
            n = q.pop(0)
            for neighbor in graph[n]:
                if neighbor not in visited:
                    q.append(neighbor)
                    visited.add(neighbor)
                    distances[neighbor-1] = distances[n-1] + 6
    
    # return distances excluding the element of starting index 
    return [distances[i] for i, x in enumerate(distances) if i not in [start-1]] 

e = [[1,2], [2,3], [3,4], [1,5]]
print(shortest_reach(6, e, 2))
