# depth first print on graph 

graph = {'a': ['b', 'c'], 'b':['d'], 'c':['e'], 'd':['f'], 'e':[], 'f':[]}

# Explores one direction till it can't anymore
def dfs_on_graph(graph, source): 
    if graph is None or source is None: return None

    stack = [ source ]

    while stack: 
        current = stack[-1]
        stack.pop()
        if current: 
            print (current)
            for ele in graph[current]: 
                stack.append(ele)

def dfs_recur(graph, source): 
    if graph is None or source is None: return None
    print (source)
    for ele in graph[source]: 
        dfs_recur(graph, ele)

print ("DFS")
dfs_recur(graph, 'a')

# Explores all directions evenly
def bfs_on_graph(graph, source): 
    if graph is None or source is None: return None 

    queue = [ source ]
    while queue: 
        current = queue[0]
        queue = queue[1:]
        if current: 
            print (current)
            for ele in graph[current]: 
                queue.append(ele)


print ("BFS")
bfs_on_graph(graph, 'a')