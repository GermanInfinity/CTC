# how_sum: retun array that adds up to target sum 

# comibinatoric problem 

def how_sum(target, array, memo={}):
    if target in memo: return memo[target]

    if target == 0: return []
    if target < 0: return None  

    resp = None
    for num in array: 
        if target - num >= 0: 
            resp = how_sum(target - num, array, memo)
            memo[target] = resp + [num]
            return memo[target]

    memo[target] = None
    return None



print (how_sum(20, [7, 3, 8]))
print (how_sum(7, [2, 3]))

# time O(n^target * target) space O(m*m)
def how_sum_recur(target, array): 
    if target == 0: return []
    if target < 0: return None  

    resp = None
    for num in array: 
        if target - num >= 0:
            resp = how_sum_recur(target - num, array)
            if resp is not None: 
                #resp.append(num)
                return resp + [num]
            

    return resp


print (how_sum_recur(20, [7, 3, 8]))
print (how_sum_recur(7, [2, 3]))