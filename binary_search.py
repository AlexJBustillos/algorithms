def binary_search(arr, target):
    low = 0
    high = len(arr) - 1

    while low <= high:
        middle = (low + high)// 2
    
        if arr[middle] == target:
            return middle
        elif arr[middle] > target:
            high = middle - 1
        else:
            low = middle + 1
    return -1

# print(binary_search([1, 3, 7, 15, 26, 27, 30, 32, 45], 6))

def binary_rec(arr, target, lost_index = 0):
    if len(arr) == 0:
        return -1
    
    middle = len(arr) // 2
    middle_value = arr[middle]
    low = arr[:middle]
    high = arr[middle + 1:]

    if middle_value == target:
        return middle + lost_index
    elif len(arr) == 1 and middle_value != target:
        return -1
    elif middle_value < target:
        return binary_rec(high, target, middle + 1 + lost_index)
    elif middle_value > target:
        return binary_rec(low, target, lost_index)

print(binary_rec([1, 3, 7, 15, 26, 27, 30, 32, 45], 3))
