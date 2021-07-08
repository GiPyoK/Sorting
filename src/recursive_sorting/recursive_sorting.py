# TO-DO: complete the helpe function below to merge 2 sorted arrays
def merge( arrA, arrB ):
    elements = len( arrA ) + len( arrB )
    merged_arr = [0] * elements
    # TO-DO
    index = 0

    while len(arrA) > 0 and len(arrB) > 0:
        if arrA[0] < arrB[0]:
            merged_arr[index] = arrA[0]
            arrA.remove(arrA[0])
            index += 1
        else:
            merged_arr[index] = arrB[0]
            arrB.remove(arrB[0])
            index += 1

    while len(arrA) > 0:
        merged_arr[index] = arrA[0]
        arrA.remove(arrA[0])
        index += 1

    while len(arrB) > 0:
        merged_arr[index] = arrB[0]
        arrB.remove(arrB[0])
        index += 1
    
    return merged_arr


# TO-DO: implement the Merge Sort function below USING RECURSION
def merge_sort( arr ):
    # TO-DO
    if len(arr) == 1 or len(arr) == 0:
        return arr

    half_index = len(arr) // 2

    arr1 = arr[ : half_index]
    arr2 = arr[half_index : ]

    arr1 = merge_sort(arr1)
    arr2 = merge_sort(arr2)

    return merge(arr1,  arr2)


# STRETCH: implement an in-place merge sort algorithm
def merge_in_place(arr, start, mid, end):
    # TO-DO
    temp = []
    if mid - start > end - mid: # make copy of smaller portion of arr
        temp = arr[mid : end + 1]
        end_index_l = mid - 1
        end_index_r = end
        for _ in range(mid - start): # shift right the left array
            arr[end_index_r] = arr[end_index_l]
            end_index_l -= 1
            end_index_r -= 1
    else:
        temp = arr[start : mid + 1]

    while :

        

        count -= 1

    return arr

def merge_sort_in_place(arr, l, r): 
    # TO-DO
    # arr = [4,2,5,1]
    # l = 0, r = 3
    m = (l - r) // 2 # m = 1

    merge_sort_in_place(arr, l, m) # merge_sourt_in_place(arr, 0, 1)
    merge_sort_in_place(arr, m + 1, r) # merge_sourt_in_place(arr, 2, 3)

    return merge_in_place(arr, l, m, r)


# STRETCH: implement the Timsort function below
# hint: check out https://github.com/python/cpython/blob/master/Objects/listsort.txt
def timsort( arr ):

    return arr