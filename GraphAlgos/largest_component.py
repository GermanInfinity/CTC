## largest component.py: returns size of largest component in graph 

graph = {0:[8,1,5], 1:[0], 5:[0,8], 8:[0,5], 2:[3,4], 3:[2,4], 4:[3,2]}

def largest_component(graph): 
    if graph is None: return None 
    # keep visited list to ensure you are not visiting same component twice 
    # go through all components, update a max value for size
    # return max 

    visited = set()
    max_val = float('-inf')

    for node in graph: 
        seen_component, size = dfs(graph, node, visited)
        if seen_component == True: 
            if size > max_val:
                max_val = size

    print (max_val)


    


def dfs(graph, src, visited): 
    if src in visited: return False, 0

    visited.add(src)
    size = 1
    for node in graph[src]: 
        size += dfs(graph, node,visited)[1]

    return True, size

largest_component(graph)