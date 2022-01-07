"""
	paths_with_sum.py: count paths that lead to sum. 
"""

def paths_with_sum(tree, target):
    if tree is None: return None
    stack = [ tree ]
    sum = 0 

    while stack: 
        current = stack[-1]

        sum += current

        if sum == target: 
            count += 1
        stack.pop()
        sum -= current



        if current.left: 
            stack.append(current.left)


