def MultipleNumberInList(arr):
    if arr[0]<=0:
        sum = 0
    elif arr[0]>0:
        sum =1
        for i in range(len(arr)):
            sum = sum * arr[i]
    return sum


arr = [6, 4, 2, 1]
print(MultipleNumberInList(arr))