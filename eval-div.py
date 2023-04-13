def calcEquation(equations: list[list[str]], values: list[float], queries: list[list[str]]) -> list[float]:
    m = len(values)
    quotients = {}

    for i in range(m):
        num = equations[i][0]
        den = equations[i][1]
        quotients[num] = {den : values[i], num : 1.0}
        quotients[den] = {num : 1/values[i], den : 1.0}

    for num in quotients:
        for med in quotients:
            for den in quotients:
                if med != num and med != den and med in quotients[num].keys() and den in quotients[med].keys():
                    quotients[num][den] = quotients[num][med]*quotients[med][den]
                    quotients[den][num] = 1/quotients[num][den]

    n = len(queries)
    results = []
    for i in range(n):
        if queries[i][0] in quotients.keys() and queries[i][1] in quotients[queries[i][0]].keys():
            val = quotients[queries[i][0]][queries[i][1]]
            results.append(val)
        else:
            results.append(-1.0)

    return results

output = calcEquation([["a","b"], ["b", "c"]], [2.0, 3.0], [["a","c"], ["b","a"], ["a", "e"], ["a", "a"], ["x", "x"]])
print(output)
