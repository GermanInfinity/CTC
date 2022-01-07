# grid traveller : how many ways can you travel a grid if you can only move right
# or down, path from top left to bottom right 

# base case
# row or col == 0 return 0 
# row, col == 1, 1 return 1

# use base cases for our tree

# Recursive solution, takes O(2^n) time and O(n) space. too slow
def grid_traveller(row, col): 
    if row == 0 or col == 0: return 0
    if row == 1 and col == 1: return 1

    ways = 0 

    ways += grid_traveller(row - 1, col) 
    ways += grid_traveller(row, col - 1) 

    return ways


print (grid_traveller(3, 3))


# DP solution
def grid_traveller(row, col, memo={}): 
    if str(row)+'.'+str(col) in memo: return memo[str(row)+'.'+str(col)]
    #if str(col)+'.'+str(row) in memo: return memo[str(row)+'.'+str(col)]

    if row == 0 or col == 0: return 0 
    if row == 1 and col == 1: return 1 

    memo[str(row)+'.'+str(col)] = grid_traveller(row - 1, col, memo) + grid_traveller(row, col - 1, memo)
    return memo[str(row)+'.'+str(col)]


print (grid_traveller(18, 18))