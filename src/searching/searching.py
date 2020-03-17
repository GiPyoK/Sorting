# STRETCH: implement Linear Search				
def linear_search(arr, target):
  
  # TO-DO: add missing code
  for i in range(len(arr)):
    if arr[i] == target:
      return i

  return -1   # not found


# STRETCH: write an iterative implementation of Binary Search 
def binary_search(arr, target):
  # TO-DO: add missing code
  newArr = arr # create a copy of arr to avoid mutating the original copy
  low = 0
  index = 0
  mid = len(arr)

  while mid != 0:

    mid = len(newArr) // 2
    index = mid + low # keep track of original index of arr to return.

    if newArr[mid] == target:
      return index
    elif newArr[mid] > target:
      newArr = newArr[ : mid] # overwrite newArr from start to mid - 1
    else:
      newArr = newArr[mid + 1: ] # overwrite newArr from mid + 1 to end
      low = low + mid + 1

  return -1 # not found


# STRETCH: write a recursive implementation of Binary Search 
def binary_search_recursive(arr, target, low, high):
  
  middle = (low+high)//2

  if len(arr) == 0:
    return -1 # array empty
  # TO-DO: add missing if/else statements, recursive calls
  if arr[middle] == target:
    return middle
  elif arr[middle] > target:
    return binary_search_recursive(arr, target, low, middle - 1)
  else:
    return binary_search_recursive(arr, target, middle + 1, high)