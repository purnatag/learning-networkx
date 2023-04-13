import networkx as nx

def allPathsSourceTarget(graph: list[list[int]]) -> list[list[int]]:
    n = len(graph)
    dag = nx.DiGraph()

    for i in range(n):
        for v in graph[i]:
            dag.add_edge(i, v)

    memo = [[] for i in range(n)]
    allpaths = dfs(0, n-1, dag, memo)
    return allpaths

def dfs(src: int, dest: int, dag: nx.graph, memo: list[list[list[int]]])-> list[list[int]]:
    if memo[src] != []:
        return memo[src]
    
    if src == dest:
        memo[src].append([src])
        return memo[src]
    
    result = []
    for v in list(dag.adj[src]):
        if v == dest:
            plist = [src, dest]
            result.append(plist)
        else:
            paths = dfs(v, dest, dag, memo)
            if len(paths) == 0: continue
            for path in paths:
                plist = [src]
                plist.extend(path)
                result.append(plist)

    memo[src] = result
    return result

vpaths = allPathsSourceTarget([[1,2], [3], [3], []])
print(vpaths)

