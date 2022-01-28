def quicksort(arr):
    if len(arr)==0 or len(arr) == 1:
        return arr
    elif len(arr) == 2:
        if arr[0] >arr[1]:
            arr[0] = arr[0] + arr[1]
            arr[1] = arr[0] - arr[1]
            arr[0] = arr[0] - arr[1]
            return arr
        else:
            return arr
    else:

        arr1 =[]
        arr2 = []
        for i in range(1, len(arr)):
            if arr[i]<arr[0]:
                arr1.append(arr[i])
            if arr[i]>arr[0]:
                arr2.append(arr[i])
        arr1 = quicksort(arr1)
        arr2 = quicksort(arr2)
        arr = arr1 + [arr[0]] + arr2
        return arr

arr = [23, 5 ,11, 7]
print(quicksort(arr))