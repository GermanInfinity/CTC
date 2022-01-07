"""
	validate_bst.py: bst is tree that mains left < node <= right
"""

def validate_bst(root):
    if root is None: return True
    helper(root, float('-inf') , float('inf'))


def helper(node, minn, maxn): 
    if node is None: return True 
    if node.left: 
        if node.left.value > maxn: return False
    if node.right: 
        if node.right.value < minn: return False

    return helper(node.left, node.left.value, node.value) and helper(node.right, node.value,node.right.value) 