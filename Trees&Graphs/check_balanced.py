"""
    check_balanced.py: check if a binary tree is balanced.
"""
class BinaryNode: 
    def __init__(self, val): 
        self.value = val
        self.left, self.right = None, None 

def check_balanced(root): 
    if root is None: return True
    
    # get height on left 
    # get height on right 
    # subtract

    left = helper(root.left)
    right = helper(root.right)

    if abs(left - right) > 1: 
        return False

    else: 
        return check_balanced(root.left) and check_balanced(root.right)


def helper(node): # ge
    if node is None: return -1 

    height_l = helper(node.left) 
    height_r = helper(node.right) 
    return max(height_l, height_r) + 1


def _gen_balanced_1():
    root = BinaryNode(1)
    root.left = BinaryNode(2)
    return root


def _gen_balanced_2():
    root = BinaryNode(7)
    root.left = BinaryNode(2)
    root.left.left = BinaryNode(4)
    root.right = BinaryNode(3)
    root.right.left = BinaryNode(8)
    root.right.right = BinaryNode(9)
    root.right.right.right = BinaryNode(10)
    return root


def _gen_unbalanced_1():
    root = BinaryNode(1)
    root.left = BinaryNode(2)
    root.left.left = BinaryNode(4)
    root.left.right = BinaryNode(5)
    root.left.right.right = BinaryNode(6)
    root.left.right.right.right = BinaryNode(7)
    root.right = BinaryNode(3)
    root.right.left = BinaryNode(8)
    root.right.right = BinaryNode(9)
    root.right.right.right = BinaryNode(10)
    root.right.right.right.right = BinaryNode(11)
    return root


def _gen_unbalanced_2():
    tree = BinaryNode(1)
    tree.left = BinaryNode(2)
    tree.right = BinaryNode(9)
    tree.right.left = BinaryNode(10)
    tree.left.left = BinaryNode(3)
    tree.left.right = BinaryNode(7)
    tree.left.right.right = BinaryNode(5)
    tree.left.left.left = BinaryNode(6)
    tree.left.right.left = BinaryNode(12)
    tree.left.right.left.left = BinaryNode(16)
    tree.left.right.left.right = BinaryNode(0)
    return tree

test_cases = [
    #(_gen_unbalanced_1, True),
    (_gen_balanced_2, True),
    #(_gen_unbalanced_1, False),
    (_gen_unbalanced_2, False),
]

testable_functions = [check_balanced]


def test_is_balanced():
    for tree_gen, expected in test_cases:
        for is_balanced in testable_functions:
            error_msg = f"{is_balanced.__name__} failed on {tree_gen.__name__}"
            assert is_balanced(tree_gen()) == expected, error_msg


if __name__ == "__main__":
    test_is_balanced()