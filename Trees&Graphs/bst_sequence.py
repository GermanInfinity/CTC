"""
	bst_sequence.py: print all possible arrays
"""

def print_poss(tree): 
    if tree is None: return None 

    ptr = tree
    res = []
    while ptr: 
        ans = []
	    if ptr.left: 
	        left = helper(ptr.left)
	        ans.append(ptr.value)
	        ans.append(left.value)
	        ptr = ptr.left
	    if ptr.right: 
	        right = helper(ptr.right)
	        ans.append(right.value)
	        ptr = ptr.right

	        
	    res.append(ans)

	return res

def helper(node)
    if node.left == None and node.right == None: 
        return node.value

    val = []
    if node.left: val.append(helper(node.left))
    if node.right: val.append(helper(node.right))
    return val 



