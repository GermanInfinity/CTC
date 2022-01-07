## connected components count 

graph = {3:[], 4:[6], 6:[4,5,7,8], 8:[6], 7:[6], 5:[6], 1:[2], 2:[1]}

def connected_components(graph): 
    if graph is None: return 
    # run dfs on every node
    # keep a visited list 
    # visited = set()
    # comp = 0 
    # for node in graph:
    #     if node in visited: 
    #         comp += 1
    #         continue 

    #     visited.add(node)
    #     if len(graph[node]) == 0: 
    #         #comp += 1
    #         continue

    #     for neighbour in graph[node]: 
    #         visited.add(neighbour)

    # print (comp)

    visited = set()
    count = 0 
    for node in graph:
        if dfs(graph, node, visited) == True:
            count += 1

    print (count)



# explored componenet as far as possible
def dfs(graph, src, visited):
    if src in visited: return False

    visited.add(src)
    for node in graph[src]: 
        dfs(graph, node, visited) 

    return True # explored whole component


connected_components(graph)