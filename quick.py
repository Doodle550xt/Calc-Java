def quicksort(arr):
    if len(arr) <= 1:
        print(arr)
        return arr
    pivot = sum(arr) // len(arr)  # Elige el valor medio del arreglo como pivote
    print(pivot)
    left = [x for x in arr if x < pivot]
    print(left)
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    print(right)
    return quicksort(left) + middle + quicksort(right)

# Ejemplo de uso
my_list = [9,5,7]
sorted_list = quicksort(my_list)
print(sorted_list)
