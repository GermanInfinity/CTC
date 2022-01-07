# Selection sort

# Bubble sort: loops through array and swaps smaller elements with current.
# O(n^2), space O(1)
# optimized buy adding swapped variable 
for i in range(len(nums1)):
    for x in range(len(nums1)-1):
        if nums1[x] > nums1[x + 1]: #self.swap(nums1, x, x+1)
            temp = nums1[x + 1]
            nums1[x + 1] = nums1[x]
            nums1[x] = temp
                    
# Selection sort: loops through array and selects minimum to swap with 
# best: O(n^2), avergae: O(n^2), space O(1)
for i in range(len(nums1)):
    min_num = nums1[i]
    for x in range(i+1, len(nums1)):
        if nums1[x] < min_num:
            min_num_i = x
            min_num = nums1[x]
            
    temp = nums1[i]
    nums1[i] = min_num
    nums1[min_num_i] = temp
            

# Insertion sort: inserting elements in the front if less
# O(n^2), space O(1)
def insertionSort(array):

    for step in range(1, len(array)):
        key = array[step]
        j = step - 1
        
        # Compare key with each element on the left of it until an element smaller than it is found
        # For descending order, change key<array[j] to key>array[j].        
        while j >= 0 and key < array[j]:
            array[j + 1] = array[j]
            j = j - 1
        
        # Place key at after the element just smaller than it.
        array[j + 1] = key

# merge sort: divide and conquer approach 
# best: O(nlogn), average: O(nlogn), worst: O(nlogn), space: O(n)



# QUICKSORT
# best: O(nlogn), average: O(n^2), worst: O(nlogn), space: O(logn)

# function to find the partition position
def partition(array, low, high):

  # choose the rightmost element as pivot
  pivot = array[high]

  # pointer for greater element
  i = low - 1

  # traverse through all elements
  # compare each element with pivot
  for j in range(low, high):
    if array[j] <= pivot:
      # if element smaller than pivot is found
      # swap it with the greater element pointed by i
      i = i + 1

      # swapping element at i with element at j
      (array[i], array[j]) = (array[j], array[i])

  # swap the pivot element with the greater element specified by i
  (array[i + 1], array[high]) = (array[high], array[i + 1])

  # return the position from where partition is done
  return i + 1

# function to perform quicksort
def quickSort(array, low, high):
  if low < high:

    # find pivot element such that
    # element smaller than pivot are on the left
    # element greater than pivot are on the right
    pi = partition(array, low, high)

    # recursive call on the left of pivot
    quickSort(array, low, pi - 1)

    # recursive call on the right of pivot
    quickSort(array, pi + 1, high)




# BINARY SEARCH 
# best: O(1), average: O(logn), worst: O(logn), space: O(1)
# Applications: used to pinpoint location of error in debugging
# Iterative and recurvise implementations

#Iterative 
def binarySearch(array, x, low, high):

    # Repeat until the pointers low and high meet each other
    while low <= high:

        mid = low + (high - low)//2

        if array[mid] == x:
            return mid

        elif array[mid] < x:
            low = mid + 1

        else:
            high = mid - 1

    return -1
    
# Recursive 
def binarySearch(array, x, low, high):

    if high >= low:

        mid = low + (high - low)//2

        # If found at mid, then return it
        if array[mid] == x:
            return mid

        # Search the left half
        elif array[mid] > x:
            return binarySearch(array, x, low, mid-1)

        # Search the right half
        else:
            return binarySearch(array, x, mid + 1, high)

    else:
        return -1
