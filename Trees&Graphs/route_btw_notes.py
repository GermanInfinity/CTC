"""
    route_btw_nodes.py: Find out if there is a route between nodes
                        in a graph.
"""

# BFS between two given nodes. 
# Algorithm takes tree and both nodes. 

# BFS: Queue
# start at given node
# put nodes children into a queue 
# process until the queue is empty 
# if I saw finish node, I would return True 

from TreeNode import Node
import random 

def find_relationship_recur(tree, start, end): 
    if tree and start and end: 
        return helper(tree, start, False, end, False)

def helper(tree, start, visit_started, end, visit_end): 
    if tree is None: return 

    if tree.value == start: visit_started = True
    if tree.value == end: visit_end = True

    left = helper(tree.left, start, visit_start, end, visit_end)
    right = helper(tree.right, start, visit_start, end, visit_end)

    return left and right 

    
def find_relationship(tree, start, end): 
    if tree and start and end: 
        queue = [ start ] 
        
        while len(queue) > 0: 
            current = queue[-1]
            queue = queue[1:]

            if current == end: return True 

            if current: 
                if current.left: 
                    queue.append(current.left)
                if current.right: 
                    queue.append(current.right)


        return False 


if __name__=="__main__": 

    tree = Node(27)
    # num_list = [14,35,10,19,31,42]
    node_list = [Node(14),Node(35),Node(10),Node(19),Node(31),Node(42)]
    

    # print ("Post-order from Number insert")
    # for i in num_list:
    #     tree.insert(i)

    # tree.post_order()

    print ("\n")
    print ("\n")
    print ("\n")

    print ("Post-order from Node insert")  
    #tree = Node(27)
    for i in node_list:
        tree.insert_node(i)
    tree.post_order()


    #assert(find_relationship(tree, 14, 35), True)