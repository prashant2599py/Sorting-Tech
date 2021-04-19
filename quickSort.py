# Quick Sort

def pivot_placed(list,first,last):
    pivot = list[last]
    left = first
    right = last-1
    while True:
         while left <= right and list[left] <= pivot:
           left = left + 1
         while left<=right and list[right] >= pivot:
           right = right - 1
         if right<left:
           break
         else:
              list[left],list[right] = list[right],list[left]
    list[last],list[left ] = list[left],list[last]
    return left

def quickSort(list,first,last):
    if first<last:
        p = pivot_placed(list,first,last)
        quickSort(list,first,p-1)
        quickSort(list,p+1,last)
#main
list = [56 , 26 , 93 , 17 , 31 , 44]
n = len(list)
quickSort(list,0,n-1)
print(list)