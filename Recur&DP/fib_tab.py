# fib tabulation
# building a table, iterative dp

# initialize every poistion in table n + 1 to 0 
# 

def fib(n): 
    table = (n + 1) * [0]
    table[1] = 1

    for i in range(2, len(table)):
       table[i] = table[i-1] + table[i-2]

    return table[n]


print (fib(6))
print (fib(7))
print (fib(8))
print (fib(50))