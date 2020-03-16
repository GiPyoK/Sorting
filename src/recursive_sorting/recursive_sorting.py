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

    return arr

def merge_sort_in_place(arr, l, r): 
    # TO-DO

    return arr


# STRETCH: implement the Timsort function below
# hint: check out https://github.com/python/cpython/blob/master/Objects/listsort.txt
def timsort( arr ):

    return arr