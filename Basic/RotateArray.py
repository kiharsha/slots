def rotatearray(arr1, count):
    n = len(arr1)
    if count<0 and count> len(arr1):
        return "Invalid rotation value"

    rotated_arr = [0] * n
    print(len(rotated_arr))

    for i in range(n):
        print(f"i = ", i)
        print(f"index = ", (i+count) % n)
        rotated_arr[i] = arr1[(i + count) % n]
    return rotated_arr


arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
countofrotate = 3
arr = rotatearray(arr, countofrotate)
print(arr)
