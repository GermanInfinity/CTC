"""
	successor.py : finds next node (in-order successor) of a given node in a bst.
	link to parent exists.
"""

# best successor: in-order. left, root, right
def best_successor(node): 
	if node is None: return None

    ptr = node
    if ptr.right: 
    	current = ptr.right
    	while current and current.left: 
    		current = current.left
    	return current

    ancestor = node.parent
    child = node

    while ancestor and ancestor.right = child: 
    	child = ancestor
    	ancestor = ancestor.parent

    return ancestor
    	
# O(n) space O(n) time
def successor(tree, node): 
    # in order - left, root, right 
    if tree is None or node is None: return None

    in_order = order(tree, node)
    for i in range(len(in_order) - 1): 
    	if in_order[i] == node: return in_order[i + 1]

    return None


# O(1) space O(n) time
def fast_successor(tree, node): 
	if tree is None or node is None: return None
     
    ptr = tree

    while ptr: 
    	if ptr.value == node.value: 
    		if ptr.right: 
                return ptr.right
    		else: 
                # return to parent  
                if ptr.parent == None: return None
                if ptr.parent > node.value: 
                	return ptr.parent
                else: 
                	ptr = ptr.parent
    	elif ptr.value > node.value: 
    		ptr = ptr.right

        elif ptr.value < node.value: 
        	ptr = ptr.left

    if ptr is None: return "Node not in tree."

def get_in_order(root): 
	if root is None: return []

	return [get_in_order(root.left)] + [root] + [get_in_order(root.right)] 
	