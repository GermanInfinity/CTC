## undirected path 

edges = [['i','j'],['k','i'],['m','k'],['k','l'],['o','n']]

# time: O(e); space: O(n)
def undirected_path(edges, src, dst): 
    if edges is None or src is None or dst is None: return False
    # convert edge list to adjacency list
    graph = {}
    for edge in edges: 
        if edge[0] in graph:
            graph[edge[0]].append(edge[1])
        else: 
            graph[edge[0]] = [edge[1]]

        if edge[1] in graph:
            graph[edge[1]].append(edge[0])
        else: 
            graph[edge[1]] = [edge[0]]


    if src not in graph: return False
    if dst not in graph: return False

    # Find with dfs
    return bfs(graph, src, dst)
    return dfs(graph, src, dst, set()) 

    

def dfs(graph, src, dst, visited): 
    if graph is None or src is None or dst is None: return False

    if src == dst: return True
    visited.add(src)
    for neighbour in graph[src]:
        if neighbour in visited: continue
        if dfs(graph, neighbour, dst, visited): return True

    return False


def bfs(graph, src, dst): 
    if graph is None or src is None or dst is None: return False
    queue = [ src ]
    visited = set()

    while queue: 
        current = queue[0]
        queue = queue[1:]
        if current: 
            for neighbour in graph[current]: 
                if neighbour in visited: continue
                if neighbour == dst: return True
                visited.add(neighbour)
                queue.append(neighbour)

    return False

print (undirected_path(edges, 'l','j'))