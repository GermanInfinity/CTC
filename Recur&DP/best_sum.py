# best_sum: return shortest sum

# O(n * m), O(m*m)
def best_sum(target, array, memo={}):
    if target in memo: return memo[target]

    if target == 0: return []
    if target < 0: return None

    first = True
    resp = None
    min_arr = []
    for num in array: 
        if target - num >= 0: 
            resp = best_sum(target-num, array)
            if resp is not None: 
                resp = resp + [num]
                if len(resp) < len(min_arr) or first: 
                     min_arr = resp
                     first = False

                memo[target] = min_arr


    memo[target] = min_arr
    return min_arr


print (best_sum(100, [1,2,9]))
# O(n^m * m), O(m)
def best_sum_recur(target, array):
    if target == 0: return []
    if target < 0: return None

    first = True
    resp = None
    min_arr = []
    for num in array: 
        if target - num >= 0: 
            resp = best_sum_recur(target-num, array)
            if resp is not None: 
                resp = resp + [num]
                if len(resp) < len(min_arr) or first: 
                     min_arr = resp
                     first = False
   
    return min_arr


print (best_sum_recur(100, [1,2,9]))