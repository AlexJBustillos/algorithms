# Merge
# divide array until it has one index
# merge items while sorting
# repeat the process till array is complete
arr = [21, 27, 23, 20, 21, 25, 15]
def merge_sorted(arr):
    if len(arr) <= 1:
        return arr
    split = len(arr)//2
    left = arr[:split]
    right = arr[split:]

    right = merge_sorted(right)
    left = merge_sorted(left)

    return merge(left, right)

def merge(a, b):
    sorted = []
    i = j = 0

    while i < len(a) and j < len(b):
        if a[i] <= b[j]:
            sorted.append(a[i])
            i += 1
        else: 
            sorted.append(b[j])   
            j += 1
    while i < len(a):
        sorted.append(a[i])
        i += 1
    while j < len(b):
        sorted.append(b[j])
        j += 1

    return sorted

print(merge_sorted(arr))