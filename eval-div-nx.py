import networkx as nx
def calcEquation(equations: list[list[str]], values: list[float], queries: list[list[str]]) -> list[float]:
    m = len(values)
    qg = nx.DiGraph()

    for i in range(m):
        num = equations[i][0]
        den = equations[i][1]
        qg.add_edge(num, den, weight = values[i])
        qg.add_edge(den, num, weight = 1/values[i])
        qg.add_edge(num, num, weight = 1.0)
        qg.add_edge(den, den, weight = 1.0)

    for num in qg.nodes():
        for med in qg.nodes():
            for den in qg.nodes():
                if med != num and med != den and qg.has_edge(num, med) and qg.has_edge(med, den):
                    qg.add_edge(num, den, weight = qg[num][med]['weight']*qg[med][den]['weight'])
                    qg.add_edge(den, num, weight = 1/qg[num][den]['weight'])

    n = len(queries)
    results = []
    for i in range(n):
        if queries[i][0] in qg.nodes() and qg.has_edge(queries[i][0], queries[i][1]):
            val = qg[queries[i][0]][queries[i][1]]['weight']
            results.append(val)
        else:
            results.append(-1.0)

    return results

output = calcEquation([["a","b"], ["b", "c"]], [2.0, 3.0], [["a","c"], ["b","a"], ["a", "e"], ["a", "a"], ["x", "x"]])
print(output)
