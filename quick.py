def quicksort(arr):
    if len(arr) <= 1:
        print(arr)
        return arr
    pivot = sum(arr) // len(arr) 
    print(pivot)
    left = [x for x in arr if x < pivot]
    print(left)
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    print(right)
    return quicksort(left) + middle + quicksort(right)


vector = [9,5,7]
organizado = quicksort(my_list)
print(organizado)
