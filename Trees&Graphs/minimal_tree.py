"""
    minimal_tree.py: algo that creates BST 
"""

class TreeNode:
    def __init__(self, val = None):
        self.val = val
        self.left = None
        self.right = None
def minimal_tree(array): 
    if array: 
        mid = len(array) // 2
        left = array[:mid]
        right = array[mid+1:]

        root = TreeNode(array[mid])
        root.left = minimal_tree(left)
        root.right = minimal_tree(right)

        return root