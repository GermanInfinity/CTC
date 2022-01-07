
class Node:
    def __init__(self, val):
        self.value = val
        self.left, self.right = None, None

    ### Me after a little review. 
    def insert(self, val):
        if self.value: 
            if val < self.value: 
                if self.left: 
                    self.left.insert(val)
                else: 
                    self.left = Node(val)
            elif val >= self.value:
                if self.right: 
                    self.right.insert(val)
                else: 
                    self.right = Node(val)
        else: 
            self.value = val

    def insert_node(self, node):
        if self.value: 
            if node.value < node.value: 
                if self.left:
                    self.left.insert_node(node)
                else: 
                    self.left = node
            elif node.value >= self.value : 
                if self.right: 
                    self.right.insert_node(node)
                else: 
                    self.right = node
        else: 
            self.value = node.value


        

    def post_order(self): 
        if self.left: 
            self.left.post_order()
        if self.right: 
            self.right.post_order()
        print (self.value)


  


### Me not coding it correctly. Missed out on 3 if statements. 

class Tree: 
    def __init__(self, root_val):
        self.root = Node(root_val, None, None)
        
    def insert(self, val): 
        ptr = self.root

        if val < ptr.value:
            ptr = helper(ptr.left)
            ptr.left = Node(val)
        elif val > ptr.value: 
            ptr = helper(ptr.right)
            ptr.right = Node(val)

    def helper(self, val, node): 
        if node is None: return 
        ptr = node
        if val < ptr.value: 
            helper(val, ptr.left)
        elif val >= ptr.value: 
            helper(val, ptr.right)
       


