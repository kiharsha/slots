def splitarray(arr1, count):
    if k<= 0 and k >= len(arr1):
        return arr1
    first_part = arr1[:k]
    second_part = arr1[k:]
    result = second_part + first_part
    return result


arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
k = 5
arr = splitarray(arr, k)
print(arr)
