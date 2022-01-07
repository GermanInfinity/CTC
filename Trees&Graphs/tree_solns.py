

BFS
queue = [root] # FIFO
while queue: 
    current = queue[0]
    queue = queue[1:]

    print (current.val)

    if current.left: queue.append(current.left)
    if current.right: queue.append(current.right)


DFS
stack = [root]
while stack: 
    current = stack.pop()
    print (current.val)
    if current.right: stack.append(current.right)
    if current.left: stack.append(current.left)


# Recursively
if node is None: return []

left = DFS(node.left)
right = DFS(node.right)
return [node.val, left, right]


# tree includes
if root is None: return False
if root.val == target: return True
return includes(root.left, target) or includs(root.right, target)


# tree sum 
if root is None: return 0 
val = root.val
return sum(root.left) + sum(root.right) + val