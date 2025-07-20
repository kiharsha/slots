def IsMonotonic(arr):
    increasing = decreasing = True

    for i in range(1,len(arr)):
        if arr[i] > arr[i-1]:
            decreasing = False
        elif arr[i] < arr[i-1]:
            increasing = False

    return increasing or decreasing


arr = [1, 2, 2, 3]
arr1 = [3, 2, 1, 0]
arr2 = [4,2,4,1]
print(IsMonotonic(arr))
print(IsMonotonic(arr1))
print(IsMonotonic(arr2))