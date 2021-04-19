array = [15,6,56,34,2,3,33]
print("Original array is: ", array)
for i in range(1, len(array)):
    key = array[i]
    j = i-1
    while j >= 0 and key < array[j]:
        array[j+1] = array[j]
        j = j - 1
    else:
        array[j+1] = key
        print("Array after sorting:", array)