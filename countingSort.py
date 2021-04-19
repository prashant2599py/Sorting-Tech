# Counting Sort

def counting_sort(a):
    size = len(a)
    count = max(a)
    A = []
    B = []
    for i in range(0, count + 1):
        B.append(0)
    for i in range(0, size):
        A.append(0)
    for j in range(0, size):
        B[a[j]] += 1
    for i in range(1, count + 1):
        B[i] += B[i - 1]
    for j in reversed(range(size)):
        A[B[a[j]] - 1] = a[j]
        B[a[j]] -= 1
    return A


array = [2, 0, 3, 4, 2, 1, 0, 3]
print("Original Array:", array)
print("Sorted Array:", counting_sort(array))