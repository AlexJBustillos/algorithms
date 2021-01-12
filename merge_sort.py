def merge(arr1, arr2):
    output = []
    start_length_arr1 = len(arr1)
    start_length_arr2 = len(arr2)
    target_output_length = start_length_arr1 + start_length_arr2
    
    # another way to do while loop
    # while len(arr1) > 0 or len(arr2) > 0
    while len(output) < target_output_length:
        print('--------')
        print('arr1: ', arr1)
        print('arr2: ', arr2)
        print('output: ', output)

        if len(arr1) == 0:
            output += arr2
            arr2 = []
        # do same for arr2
        elif len(arr2) == 0:
            output += arr1
            arr1 = []
        elif arr1[0] < arr2[0]:
            output.append(arr1[0])
            arr1 = arr1[1:]
        else:
            output.append(arr2[0])
            arr2 = arr2[1:]

    return output

# print(merge([1,3], [2,4]))
# print(merge([4], [2]))


def split(arr):
    print('Splitting: ', arr)
    middle = len(arr) // 2
    arr1 = arr[:middle]
    arr2 = arr[middle:]
    # print(arr1, arr2)
    if len(arr1) <= 1 and len(arr2) <= 1:
        return merge(arr1, arr2)
    
    split1 = split(arr1)
    split2 = split(arr2)
    return merge(split1, split2)



print('Final result: ', split([1,5,8,4,6,10,9,7]))