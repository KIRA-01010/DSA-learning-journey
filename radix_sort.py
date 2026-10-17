# It is Stable.
# Time Complexity:
# On Average: O(n*k)
# Best Case: O(n)
# On Average: O(n^2)
# if the number of digits k is something like
# k(n)=logn, time complexity: O(n⋅logn)

an_array = [33,5,6,34,6,77,654,43,65,66]
print("Original Array:", an_array)

radix_array = [[], [], [], [], [], [], [], [], [], []]
max_val = max(an_array)

exp = 1

while max_val // exp > 0:

    while len(an_array) > 0:
        val = an_array.pop()
        radix_index = (val // exp) % 10
        radix_array[radix_index].append(val)

    for bucket in radix_array:
        while len(bucket) > 0:
            val = bucket.pop()
            an_array.append(val)

    exp *= 10

print("Sorted Array:", an_array)