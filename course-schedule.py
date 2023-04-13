import networkx as nx
from queue import Queue

def canFinish(numCourses: int, prerequisites: list[list[int]])-> bool:
    m = len(prerequisites)
    eligible = Queue(maxsize = m)
    cg = nx.DiGraph()

    for i in range(numCourses):
        prereq = 0
        for j in range(m):
            if prerequisites[j][0] == i:
                cg.add_edge(prerequisites[j][1], i)
                prereq += 1
        if prereq == 0:
            eligible.put(i)

    esize = eligible.qsize()
    count = numCourses
    while esize > 0:
        course = eligible.get()
        esize -= 1
        for c in list(cg.successors(course)):
            cg.remove_edge(course, c)
            if list(cg.predecessors(c)) == []:
                eligible.put(c)
                esize += 1
        count -= 1
    
    if count > 0:
        return False
    return True

retval = canFinish(2, [[1,0], [0,1]])
print(retval)


