# Merge Sort

def mergeSort(array):
    if len(array) > 1:
        mid = len(array) // 2
        left_array = array[: mid]
        right_array = array[mid:]
        mergeSort(left_array)
        mergeSort(right_array)

        i = 0
        j = 0
        k = 0
        while i < len(left_array) and j < len(right_array):
            if left_array[i] < right_array[j]:
                array[k] = left_array[i]
                i = i + 1
                k = k + 1
            else:
                array[k] = right_array[j]
                j = j + 1
                k = k + 1

        while i < len(left_array):
            array[k] = left_array[i]
            i = i + 1
            k = k + 1

        while j < len(right_array):
            array[k] = right_array[j]
            j = j + 1
            k = k + 1

array = [12 , 45 , 6 , 0 , 23 ]
mergeSort(array)
print("Sorted array is:", array)