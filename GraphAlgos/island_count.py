# island count 

def island_count(graph): 
    # keep visited list 
    # use iteratvie to move through area
    # use depth first to get whole component

    visited = set()
    count = 0 
    for row in len(graph):
        for col in len(graph[0]): 
	        if dfs(graph, row, col, visited): 
	            count += 1

    return count


def dfs(graph, row, col, visited): 
    if row < 0 or row >= len(graph) or col < 0 or col >= len(graph[0]): return False
    if graph[row][col] in visited: return False 

    if grid[row][col] == "W": return False 

    visited.add(graph[row][col])

    #for nod in graph[node]: 
    dfs(graph, row + 1, col, visited)
    dfs(graph, row - 1, col, visited)
    dfs(graph, row, col + 1, visited)
    dfs(graph, row, col - 1, visited)

    return True


island = 
print (island_count(island))