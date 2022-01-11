## canSum.py: function returns true if can find sum of target in array 
# Decision problem

def can_sum(target, array, memo={}): 

    if target in memo: return memo[target]

    if target == 0: return True
    if target < 0: return False
    
    res = False
    for ele in array: 
        if target - ele >= 0: 
            #memo[target] = res or can_sum(target - ele, array, memo)
            if can_sum(target - ele, array, memo): 
                memo[target] = True
                return True

    memo[target] = False
    return False


# time O(n^target) space O(m)
def can_sum_recur(target, array): 
    if target == 0: return True
    if target < 0: return False

    res = False
    for num in array: 
        if target - num >= 0:
            res = res or can_sum_recur(target - num, array)

    return res

    


print (can_sum(300, [7,14]))