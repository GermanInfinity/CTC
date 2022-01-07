# recurvie multiply: recursively multiply two numbers


def recur_mult(a, b): 
    if b == 0: return 0

    sum_val = 0 
    sum_val += recur_mult(a, b - 1) + a

    return sum_val


print (recur_mult(12, 4))