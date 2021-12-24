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


def find_relationship(tree, start, end): 
    if tree and start and end: 
        queue = [ start ] 
        
        while len(queue) > 0: 
            current = queue[-1]
            queue = queue[1:]

            if current == end: return True 

            for child in current: 
                queue.append(child) 



        return False 