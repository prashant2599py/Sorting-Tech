 # Bubble Sort
array = [34, 22, 12, 10, 6, 45, 36]
print("Original array is: ", array)
n = len(array)
for i in range(n):
    for j in range(0, n - i - 1):
        if array[j] > array[j + 1]:
            array[j], array[j + 1] = array[j + 1], array[j]
            print("array after sorting:", array)

# Selection Sort

Array = [64, 25, 12, 22, 11]
for i in range(len(Array)):

    min_index = i
    for j in range(i + 1, len(Array)):
        if Array[min_index] > Array[j]:
            min_index = j

    Array[i], Array[min_index] = Array[min_index], Array[i]

print("Sorted array",Array)