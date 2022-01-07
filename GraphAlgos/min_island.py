# minimum island count 

def island_count(graph): 
    # keep visited list 
    # use iterative to move through area
    # use depth first to get whole component

    visited = set()
    min_val = float('inf')
    for row in len(graph):
        for col in len(graph[0]): 
            val = dfs(graph, row, col, visited)
	        if val[0]: 
	            if val[1] < min_val: 
                    min_val = val[1]

    return count


def dfs(graph, row, col, visited): 
    if row < 0 or row >= len(graph) or col < 0 or col >= len(graph[0]): return False,
    0
    if graph[row][col] in visited: return False, 0

    if grid[row][col] == "W": return False, 0

    visited.add(graph[row][col])
    size = 1

    #for nod in graph[node]: 
    size += dfs(graph, row + 1, col, visited)
    size += dfs(graph, row - 1, col, visited)
    size += dfs(graph, row, col + 1, visited)
    size += dfs(graph, row, col - 1, visited)

    return True, size


island = 
print (island_count(island))