def binary_search(arr, target): 
    if len(arr) == 0: return None
    start, end = 0, len(arr) - 1
    
    while start <= end: 
        mid = (start + end) // 2
        if target == arr[mid]: return True 
        
        if target > arr[mid]:
            start = mid + 1
        else: 
            end = mid - 1
            
    return False
    
def binary_search_recur(arr, target): 
    return helper(arr, target, 0, len(arr)-1)
    
def helper(array, target, start, end): 
    if start > end: return False
    mid = (start + end) // 2
    
    if array[mid] == target: 
        return True 
    
    if target > array[mid]: 
        return helper(array, target, mid + 1, end)
    else: 
        return helper (array, target, start, mid - 1)
        
    
array = sorted([2,3,5,6,7,-1,-12,-80,800,34,-600])
print (array)
print (binary_search(array, 800))
            