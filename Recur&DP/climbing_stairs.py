# climbing_stairs.py: number of ways to climb n stairs 


def climbing_stairs(n, steps): 
    if n == 0: return True 
    if n < 0: return False 

    val = 0 
    for step in steps: 
        if climbing_stairs(n - step, steps):
            val += 1

    return val


print (climbing_stairs(3, [1,2]))
