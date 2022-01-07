
## has_path
graph = {'f':['g', 'i'], 'g':['h'], 'h':[], 'i':['g', 'k'], 'j':['i'], 'k':[]}

def has_path(graph, src, dst): 
    if graph is None or src is None or dst is None: return False 

    queue = [ src ]

    while queue: 
        current = queue[0]
        queue = queue[1:]

        for child in graph[current]:
            if child == dst: return True

            queue.append(child)

    return False


def dfs_has_path(graph, src, dst):
    if graph is None or src is None or dst is None: return False 
    if src == dst: return True
    for neighbour in graph[src]: 
        if (dfs_has_path(graph, neighbour, dst)): return True

    return False



print (dfs_has_path(graph, 'f', 'k'))