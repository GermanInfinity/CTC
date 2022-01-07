"""
   list_of_levels.py: stores levels of tree in list
   list_of_depths.py: stores depths of tree in list
"""
from collections import deque 
class BinaryNode:
    def __init__(self, name, left=None, right=None):
        self.name = name
        self.left = left
        self.right = right

def create_node_list_by_depth(tree_root):
    # BFS.
    levels = {}
    q = deque()
    q.append((tree_root, 0))

    while len(q) > 0:
        node, level = q.popleft()
        print (level)
        if level not in levels:
            # First node in the level
            levels[level] = []
        # Nodes already exist
        levels[level].append(node.name)

        # Push onto queue
        if node.left:
            q.append((node.left, level + 1))
        if node.right:
            q.append((node.right, level + 1))
    return levels

def level_nodes(root): # Implement without arrays but with deque
    if root: 
        # DFS
        # Store with dictionary 
        level, levels, queue = 0, {}, [ root ]
        levels[0] = [root.name]
        while queue: 
            level += 1

            node = queue[0]
            queue = queue[1:]
 
            if level in levels: levels[level].append(node.name)
            else: levels[level] = [node.name]

            if node.left: queue.append(node.left)
            if node.right: queue.append(node.right)

        return levels

    else: return 


def level_nodes_recur(root): 
    if root is None: return 
    helper(0, {}, root)

def helper(level, levels, node):
    if node is None: return levels 

    if level in levels: levels[level].append(node.name)
    else: levels[level] = [node.name]

    level += 1

    helper(level, levels, node.right)
    helper(level, levels, node.left)
    return levels


/*
 * node - node being visited
 * clevel - current level
 * rlevel - requested level
 * result - result queue
 */
def find_all_on_level(node, clevel, rlevel, result):
    if (clevel == rlevel):
        result.enqueue (node);
    else:
    if (node.left != null)
      drill (node.left, clevel + 1, rlevel, result);
    if (node.right != null)
      drill (node.right, clevel + 1, rlevel, result);
 

testable_functions = [level_nodes, level_nodes_recur]


def test_level_nodes():
    for f in testable_functions:
        node_h = BinaryNode("H")
        node_g = BinaryNode("G")
        node_f = BinaryNode("F")
        node_e = BinaryNode("E", node_g)
        node_d = BinaryNode("D", node_h)
        node_c = BinaryNode("C", None, node_f)
        node_b = BinaryNode("B", node_d, node_e)
        node_a = BinaryNode("A", node_b, node_c)
        lists = f(node_a)

        assert lists[0].values() == [node_a.name]
        assert lists[1].values() == [node_b.name, node_c.name]
        assert lists[2].values() == [node_d.name, node_e.name, node_f.name]
        assert lists[3].values() == [node_h.name, node_g.name]

def example():
    root = BinaryNode(0)
    root.left = BinaryNode(1)
    root.right = BinaryNode(2)
    root.left.left = BinaryNode(3)
    root.left.right = BinaryNode(4)
    root.right.left = BinaryNode(5)
    root.right.right = BinaryNode(6)

    levels = level_nodes_recur(root)
    print(levels)


if __name__ == "__main__":
    example()