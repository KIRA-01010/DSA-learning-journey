# Time Complexity:
# On Average: O(n*k)
# Best Case: O(n)
# On Average: O(n^2)
# if the number of digits k is something like
# k(n)=logn, time complexity: O(n⋅logn)

myArray = [170, 45, 75, 90, 802, 24, 2, 66]
print("Original array:", myArray)
radixArray = [[], [], [], [], [], [], [], [], [], []]
maxVal = max(myArray)
exp = 1

while maxVal // exp > 0:

    while len(myArray) > 0:
        val = myArray.pop()
        radixIndex = (val // exp) % 10
        radixArray[radixIndex].append(val)

    for bucket in radixArray:
        while len(bucket) > 0:
            val = bucket.pop()
            myArray.append(val)

    if exp == 1:
        print("First Sort:", myArray)
    if exp == 10:
        print("Second Sort:", myArray)

    exp *= 10

print("Final Sorted array:", myArray)