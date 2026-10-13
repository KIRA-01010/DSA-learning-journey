# Counting Sort Algorithm
# Time Complexity:
    # On Avergae: O(n + k)
    # Best Case:  O(n)
    # Worst Case: O(n^2)

def countingSort(arr):
    if not arr:
        return arr

    # Creating an array "count" whose length matches
    # the max value in the given unsorted array
    count = [0] * (max(arr) + 1)

    # For every value in the unsorted array, the
    # corresponding index in the count array is
    # increased to match the number of times each
    # value occurs in the unsorted array
    for num in arr:
        count[num] += 1

    # unsorted array is then emptied
    arr[:] = []

    for num, freq in enumerate(count):
        arr.extend([num] * freq)

    return arr
    
unsorted_arr = [3,2,5,2,4,2,4,2,4]

sorted_arr = countingSort(unsorted_arr)
print(sorted_arr)
