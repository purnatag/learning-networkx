from __future__ import annotations
import networkx as nx

def validPath(n: int, edges: list[list[int]], source: int, destination: int) -> bool:
    G = nx.Graph()
    m = len(edges)
    visited = []
    for i in range(m):
        G.add_edge(*edges[i])
        visited.append(0)
        visited.append(0)

    retval = dfs(source, destination, G, visited)
    return retval

def dfs(src: int, dest: int, G: nx.graph, visited: list[int]) -> bool:
    if src == dest:
        return True
    elif visited[src] == 1:
        return False

    visited[src] = 1
    for v in list(G.adj[src]):
        if v == dest:
            return True
        if dfs(v, dest, G, visited):
            return True
    return False

val = validPath(6, [[0,1], [0,2], [3,5], [5,4], [4,3]], 0, 5)
if val:
    print("True")
else:
    print("False")