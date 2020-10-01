def linear_search(arr, target):
    # Your code here
    for i in range(len(arr)):
        if arr[i] == target:
            return i

    return -1   # not found


# Write an iterative implementation of Binary Search
def binary_search(arr, target):
    # Your code here
    return search_recursive(0, len(arr), arr, target)


    return -1  # not found


def search_recursive(left, right, arr,target):
    if left > right or len(arr) == 0:
        return -1
    middle = (left + right) // 2
    value = arr[middle]
    if value == target:
        return middle
    elif target < value:
        return search_recursive(left, middle, arr, target)
    else:
        return search_recursive(middle + 1, right, arr, target)
    
