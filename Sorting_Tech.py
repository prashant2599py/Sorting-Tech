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


# Breadth First Search

graph = {
    'A' : ['B', 'C'],
    'B' : ['C', 'D', 'E'],
    'C' : ['D', 'F'],
    'D' : [],
    'E' : ['F'],
    'F' : []
}
visited = []
queue = []

def bfs(visited, graph, node):
    visited.append(node)
    queue.append(node)

    while queue:
        s = queue.pop(0)
        print(s, end=" ")

        for neighbour in graph[s]:
            if neighbour not in visited:
                visited.append(neighbour)
                queue.append(neighbour)

bfs(visited, graph, 'A')


# Depth First Search

graph = {
    'A' : ['B', 'C'],
    'B' : ['C', 'E'],
    'C' : ['F'],
    'D' : [],
    'E' : ['F'],
    'F' : []
}
visited = set()
def dfs(visited, graph, node):
    if node not in visited:
        print(node, end=" ")
        visited.add(node)
        for neighbour in graph[node]:
            dfs(visited, graph, neighbour)

dfs(visited, graph, 'A')


# Prim's Algorithm

INF = 9999999
Vertices = 4
Graph = [[0, 9, 75, 0],
         [9, 0, 95, 19],
         [75, 95, 0, 51],
         [0, 19, 51, 0]]

selected = [0, 0, 0, 0]
no_edge = 0
selected[0] = True
print("Edge : Weight")
while (no_edge < Vertices - 1):
    minimum = INF
    x = 0
    y = 0
    for i in range(Vertices):
        if selected[i]:
            for j in range(Vertices):
                if((not selected[j] and Graph[i][j])):
                    if minimum > Graph[i][j]:
                        minimum = Graph[i][j]
                        x = i
                        y = j
    print(str(x) + "-" + str(y) + ":" + str(Graph[x][y]))
    selected[y] = True
    no_edge += 1



#  Kruskal Algorithm

parent = dict()
rank = dict()

def make_set(vertice):
    parent[vertice] = vertice
    rank[vertice] = 0

def find(vertice):
    if parent[vertice] != vertice:
        parent[vertice] = find(parent[vertice])
    return parent[vertice]

def union(vertice1, vertice2):
    root1 = find(vertice1)
    root2 = find(vertice2)
    if root1 != root2:
        if rank[root1] > rank[root2]:
            parent[root2] = root1
        else:
            parent[root1] = root2
        if rank[root1] == rank[root2]: rank[root2] += 1

def kruskal(graph):
    global edges, minimum_spanning_tree
    for vertice in graph['vertices']:
        make_set(vertice)
        minimum_spanning_tree = set()
        edges = list(graph['edges'])
        edges.sort()

#For Printing the edges
    for edge in edges:
        weight, vertice1, vertice2 = edge
        if find(vertice1) != find(vertice2):
            union(vertice1, vertice2)
            minimum_spanning_tree.add(edge)
    return sorted(minimum_spanning_tree)

graph = {
'vertices': ['A', 'B', 'C', 'D', 'E', 'F', 'G'],
'edges': {(7, 'A', 'B'), (5, 'A', 'D'), (7, 'B', 'A'), (8, 'B', 'C'), (9, 'B', 'D'), (7, 'B', 'E'), (8, 'C', 'B'),
          (5, 'C', 'E'), (5, 'D', 'A'), (9, 'D', 'B'), (7, 'D', 'E'), (6, 'D', 'F'), (7, 'E', 'B'), (5, 'E', 'C'),
          (15, 'E', 'D'), (8, 'E', 'F'), (9, 'E', 'G'), (6, 'F', 'D'), (8, 'F', 'E'), (11, 'F', 'G'), (9, 'G', 'E'),
          (11, 'G', 'F')}
}
print(kruskal(graph))


# KnapSack Problem  (Maximum Profit with less Weight)

def knapSack(m, weight, profit, n):
   K = [[0 for x in range(m + 1)] for x in range(n + 1)]
   for i in range(n + 1):
      for j in range(m + 1):
         if i == 0 or j == 0:
            K[i][j] = 0
         elif weight[i-1] <= j:
            K[i][j] = max(profit[i-1] + K[i-1][j-weight[i-1]], K[i-1][j])
         else:
            K[i][j] = K[i-1][j]
   return K[n][m]
profit = [50,100,150,200]
weight = [8,16,32,40]
m = 64
n = len(profit)
print(knapSack(m, weight, profit, n))


# Matrix multiplication

import sys;

def MatrixMul(m, i, j):
    if i == j:
        return 0

    _min = sys.maxsize

    for k in range(i, j):

        count = (MatrixMul(m, i, k)
                 + MatrixMul(m, k + 1, j)
                 + m[i - 1] * m[k] * m[j])

        if count < _min:
            _min = count;

    return _min;


arr = [1, 2, 3, 4, 2];
n = len(arr);

print("Minimum number of multiplication is ",
      MatrixMul(arr, 1, n - 1));


