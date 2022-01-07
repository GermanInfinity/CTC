""" 
    merge_sort.py: merge sort algorithm 
"""
def merge_sort_recur(array):
    if len(array) > 1: 
        half = len(array) // 2
        left = array[:half]
        right = array[half:]

        merge_sort_recur(left)
        merge_sort_recur(right)

        i, j, k = 0, 0, 0

        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                array[k] = left[i]
                i += 1
                k += 1

            else: 
                array[k] = right[j]
                j += 1
                k += 1

        while i < len(left):# collect from left
            array[k] = left[i]
            i += 1
            k += 1

        while j < len(right):# 
            array[k] = right[j]
            j += 1
            k += 1

        return array

    

def merge_sort_iter(array):
    if len(array) == 1: return array

    half = len(array) // 2
    left = array[:half]
    right = array[half:]

    return merge((merge_sort_iter(left)), merge_sort_iter(right))


def merge(left, right):

    res = []
    i, j = 0, 0

    while i < len(left) and j < len(right): 
        if left[i] < right[j]:
            res.append(left[i])
            i += 1
        else: 
            res.append(right[j])
            j += 1
    res.append(left[i])
    res.append(right[j])
    return res



if __name__=="__main__": 
    print (merge_sort_recur([5,4,3,-1,190]))
    #print (merge_sort_iter([5,4,3,-1,190]))
    #assert(merge_sort_iter([5,4,3,-1,190]), [-1,3,4,5,190])