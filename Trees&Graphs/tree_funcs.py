"""
    random_node.py: binary tree class with functions, insert, find, delete. 
"""

class Node: 
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right 

    def insert(self, node):  # iterative solution
        if node is None: return None

        ptr = self
        not_inserted = True
        while not_inserted and ptr:
            if ptr.value <= node.value: 
                if ptr.right: 
                    ptr = ptr.right
                else: 
                    ptr.right = node
                    not_inserted = False

            elif ptr.value > node.vale: 
                if ptr.left: 
                    ptr = ptr.left
                else: 
                    ptr.left = node
                    not_inserted = False
        if not_inserted: self = node


    def find(self, node): 
        if node is None: return False
        if self.value == node.value:
            return True

        if self.left: 
            left = self.left.find(node)

        if left: return True
        right = self.right.find(node)

        return right
        

    def delete(self, node): 
        pass

    def random(self):
        pass


# Driver Code
if __name__ == '__main__':
    root = Node(0)
    root.left = Node(1)
    root.left.left = Node(3)
    root.left.left.left = Node(7)
    root.left.right = Node(4)
    root.left.right.left = Node(8)
    root.left.right.right = Node(9)
    root.right = Node(2)
    root.right.left = Node(5)
    root.right.right = Node(6)


    print (root.find(Node(4)))


