def partition(array, low, high):
    pivot = array[high]
    i = low - 1

    for j in range(low, high):
        if array[j] <= pivot:
            i += 1
            array[i], array[j] = array[j], array[i]

    array[i + 1], array[high] = array[high], array[i + 1]
    return i + 1

def quicksort(array, low = 0, high = None):
    if high == None:
        high = len(array) - 1

    if low < high:
        # sets/updates the pivot, according to which the
        # remaining elements/values are sorted
        pivot_index = partition(array, low, high)
        # sorts the elements/values on the left side of the pivot
        quicksort(array, low, pivot_index-1)
        # sorts the elements/values on the right side of the pivot
        quicksort(array, pivot_index+1, high)

my_array = [4,2,5,7,3,2,6,1,7]
print("Original array", my_array)

quicksort(my_array)
print("QuickSorted array:", my_array)