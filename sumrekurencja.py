def sum(arr):
    i=0
    wynik =0
    if len(arr) ==1:
        return arr[0]
    else:
         wynik = arr[i]+sum(arr[i+1:])
    return wynik

def maxV(arr):
    max = arr[0]
    for j in range(1,len(arr)):
        if max < arr[j]:
            max = arr[j]
    return max

print(sum([1,2,3,8]))
print(maxV([1,8,366,56]))