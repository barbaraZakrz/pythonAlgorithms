def binary_search(myList, item):
    low = 0
    high = (len(myList)-1)


    while (low <=high):
        mid = int((low + high) / 2)
        guess = myList[mid]
        if guess == item:
            return mid +1
        if guess < item:
            low = mid +1
        else:
            high = mid -1
    return None


myList = [1, 2, 3, 4, 5, 6, 7, 8]
print(binary_search(myList, 89))