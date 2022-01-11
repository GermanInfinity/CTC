"""
    stack_min.py: implement a stack with push, pop and min. 
"""

class stack: 
    def __init__(self): 
        self.stack = []
        self.min_stack = []

    def push(self, element): 
        self.stack.append(element)
        if self.min_stack: 
            sel.min_stack.append(min(element, self.min_stack[-1]))
        else: 
            self.min_stack.append(element)


        
    def pop(self, element): 
        self.self.stack.pop(-1)
        self.self.min_stack.pop(-1)

    def getMin(self): 
        return self.min_stack[-1]